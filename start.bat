@echo off
:restart
cls
call .\venv\Scripts\activate
python -V
cd reistestion
python manage.py runserver
goto restart
