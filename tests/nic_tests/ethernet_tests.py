from mclib.nic import ethernet
from nose.tools import ok_, eq_

def test_get_mac():
    ok_(ethernet.get_mac())
