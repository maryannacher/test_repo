import subprocess
import sys

def pep8_error():
    proc = subprocess.Popen([sys.executable, 'pep8.py', '.'],
                             stdout=subprocess.PIPE)
    out, err = proc.communicate()
    return out

print pep8_error()
