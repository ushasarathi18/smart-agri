"""Smart Agri — automated setup script.
Run: python setup_and_run.py
"""
import subprocess, sys, os
def run(cmd, cwd=None):
    print(f'>>> {cmd}'); r = subprocess.run(cmd, shell=True, cwd=cwd)
    if r.returncode: sys.exit(r.returncode)
HERE = os.path.dirname(os.path.abspath(__file__))
BE = os.path.join(HERE,'backend'); FE = os.path.join(HERE,'frontend')
print('=== BACKEND SETUP ===')
run(f'{sys.executable} -m pip install -r requirements.txt', cwd=BE)
run(f'{sys.executable} manage.py makemigrations accounts products transactions vendors warehouse', cwd=BE)
run(f'{sys.executable} manage.py migrate', cwd=BE)
run(f'{sys.executable} seed.py', cwd=BE)
print('\n=== FRONTEND SETUP (optional) ===')
print('cd frontend && npm install && npm start')
print('\n=== START BACKEND ===')
print(f'cd backend && python manage.py runserver 0.0.0.0:8000')
print('\nDefault logins:\n  admin/admin123 (Django /admin/)\n  seller/seller123\n  vendor/vendor123\n  user/user123')
