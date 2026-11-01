from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class RepoPrivacyTests(unittest.TestCase):
    def test_private_paths_ignored(self):
        content = (ROOT / ".gitignore").read_text("utf-8")
        for pattern in ("data/", "private/", ".env", "config.toml", "*.log"):
            self.assertIn(pattern, content)

    def test_example_config_has_no_secrets(self):
        content = (ROOT / "config.example.toml").read_text("utf-8")
        for key in ("username", "password", "ntfy_token"):
            self.assertFalse(any(line.strip().startswith(key + " =")
                                 for line in content.splitlines()))

    def test_password_prompt(self):
        launcher = (ROOT / "bot.py").read_text("utf-8")
        self.assertIn("getpass.getpass", launcher)
        self.assertIn("WOCABEE_PASSWORD", launcher)


if __name__ == "__main__":
    unittest.main()
