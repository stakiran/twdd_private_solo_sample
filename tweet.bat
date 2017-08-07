@echo off
title TwDD tweet
setlocal
set target=%~dp0tweets.md

python %~dp0tweet.py -o "%target%"
if ERRORLEVEL 1 exit /b

call %~dp0displaywait.bat
