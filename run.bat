@echo off
rem 检查requirements.txt文件是否存在
if not exist requirements.txt (
    echo requirements.txt file not found!
    pause
    exit /b 1
)

rem 检查python是否安装
where python >nul 2>&1
if %errorlevel% neq 0 (
    echo python not installed!
    pause
    exit /b 2
)

rem 检查pip是否安装
where pip >nul 2>&1
if %errorlevel% neq 0 (
    echo pip not installed!
    pause
    exit /b 3
)

rem 安装依赖包
pip install -r requirements.txt -i http://pypi.douban.com/simple --trusted-host pypi.douban.com

rem 检查BingServer.py文件是否存在
if not exist BingServer.py (
    echo BingServer.py file not found!
    pause
    exit /b 4
)

rem 运行BingServer.py
python ./BingServer.py

rem 结束
pause
exit /b 0
