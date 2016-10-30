from django.http import HttpResponse
import linedb

def stream(request):
	after = None

	grip_last = request.META.get('HTTP_GRIP_LAST')
	if grip_last:
		channel, params = grip_last.split(';')
		params = params.strip()
		assert(params.startswith('last-id='))
		after = int(params[8:])
	else:
		after_param = request.GET.get('after')
		if after_param:
			after = int(after_param)

	items = linedb.read()
	prev_id = len(items)

	if after:
		items = items[after:]

	if len(items) > 0:
		body = '\n'.join(items) + '\n'
	else:
		body = ''

	resp = HttpResponse(body, content_type='text/plain')
	resp['Grip-Hold'] = 'stream'
	resp['Grip-Channel'] = 'test; prev-id=%d' % prev_id
	resp['Grip-Link'] = '</?after=%d>; rel=next' % prev_id

	return resp
