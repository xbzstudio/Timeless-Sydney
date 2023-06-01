@echo off
rem conda activate newbing
cd ..
mkdir .\release\tmp
cd .\release\tmp
set NAME=newbing-sydney
pyinstaller ..\..\BingServer.py -n %NAME% -i ..\..\static\images\my-sydney.ico
xcopy .\dist\%NAME% ..\%NAME% /S /I /F /Y
cd ..
rmdir /S /Q .\tmp
for %%f in (..\LICENSE ..\cookie.json ..\README.md) do copy %%f .\%NAME%
xcopy ..\static .\%NAME%\static /S /I /F /Y
pause
