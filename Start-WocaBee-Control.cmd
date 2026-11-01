@echo off
setlocal EnableExtensions

if not exist "%~dp0config.toml" (
  echo First run: starting the one-time setup.
  call "%~dp0Setup-Browser.cmd"
  if errorlevel 1 exit /b 1
)

start "WocaBee Control" "%~dp0WocaBee-Control.exe"
