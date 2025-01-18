@echo off
echo Deploying the application...

:: Set the Python path for module resolution
set PYTHONPATH=%CD%\src

:: Check if the virtual environment exists
if not exist venv\Scripts\activate (
    echo ERROR: Virtual environment not found! Exiting...
    pause
    exit /b 1
)

:: Activate the virtual environment
call venv\Scripts\activate
if errorlevel 1 (
    echo ERROR: Failed to activate virtual environment! Exiting...
    pause
    exit /b 1
)

:: Run the Flask application
if not exist src\app.py (
    echo ERROR: app.py not found! Exiting...
    pause
    exit /b 1
)

python src\app.py
if errorlevel 1 (
    echo ERROR: Application failed to start! Check logs for details.
    pause
    exit /b 1
)

echo Application deployed successfully.
pause
