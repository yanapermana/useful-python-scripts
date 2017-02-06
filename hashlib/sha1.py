import hashlib

def sha1(message):
	h = hashlib.sha1()
	h.update(message)
	return h.hexdigest()

if __name__ == '__main__':
	print sha1('Whatever')