@echo off
set PYTHONPATH=%CD%\src

echo Current directory: %CD%
echo PYTHONPATH: %PYTHONPATH%

echo Installing dependencies...
pip install -r ..\requirements.txt

echo Running tests...
pytest --maxfail=1 --disable-warnings -q

pause
