#Environment
import os

def run(**args):
    print "In Environment mode")
    return str(os.environ)
