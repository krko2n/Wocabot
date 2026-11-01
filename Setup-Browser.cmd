@echo off
setlocal EnableExtensions

set "ROOT=%~dp0"
set "RUNTIME=%ROOT%runtime"
set "BROWSERS=%ROOT%ms-playwright"

where py >nul 2>nul
if errorlevel 1 (
  echo Python 3 is required for the one-time browser download.
  echo Install Python for Windows from https://www.python.org/downloads/ and run this file again.
  pause
  exit /b 1
)

if not exist "%RUNTIME%" mkdir "%RUNTIME%"
if not exist "%RUNTIME%\wordlist.json" copy /y "%ROOT%defaults\wordlist.json" "%RUNTIME%\wordlist.json" >nul
if not exist "%RUNTIME%\picturelist.json" copy /y "%ROOT%defaults\picturelist.json" "%RUNTIME%\picturelist.json" >nul
if not exist "%ROOT%config.toml" copy /y "%ROOT%config.example.toml" "%ROOT%config.toml" >nul

echo Installing the compatible Playwright browser runtime. This download is large and may take a while.
py -3 -m pip install --user "playwright==1.64.1"
if errorlevel 1 goto :failed

set "PLAYWRIGHT_BROWSERS_PATH=%BROWSERS%"
py -3 -m playwright install chromium
if errorlevel 1 goto :failed

echo.
echo Setup is complete. Edit config.toml with your own credentials, then run Start-WocaBee-Control.cmd.
pause
exit /b 0

:failed
echo.
echo Setup did not finish. Check your Internet connection, available disk space, and Python installation, then retry.
pause
exit /b 1
