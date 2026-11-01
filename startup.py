#!/usr/bin/env python3
import os
import sys
import toml
from playwright.sync_api import sync_playwright
import subprocess

CONFIG_FILE = "config.toml"

def load_config(path=CONFIG_FILE):
    if not os.path.exists(path):
        print(f"Config file not found: {path}")
        return {}
    return toml.load(path)


def main():
    cfg = load_config()
    headless = os.environ.get("HEADLESS", str(cfg.get("headless", False))).lower() in ("1", "true", "yes")
    username = os.environ.get("WOCABEE_USERNAME") or cfg.get("username", "")
    password = os.environ.get("WOCABEE_PASSWORD") or cfg.get("password", "")
    double_points = os.environ.get("WOCABEE_DOUBLE_POINTS", str(cfg.get("double_points", False))).lower() in ("1", "true", "yes")
    class_index = int(os.environ.get("WOCABEE_CLASS_INDEX", cfg.get("class_index", 0)))
    package_index = int(os.environ.get("WOCABEE_PACKAGE_INDEX", cfg.get("package_index", 0)))
    urlbase = cfg.get("urlbase", "https://wocabee.app/app")

    if not username or not password:
        print("Missing credentials. Launch using: python bot.py")
        sys.exit(1)

    def enable_double_points(page):
        try:
            # Wait for wrapper instead of input visibility
            page.wait_for_selector("#toggleWrapper", timeout=5000)

            toggle = page.locator("#levelToggle")

            # Check state directly (hidden is fine)
            is_checked = toggle.is_checked()

            if not is_checked:
                # Click the visible slider, not the hidden input
                page.locator("#toggleWrapper .slider").click()
                print("Double points enabled.")
            else:
                print("Double points already enabled.")

            return True

        except Exception as e:
            print("Failed to enable double points:", e)
            return False
    
    def click_package_by_index(page, index: int):
        page.wait_for_selector("tr.pTableRow, tr.packageTableRow", timeout=15000)

        packages = page.locator("tr.pTableRow, tr.packageTableRow")

        count = packages.count()
        if index < 0 or index >= count:
            print(f"Package index {index} out of range. Found {count} packages.")
            return False

        print(f"Clicking package {index}")

        # Click practice button inside that row
        row = packages.nth(index)
        links = row.locator("td:nth-child(4) a, a.btn-primary, a:has(.btn-primary)")
        if links.count() == 0:
            raise RuntimeError("No practice link found for selected package; WocaBee UI may have changed.")
        links.first.click()

        page.wait_for_load_state("networkidle")
        return True
    
    def click_class_by_index(page, index: int):
        try:
            # Wait for the class list to appear
            page.wait_for_selector("#listOfClasses a", timeout=10000)

            # Get all class links
            class_links = page.query_selector_all("#listOfClasses a")

            if not class_links:
                print("No classes found.")
                return

            if index < 0 or index >= len(class_links):
                print(f"Index {index} out of range. Found {len(class_links)} classes.")
                return

            print(f"Clicking class at index {index}")
            class_links[index].click()

        except Exception as e:
            print("Error clicking class:", e)
    
    p = sync_playwright().start()

    browser = p.chromium.launch(
        headless=headless,
        args=[
            "--remote-debugging-address=127.0.0.1",
            "--remote-debugging-port=9222"
        ]
    )

    context = browser.new_context()
    page = context.new_page()

    # navigate to target
    if not urlbase.startswith(("http://", "https://")):
        target = "https://" + urlbase
    else:
        target = urlbase

    page.goto(target)
    try:
        page.wait_for_load_state("domcontentloaded", timeout=5000)
    except Exception:
        pass
    print("Opened page:", page.url)

    # fill login fields
    try:
        page.wait_for_selector("#login", timeout=5000)
        page.fill("#login", username)
        print("Filled #login")
    except Exception:
        print("Login input (#login) not found")

    try:
        page.wait_for_selector("#password", timeout=5000)
        page.fill("#password", password)
        print("Filled #password")
        # submit (press Enter)
        page.press("#password", "Enter")
        print("Submitted credentials")
    except Exception:
        print("Password input (#password) not found")
    
            # Wait for navigation after login
    page.wait_for_load_state("networkidle")

    click_class_by_index(page, class_index)
    page.wait_for_selector("tr.pTableRow, tr.packageTableRow", timeout=15000)
    if not click_package_by_index(page, package_index):
        raise RuntimeError("Invalid package selection.")
    
    if double_points:
        enable_double_points(page)
    
    solver_proc = subprocess.Popen([sys.executable, "solver.py"])

    try:
        exit_code = solver_proc.wait()
        if exit_code:
            print(f"Solver returned exit code: {exit_code}")
    finally:
        print("Solver exited. Cleaning up...")

        browser.close()
        p.stop()
    if exit_code:
        sys.exit(exit_code)


if __name__ == "__main__":
    main()