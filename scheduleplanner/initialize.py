import os, sys, django, socket
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "scheduleplanner.settings")
django.setup()
from sch_account.views import *

