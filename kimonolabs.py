# import modules
import json
import requests
import os.path
# import config file (edit the kimonoconfig.py.sample file and save as kimonoconfig.py)
from kimonoconfig import kimono

# variables for building request url
api_id = kimono['api_id']
api_key = kimono['api_key']
url_base = "https://www.kimonolabs.com/api/"
api_url = url_base + api_id

# request current api data
api_request = requests.get(api_url, params=api_key)
# get current api data response
api_response = json.loads(api_request.content)
# determine current version of api data
version = api_response['version']
print "Latest version of " + api_id + " is " + str(version) + "."

# loop through each version and save to file
while version > 0:
	url = url_base + str(version) + "/" + api_id
	outfile = api_id + "_" + str(version) + ".json"
	print "Retrieving version " + str(version) + "..."
	r = requests.get(url, params=api_key)
	# if data is returned, check if exists already, then save file
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
	# if data not returned, print message, e.g. no previous versions available
	else:
		message = json.loads(r.content)
		message = message['message']
		print message
		version = 0