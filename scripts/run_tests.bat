@echo off
REM Set the PYTHONPATH to the src directory (relative to the location of the script)
set PYTHONPATH=%CD%\src

REM Check the current directory for debugging purposes
echo Current directory: %CD%
echo PYTHONPATH is set to: %PYTHONPATH%



REM Start the Flask server in the background
echo Starting Flask server...
start /B python -m src.app

REM Wait for the server to start up (you may need to adjust the delay)
timeout /t 5

REM Run the tests
echo Running tests...
python -m pytest --maxfail=1 --disable-warnings -q

REM Pause for debugging (optional, remove if not needed)
pause
