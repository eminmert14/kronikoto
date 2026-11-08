@echo off
chcp 65001 > nul
title KronikOto - GitHub Yukleme

echo ========================================================
echo        KRONIKOTO - GITHUB'A YUKLEME
echo ========================================================
echo.
echo Kodlar GitHub adresinize gonderiliyor:
echo https://github.com/eminmert14/kronikoto.git
echo.
echo Tarayicinizda veya ekranda GitHub onay penceresi cikarsa
echo 'Sign in with your browser' / 'Authorize' butonuna basin.
echo.
echo ========================================================
echo.

cd /d "%~dp0"
git push -u origin main

echo.
echo ========================================================
if %ERRORLEVEL% equ 0 (
    echo  TEBRIKLER! Kodlar GitHub'a basariyla yuklendi!
) else (
    echo  Yukleme sirasinda bir sorun oldu.
)
echo ========================================================
pause
