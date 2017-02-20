import subprocess
import sys
from nsenter import Namespace

mypid = sys.argv[1]

with Namespace(mypid, 'net'):
    # output network interfaces as seen from within the mypid's net NS:
subprocess.check_output(['ip', 'a'])
