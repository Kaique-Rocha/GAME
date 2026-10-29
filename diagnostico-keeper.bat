@echo off
cd /d "%~dp0"
echo Iniciando KeeperRL com registro de erros...
keeper.exe --stderr > "keeper-diagnostico.txt" 2>&1
echo.>> "keeper-diagnostico.txt"
echo Codigo de saida: %errorlevel%>> "keeper-diagnostico.txt"
echo.
echo O jogo encerrou. Log salvo em keeper-diagnostico.txt
type "keeper-diagnostico.txt"
pause
