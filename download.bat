@echo off
setlocal

pushd %~dp0
echo downloading...
git pull
popd

call %~dp0displaywait.bat
