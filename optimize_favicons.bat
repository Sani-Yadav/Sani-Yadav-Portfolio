@echo off
setlocal enabledelayedexpansion

REM Create optimized directory if it doesn't exist
if not exist "portfolio\static\img\optimized" mkdir "portfolio\static\img\optimized"

REM Optimize favicon.png to WebP
if exist "portfolio\static\img\favicon.png" (
    echo Optimizing favicon.png...
    magick convert "portfolio\static\img\favicon.png" -quality 90 "portfolio\static\img\optimized\favicon.webp"
)

REM Optimize apple-touch-icon.png to WebP
if exist "portfolio\static\img\apple-touch-icon.png" (
    echo Optimizing apple-touch-icon.png...
    magick convert "portfolio\static\img\apple-touch-icon.png" -quality 90 "portfolio\static\img\optimized\apple-touch-icon.webp"
)

echo.
echo Favicon optimization complete!
pause
