@echo off
set PYTHONPATH=%CD%\src
echo Running tests...
pytest --maxfail=1 --disable-warnings -q

:: Activate the virtual environment
call venv\Scripts\activate

:: Run tests and generate a test report
pytest --junitxml=reports\test_report.xml

pause
