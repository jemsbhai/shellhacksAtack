import subprocess

cmd = 'which python'

arch = subprocess.check_output(cmd, shell=True);


print (arch)
