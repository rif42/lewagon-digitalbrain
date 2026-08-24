@echo off
setlocal
set "ROOT=%~dp0.."
for %%I in ("%ROOT%") do set "ROOT=%%~fI"
set "SRC=%ROOT%\notes"
set "DEST=%ROOT%\quartz\content"

if not exist "%SRC%" (
  echo Source notes dir not found: %SRC% 1>&2
  exit /b 1
)

if exist "%DEST%" rmdir /s /q "%DEST%"
mkdir "%DEST%"

xcopy /s /e /y /i "%SRC%\*" "%DEST%\" >nul
if errorlevel 1 (
  echo xcopy failed 1>&2
  exit /b 1
)

if not exist "%DEST%\index.md" (
  if exist "%SRC%\index.md" copy /y "%SRC%\index.md" "%DEST%\index.md" >nul
)

echo Synced notes -> quartz/content
endlocal
