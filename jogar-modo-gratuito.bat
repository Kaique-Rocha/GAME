@echo off
cd /d "%~dp0"
echo Iniciando KeeperRL em modo gratuito (sem recursos comerciais)...
keeper.exe --free_mode --stderr > "keeper-modo-gratuito.log" 2>&1
echo Codigo de saida: %errorlevel%
type "keeper-modo-gratuito.log"
pause
