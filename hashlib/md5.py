import hashlib

def md5(message):
	h = hashlib.md5()
	h.update(message)
	return h.hexdigest()

if __name__ == '__main__':
	print md5('Whatever')
