import os
import sys

__all__ = [
    'get_hw_mac',
]

def get_hw_mac(interface=None):
    '''
    get ethernet mac address
    '''
    #default setting
    if not interface and sys.platform.startswith('linux'):
        interface = 'eth0'

    interface_path = "/sys/class/net/%s/address" % interface
    with open(interface_path, 'r') as f:
        first_line = f.readline()
    return first_line.rstrip('\n')
