@echo off
cd /d "%~dp0"
where py >nul 2>nul
if %errorlevel%==0 (
  py -3 -m pip install -r requirements.txt
  if errorlevel 1 goto :fail
  py -3 -m playwright install chromium
) else (
  python -m pip install -r requirements.txt
  if errorlevel 1 goto :fail
  python -m playwright install chromium
)
if errorlevel 1 goto :fail
echo Instalace hotova.
pause
exit /b 0
:fail
echo Instalace selhala; zkontroluj Python a internet.
pause
exit /b 1
