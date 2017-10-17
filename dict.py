import operator

# Sorted single dictionary
def good10(raw):	
	sorted_raw = sorted(raw.items(), key=operator.itemgetter(1), reverse=True)
	sorted_raw = sorted_raw[:10]
	data = {}
	for x,y in sorted_raw:
		data[x] = y
	return data

def top10(blob):	
	# Merge dictionaries
	raw = {}
	for b in blob:
		raw.update(b)
	# Sort dictionaries by value
	sorted_raw = sorted(raw.items(), key=operator.itemgetter(1), reverse=True)
	sorted_raw = sorted_raw[:10]
	data = {}
	for x,y in sorted_raw:
		data[x] = y
	# Split dictionaries into single dictionary and save to list
	return [dict(data.items()[i:i+1]) for i in range(len(data.items()))] 

if __name__ == '__main__':
	blob = [{'A': 2}, {'B': 4}, {'C': 3}, {'D': 1}, {'E': 0}, {'F': 10}, {'G': 7}, {'H': 2}, {'I': 13}, {'J': 90}, {'K': 20}, {'L': 1000}, {'M': -20}]
	print top10(blob)
	raw = {'A': 2, 'B': 4, 'C': 3, 'D': 1, 'E': 0, 'F': 10, 'G': 7, 'H': 2, 'I': 13, 'J': 90, 'K': 20, 'L': 1000, 'M': -20}
	print good10(raw)
