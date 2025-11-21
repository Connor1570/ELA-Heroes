@echo off
echo ========================================
echo   ELA Heroes - GitHub Push Script
echo ========================================
echo.

echo Step 1: Authenticating with GitHub...
gh auth login --web --git-protocol https

echo.
echo Step 2: Creating repository on GitHub...
gh repo create connor1570/ela-heroes --public --description "Educational game for K-6 students learning ELA concepts" --source=.

echo.
echo Step 3: Pushing code to GitHub...
git push -u origin main

echo.
echo ========================================
echo   Success! Repository published!
echo   Visit: https://github.com/connor1570/ela-heroes
echo ========================================
pause
