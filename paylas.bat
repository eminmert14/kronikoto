@echo off
chcp 65001 > nul
title KronikOto - Canli Paylasim Linki

echo ========================================================
echo        KRONIKOTO - CANLI PAYLASIM LINKI HAZIRLANIYOR
echo ========================================================
echo.
echo  Sunucu kontrol ediliyor...

cd /d "%~dp0"

powershell -NoProfile -ExecutionPolicy Bypass -Command ^
  "$process = Start-Process -FilePath '.\cloudflared.exe' -ArgumentList 'tunnel --url http://localhost:3000' -NoNewWindow -PassThru -RedirectStandardError 'tunnel.log';" ^
  "Write-Host '  Cloudflare baglantisi kuruluyor, lutfen 5-10 saniye bekleyin...' -ForegroundColor Yellow;" ^
  "$url = $null;" ^
  "for ($i=0; $i -lt 30; $i++) {" ^
  "    Start-Sleep -Seconds 1;" ^
  "    if (Test-Path 'tunnel.log') {" ^
  "        $content = Get-Content 'tunnel.log' -Raw -ErrorAction SilentlyContinue;" ^
  "        if ($content -match 'https://[a-zA-Z0-9-]+\.trycloudflare\.com') {" ^
  "            $url = $matches[0];" ^
  "            break;" ^
  "        }" ^
  "    }" ^
  "}" ^
  "if ($url) {" ^
  "    Set-Clipboard -Value $url;" ^
  "    Write-Host '';" ^
  "    Write-Host '========================================================' -ForegroundColor Green;" ^
  "    Write-Host '  TEBRIKLER! CANLI LINKINIZ HAZIR:' -ForegroundColor Green;" ^
  "    Write-Host \"  $url\" -ForegroundColor Cyan;" ^
  "    Write-Host '========================================================' -ForegroundColor Green;" ^
  "    Write-Host '  (Link panoya OTOMATIK kopyalandi! Direkt yapistirabilirsiniz)' -ForegroundColor Magenta;" ^
  "    Write-Host '';" ^
  "    Write-Host 'Bu pencereyi KAPATMAYIN. Pencere acik kaldigi surece link calisir.' -ForegroundColor Yellow;" ^
  "    $process.WaitForExit();" ^
  "} else {" ^
  "    Write-Host 'Link alinamadi. Detayli log:' -ForegroundColor Red;" ^
  "    Get-Content 'tunnel.log' -Tail 15;" ^
  "}"

pause
