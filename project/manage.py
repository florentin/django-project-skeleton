#!/usr/bin/env python
from django.core.management import execute_manager

import sys, os
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, PROJECT_ROOT)
sys.path.insert(0, os.path.join(PROJECT_ROOT, "apps"))

try:
    import settings.development # Assumed to be in the same directory.
except ImportError, e:
    import sys
    sys.stderr.write("Error: Can't find the file 'settings.py' in the directory containing %r. It appears you've customized things.\nYou'll have to run django-admin.py, passing it your settings module.\n(If the file settings.py does indeed exist, it's causing an ImportError somehow.)\n" % __file__)
    #sys.stderr.write("Error importing module 'settings.py': %r \n" % str(e))
    sys.exit(1)

if __name__ == "__main__":
    execute_manager(settings.development)
