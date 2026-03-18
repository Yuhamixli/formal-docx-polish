@echo off
setlocal
set SCRIPT_DIR=%~dp0
set PY_SCRIPT=%SCRIPT_DIR%scripts\polish_docx.py

if "%~1"=="" (
  echo Usage: run-polish.cmd INPUT.docx [OUTPUT.docx] [KIND]
  exit /b 1
)

set INPUT=%~1
set OUTPUT=%~2
set KIND=%~3
if "%KIND%"=="" set KIND=generic

if "%OUTPUT%"=="" (
  python "%PY_SCRIPT%" "%INPUT%" --kind %KIND%
) else (
  python "%PY_SCRIPT%" "%INPUT%" "%OUTPUT%" --kind %KIND%
)
exit /b %ERRORLEVEL%
