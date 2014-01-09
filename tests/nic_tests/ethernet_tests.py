from mclib.nic import ethernet
from nose.tools import ok_, eq_

def test_get_hw_mac():
    ok_(ethernet.get_hw_mac())
    
