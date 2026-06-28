@echo off
cd /d "%~dp0"
set PYTHON_EXE="C:\Users\Administrator\AppData\Local\Programs\Python\Python312\python.exe"

echo Installing required packages...
%PYTHON_EXE% -m pip install -r requirements.txt

echo Starting background auto publisher...
%PYTHON_EXE% auto_publisher.py
pause
