@echo off
title TwDD Status
setlocal
pushd %~dp0
git status
popd
pause
