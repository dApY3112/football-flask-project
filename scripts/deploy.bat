@echo off
echo Deploying the application...

:: Set PYTHONPATH to the src directory
set PYTHONPATH=%CD%

:: Check the current directory for debugging purposes
echo Current directory: %CD%
echo PYTHONPATH is set to: %PYTHONPATH%

:: Activate the virtual environment
call venv\Scripts\activate

:: Start the Flask application in the background
start /B python src\app.py

:: Optional: Add a sleep to allow the Flask app to initialize
timeout /t 5

:: Pause for debugging (optional, remove if not needed)
pause
