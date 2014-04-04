import sys, os, bottle

sys.path = ['/var/www/autoweb2/autoweb'] + sys.path
os.chdir(os.path.dirname(__file__))

import bottle
# ... build or import your bottle application here ...
# Do NOT use bottle.run() with modi_wsgi
try:
    import form
    application = form.app
except ImportError as ie:
    raise ImportError(str(ie) + str(os.getcwd()))

