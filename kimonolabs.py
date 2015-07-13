import json
import requests
import os.path
from kimonoconfig import kimono

# api id
api_id = kimono['api_id']
api_key = kimono['api_key']
url_base = "https://www.kimonolabs.com/api/"
api_url = url_base + api_id
api_request = requests.get(api_url, params=api_key)
api_response = json.loads(api_request.content)
version = api_response['version']
print "Latest version of " + api_id + " is " + str(version) + "."

# loop through each version and save to file
while version > 0:
	url = url_base + str(version) + "/" + api_id
	outfile = api_id + "_" + str(version) + ".json"
	print "Retrieving version " + str(version) + "..."
	r = requests.get(url, params=api_key)
	if (r.status_code == requests.codes.ok):
		if os.path.isfile(outfile):
			print "File version exists, trying previous version..."
			version -= 1
		else:
			with open(outfile, 'w') as f:
				json_out = json.loads(r.content)
				json.dump(json_out, f)
				print "Version " + str(version) + " saved to " + outfile + "."
				version -= 1
	else:
		message = json.loads(r.content)
		message = message['message']
		print message
		version = 0