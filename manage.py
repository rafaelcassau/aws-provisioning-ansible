#!/usr/bin/env python
import os
import sys

sys.path.append("/home/ubuntu/virtualenvs/itreta/lib/python2.7/site-packages")
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "<my_project_name>.settings")

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "itreta.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
