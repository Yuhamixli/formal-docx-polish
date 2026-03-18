@echo off
setlocal
set SCRIPT_DIR=%~dp0
set PY_SCRIPT=%SCRIPT_DIR%scripts\validate_docx.py

if "%~1"=="" (
  echo Usage: validate-docx.cmd INPUT.docx [KIND] [STRICT]
  exit /b 1
)

set INPUT=%~1
set KIND=%~2
set STRICT=%~3
if "%KIND%"=="" set KIND=generic

if /I "%STRICT%"=="strict" (
  python "%PY_SCRIPT%" "%INPUT%" --kind %KIND% --strict
) else (
  python "%PY_SCRIPT%" "%INPUT%" --kind %KIND%
)
exit /b %ERRORLEVEL%
