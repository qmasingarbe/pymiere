@echo off
rem Auto install PymiereLink extension to Premiere on windows

echo Downloading Adobe Extension Manager
curl "http://download.macromedia.com/pub/extensionmanager/ExManCmd_win.zip" --output %temp%\ExManCmd_win.zip
echo.

echo Download PymiereLink extension
curl "https://raw.githubusercontent.com/qmasingarbe/pymiere/master/pymiere_link.zxp" --output %temp%\pymiere_link.zxp
echo.

echo Unzip Extension Manager
rem require powershell
powershell Expand-Archive %temp%\ExManCmd_win.zip -DestinationPath %temp%\ExManCmd_win -Force
echo.

echo Install Extension
call %temp%\ExManCmd_win\ExManCmd.exe /install %temp%\pymiere_link.zxp
if %ERRORLEVEL% NEQ 0 (
    echo Installation failed...
) else (
    echo.
    echo Installation successful !
)

