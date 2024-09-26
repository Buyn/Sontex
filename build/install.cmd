@echo off
py -m venv sontex-env -env
cmd /c "toch-env\Scripts\activate & pip install -r requirements.txt"
cmd /c "toch-env\Scripts\activate & main.py"
rem pip freeze > requirements.txt
rem python main.py
pause
