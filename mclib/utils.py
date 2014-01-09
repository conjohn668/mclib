import os.path
import glob
import subprocess

def pardir(abspath):
    '''
    get parent dirent of abspath [ either a file or dirent ]
    '''
    if not os.path.isdir(abspath):
        curdir = os.path.dirname(abspath)
    else:
        curdir = abspath
    return os.path.dirname(curdir)

    
def install_app_unix(dirpath):
    '''
    install an app on unix platform automately
    '''
    pkg = glob.glob(os.path.join(dirpath, '*.tar.gz'))[0]
    
    cmd = 'tar -zxvf %s' % pkg
    p = subprocess.Popen(cmd, shell=True,
                         cwd=dirpath,
                         stdout=subprocess.PIPE)
    p.wait()
    pkg_dir = p.stdout.readline()[:-1]

    cmd = './configure && make && make install'
    p = subprocess.Popen(cmd, shell=True,
                         cwd=os.path.join(dirpath, pkg_dir),
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)
    outdata, errdata = p.communicate()
    if p.returncode != 0:
        return False, '%s\n%s' % (outdata, errdata)
    else:
        return True, None
