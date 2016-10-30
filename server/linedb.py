import os
from django.conf import settings

fname = os.path.join(settings.BASE_DIR, 'data.txt')

def read():
	f = open(fname, 'r')
	lines = []
	for line in f:
		line = line.strip()
		if not line:
			continue
		lines.append(line)
	f.close()
	return lines

# return line number
def append(item):
	items = read()
	count = len(items)
	f = open(fname, 'a')
	f.write(item + '\n')
	f.close()
	return (count + 1)
