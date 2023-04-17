@echo off
cd toch
rem venv-run main.py
rem pause
rem cmd /k "cd /d C:\Users\Admin\Desktop\venv\Scripts & activate & cd /d    C:\Users\Admin\Desktop\helloworld & python manage.py runserver"
rem pause
rem cmd /k "toch-env\Scripts\activate & main.py"
cmd /c "toch-env\Scripts\activate &python main.py"
rem pause
