#!/usr/bin/env python
from django.core import management
import sys, os

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, PROJECT_ROOT)
sys.path.insert(0, os.path.join(PROJECT_ROOT, "apps"))

if __name__ == "__main__":
    management.execute_from_command_line()
