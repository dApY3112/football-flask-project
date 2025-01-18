@echo off
echo Deploying the application...

:: Activate the virtual environment
call venv\Scripts\activate

:: Run the Flask application
python src\app.py

pause
