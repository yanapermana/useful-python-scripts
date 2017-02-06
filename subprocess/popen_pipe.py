from subprocess import PIPE,Popen
proc = Popen(['ls', '-l'], stdout=PIPE)
for item in proc.communicate():
	if item != None:
		print item