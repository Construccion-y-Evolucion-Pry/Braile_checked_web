@echo off
REM Script para generar la documentación con Sphinx en Windows

echo Generando documentacion con Sphinx...

REM Cambiar al directorio del script
cd /d "%~dp0"

REM Limpiar la build anterior (opcional)
if exist "Documentation\build" (
    echo Limpiando documentacion anterior...
    rmdir /s /q "Documentation\build"
)

REM Generar la documentación
echo Compilando documentacion HTML...
".venv\Scripts\python.exe" -m sphinx -b html Documentation\source Documentation\build\html

if %ERRORLEVEL% EQU 0 (
    echo.
    echo Documentacion generada exitosamente!
    echo Ubicacion: Documentation\build\html\index.html
    echo.
    echo Para ver la documentacion, abre el archivo:
    echo    %CD%\Documentation\build\html\index.html
) else (
    echo.
    echo Error al generar la documentacion
    exit /b 1
)
