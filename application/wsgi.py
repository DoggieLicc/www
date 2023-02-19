import os
import sys

try:
    os.chdir(os.path.dirname(sys.argv[0]))
except OSError:
    pass

from api import app

application = app
