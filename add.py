import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "server.settings")

import sys
import json
import requests
from server import linedb

newitem = sys.argv[1]

items = linedb.read()
prev_id = len(items)

id = linedb.append(newitem)

pubitem = {
	'channel': 'test',
	'id': str(id),
	'prev-id': str(prev_id),
	'http-stream': {
		'content': newitem + '\n'
	}
}

postdata = json.dumps({'items': [pubitem]})

requests.post('http://localhost:5561/publish/', data=postdata)
