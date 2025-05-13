@echo off
setlocal


set "PROJECT_PATH=%USERPROFILE%\Desktop\Watchbox-main"
set "PROC_PATH=%PROJECT_PATH%\Procmon64a.exe"
set "LOG_PATH=%PROJECT_PATH%\procmon_log.pml"


taskkill /IM Procmon64a.exe /F >nul 2>&1


start "" /B "%PROC_PATH%" /AcceptEula /Quiet /Minimized /BackingFile "%LOG_PATH%"


timeout /t 10 /nobreak > nul


"%PROC_PATH%" /Terminate


timeout /t 2 > nul

