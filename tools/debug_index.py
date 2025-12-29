import os
import sys
# Ensure project root (where manage.py lives) is on sys.path
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')
import django
django.setup()

from django.test import RequestFactory
import traceback

def run():
    rf = RequestFactory()
    req = rf.get('/')
    try:
        from webapp.views import index
        resp = index(req)
        print('OK:', type(resp))
    except Exception:
        traceback.print_exc()

if __name__ == '__main__':
    run()
