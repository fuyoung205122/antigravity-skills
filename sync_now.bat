@echo off
cd /d "%~dp0"
set PYTHON_EXE="C:\Users\Administrator\AppData\Local\Programs\Python\Python312\python.exe"

echo Starting manual sync...
%PYTHON_EXE% generate_docs.py

echo Pushing updates to GitHub...
git add .
git commit -m "Manual Sync: Update Skills"
git push origin main

echo.
echo ===================================================
echo Sync Complete! The website will update in 1-2 minutes.
echo ===================================================
pause
