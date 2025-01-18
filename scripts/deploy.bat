@echo off
echo Deploying the application...

:: Set PYTHONPATH to the src directory
set PYTHONPATH=%CD%\src

:: Check the current directory for debugging purposes
echo Current directory: %CD%
echo PYTHONPATH is set to: %PYTHONPATH%

:: Activate the virtual environment
call venv\Scripts\activate

:: Start Flask app without input redirection
start /B python src\app.py

:: Allow time for the Flask app to initialize
timeout /t 5

:: Avoid the interactive pause (remove the pause command)
echo Flask app should now be running in the background.

:: Clean up and exit
exit
