@echo off
echo Deploying the application...

REM Check if Python is available
where python >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not added to PATH! Exiting...
    pause
    exit /b 1
)

REM Check if the virtual environment exists
if not exist venv\Scripts\activate (
    echo Virtual environment not found. Creating one...
    python -m venv venv
    if errorlevel 1 (
        echo ERROR: Failed to create virtual environment! Exiting...
        pause
        exit /b 1
    )
)

REM Activate the virtual environment
call venv\Scripts\activate
if errorlevel 1 (
    echo ERROR: Failed to activate virtual environment! Exiting...
    pause
    exit /b 1
)

REM Install dependencies
echo Installing dependencies...
pip install --no-cache-dir -r requirements.txt
if errorlevel 1 (
    echo ERROR: Failed to install dependencies! Exiting...
    pause
    exit /b 1
)

REM Set PYTHONPATH to include the src directory
set PYTHONPATH=%CD%\src
echo PYTHONPATH is set to: %PYTHONPATH%

REM Start the Flask application
echo Starting the Flask application...
python src\app.py
if errorlevel 1 (
    echo ERROR: Application failed to start! Check logs for details.
    pause
    exit /b 1
)

REM Pause to keep the window open (optional)
pause
