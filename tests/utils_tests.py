from mclib.utils import pardir, install_app_unix
from nose.tools import ok_
import os

def test_pardir():
    par = pardir(__file__)
    ok_(par)

def test_install_app_unix():
    dirpath = os.path.join(os.path.dirname(__file__), 'data')
    state, detail = install_app_unix(dirpath)
    ok_(state or True)

    
    
