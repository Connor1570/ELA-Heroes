@echo off
echo.
echo ============================================================
echo   ELA Heroes - GitHub Repository Setup
echo ============================================================
echo.
echo Your repository is ready to push!
echo.
echo STEP 1: Create the repository on GitHub
echo ----------------------------------------
echo 1. Open your browser and go to: https://github.com/new
echo 2. Repository name: ela-heroes
echo 3. Description: Educational game for K-6 students learning ELA concepts
echo 4. Select: Public
echo 5. DO NOT check "Initialize with README"
echo 6. Click "Create repository"
echo.
echo STEP 2: Press any key here AFTER you've created the repository...
pause
echo.
echo STEP 3: Pushing your code to GitHub...
echo ----------------------------------------
git push -u origin main
echo.
if %ERRORLEVEL% EQU 0 (
    echo SUCCESS! Your repository is now live at:
    echo https://github.com/connor1570/ela-heroes
) else (
    echo.
    echo If you got a password prompt and it failed:
    echo 1. Go to: https://github.com/settings/tokens/new
    echo 2. Create a token with 'repo' permissions
    echo 3. Use the token as your password when prompted
)
echo.
echo ============================================================
pause
