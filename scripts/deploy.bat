@echo off
echo Deploying the application...
:: Activate the virtual environment
call venv\Scripts\activate

REM Set PYTHONPATH to include the src directory
set PYTHONPATH=%CD%\src
echo PYTHONPATH is set to: %PYTHONPATH%

REM Start the Flask application
echo Starting the Flask application...


:: Avoid the interactive pause (remove the pause command)
echo Flask app should now be running in the background.

:: Clean up and exit
exit
