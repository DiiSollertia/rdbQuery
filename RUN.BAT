rmdir /s /q env
python3 -m venv --without-pip env
cmd /k "env\Scripts\activate.bat && pip install --force-reinstall -v 'rdbtools==0.1.15' && pip install --force-reinstall -v 'python-lzf==0.2.4' && env\Scripts\python3 -m combineJSON.py"
deactivate
pause