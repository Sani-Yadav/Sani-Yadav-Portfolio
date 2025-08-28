@echo off
setlocal enabledelayedexpansion

echo Starting cleanup process...
echo ===========================

REM 1. Remove Python cache files
echo Removing Python cache files...
for /r . %%d in (__pycache__) do if exist "%%d" (
    echo Removing directory: %%d
    rd /s /q "%%d" 2>nul
)

REM 2. Remove Python compiled files
echo Removing .pyc and .pyo files...
del /s /q *.pyc 2>nul
del /s /q *.pyo 2>nul
del /s /q *.pyd 2>nul

REM 3. Remove temporary files
echo Removing temporary files...
del /s /q *.tmp 2>nul
del /s /q *.swp 2>nul

REM 4. Remove Windows and IDE specific files
echo Removing system and IDE files...
del /s /q Thumbs.db 2>nul
del /s /q .DS_Store 2>nul
del /s /q *.swo 2>nul

REM 5. Remove backup files
echo Removing backup files...
del /s /q *.bak 2>nul
del /s /q *~ 2>nul

REM 6. Remove empty directories
echo Removing empty directories...
for /f "delims=" %%d in ('dir /ad /b /s ^| sort /r') do (
    rd "%%d" 2>nul
)

echo.
echo Cleanup complete!
pause
