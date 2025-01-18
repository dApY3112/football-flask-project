@echo off
echo Deploying the application...
:: Activate the virtual environment
call venv\Scripts\activate

REM Set PYTHONPATH to include the src directory
set PYTHONPATH=%CD%\src
echo PYTHONPATH is set to: %PYTHONPATH%

REM Start the Flask application
echo Starting the Flask application...
start /B python src\app.py
if errorlevel 1 (
    echo ERROR: Application failed to start! Check logs for details.
    pause
    exit /b 1
)


:: Start Flask app without input redirection
start pythonw src\app.py

:: Allow time for the Flask app to initialize
timeout /t 5

:: Avoid the interactive pause (remove the pause command)
echo Flask app should now be running in the background.

:: Clean up and exit
exit
