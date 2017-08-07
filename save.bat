@echo off
setlocal

pushd %~dp0
git status --short
popd

set commitmsg= %date% %time:~0,8%
pushd %~dp0
echo saving...
git add -A
git commit -m "%commitmsg%"
popd
