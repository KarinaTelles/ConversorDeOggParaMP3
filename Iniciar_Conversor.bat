@echo off
REM Conversor de Áudio WhatsApp - Launcher
REM Este arquivo facilita a execução do conversor no Windows

echo ========================================
echo   Conversor de Audio WhatsApp
echo ========================================
echo.

REM Verificar se Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo [ERRO] Python nao encontrado!
    echo.
    echo Por favor, instale o Python em: https://www.python.org/downloads/
    echo.
    pause
    exit /b 1
)

REM Verificar se o arquivo existe
if not exist "converter_gui.py" (
    echo [ERRO] Arquivo converter_gui.py nao encontrado!
    echo.
    echo Execute este arquivo na mesma pasta do converter_gui.py
    echo.
    pause
    exit /b 1
)

REM Executar o conversor
echo Iniciando o conversor...
echo.
python converter_gui.py

REM Se houver erro
if errorlevel 1 (
    echo.
    echo [ERRO] Ocorreu um problema ao executar o conversor.
    echo.
    pause
)

exit /b 0