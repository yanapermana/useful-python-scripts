from subprocess import Popen, PIPE, check_output
proc = Popen(('ps', '-A'), stdout=PIPE)
output = check_output(('grep', 'python'), stdin=proc.stdout)
proc.wait()
print output