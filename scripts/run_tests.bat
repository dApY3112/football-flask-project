@echo off
echo Running tests...

:: Activate the virtual environment
call venv\Scripts\activate

:: Run tests and generate a test report
pytest --junitxml=reports\test_report.xml

pause
