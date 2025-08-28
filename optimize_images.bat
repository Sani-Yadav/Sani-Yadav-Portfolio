@echo off
setlocal enabledelayedexpansion

REM Create optimized directory if it doesn't exist
if not exist "portfolio\static\img\optimized" mkdir "portfolio\static\img\optimized"

REM Process all JPG and PNG files
for /r "portfolio\static\img" %%f in (*.jpg *.jpeg *.png) do (
    set "filepath=%%~f"
    set "relpath=!filepath:portfolio\static\img\=!"
    set "outpath=portfolio\static\img\optimized\%%~nf.webp"
    
    echo Optimizing: %%f
    
    REM Create output directory if it doesn't exist
    if not exist "%%~dpf" mkdir "%%~dpf"
    
    REM Convert to WebP with 80% quality
    magick convert "%%f" -quality 80 -resize 1920x1080\> "!outpath!"
)

echo.
echo Image optimization complete!
pause
