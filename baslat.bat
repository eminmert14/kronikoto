@echo off
chcp 65001 > nul
title KronikOto Baslatici
echo ====================================================
echo           KronikOto Platformu Baslatiliyor...
echo ====================================================
echo.

echo [1/3] Onceki servisler kontrol ediliyor ve portlar (3000, 8000) temizleniyor...
powershell -NoProfile -Command "Get-NetTCPConnection -LocalPort 8000,3000 -State Listen -ErrorAction SilentlyContinue | ForEach-Object { Stop-Process -Id $_.OwningProcess -Force -ErrorAction SilentlyContinue }"
timeout /t 1 /nobreak > nul

cd /d "%~dp0backend"
echo [2/3] Backend servisi baslatiliyor (FastAPI - Port 8000)...
start "KronikOto Backend" cmd /k ".\.venv\Scripts\python -m uvicorn app.main:app --port 8000"

timeout /t 3 /nobreak > nul

cd /d "%~dp0frontend"
echo [3/3] Frontend servisi baslatiliyor (Next.js - Port 3000)...
start "KronikOto Frontend" cmd /k "npm run start"

timeout /t 3 /nobreak > nul

echo.
echo ====================================================
echo  TUM SERVISLER BASARIYLA AYAGA KALKTI!
echo.
echo  Tarayicinizdan asagidaki adresi acabilirsiniz:
echo  >>> http://localhost:3000 <<<
echo ====================================================
echo.
start http://localhost:3000
pause
