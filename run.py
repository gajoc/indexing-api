import sys

from app import GeneiAppSelenium


g_app = GeneiAppSelenium(control_via=sys.argv[1])
g_app.run()
