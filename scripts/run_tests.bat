@echo off
REM Set the PYTHONPATH to the src directory (relative to the location of the script)
set PYTHONPATH=%CD%\src

REM Check the current directory for debugging purposes
echo Current directory: %CD%
echo PYTHONPATH is set to: %PYTHONPATH%

REM Install dependencies (optional, if you haven't done so already)
echo Installing dependencies...
pip install -r C:\ProgramData\Jenkins\.jenkins\workspace\football-backend\requirements.txt

REM Run the tests
echo Running tests...
python -m pytest --maxfail=1 --disable-warnings -q

REM Pause for debugging (optional, remove if not needed)
pause
