@echo off
echo.
echo ================================================================
echo   FINAL STEP: Create Repository and Push to GitHub
echo ================================================================
echo.
echo I will now open GitHub in your browser.
echo.
echo Please:
echo   1. Log in to GitHub if needed
echo   2. Click "New" (or use the page that opens)
echo   3. Name: ela-heroes
echo   4. Make it Public
echo   5. DO NOT initialize with README
echo   6. Click "Create repository"
echo.
echo Opening GitHub...
start https://github.com/new
echo.
echo After you create the repository, press any key to push...
pause
echo.
echo Pushing to GitHub...
echo.
git push -u origin main
echo.
if %ERRORLEVEL% EQU 0 (
    echo.
    echo ================================================================
    echo   SUCCESS! Repository published!
    echo   Visit: https://github.com/connor1570/ela-heroes
    echo ================================================================
) else (
    echo.
    echo Authentication needed. Opening browser for token creation...
    start https://github.com/settings/tokens/new?description=ELA%%20Heroes&scopes=repo
    echo.
    echo 1. Click "Generate token"
    echo 2. COPY the token
    echo 3. Press any key, then enter your username and paste token as password
    pause
    git push -u origin main
)
echo.
pause
