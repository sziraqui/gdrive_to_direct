#!/usr/bin/python2
import sys
import json

# Note: Base url may change in future
base_direct_url = "https://drive.google.com/uc?export=download&id="

def getDirectUrl(public_url=""):
	parts = public_url.split('/')
	file_id = ""
	for part in parts:
		if "http" in part or "drive.google.com" in part or "view?usp=sharing" in part or len(part) < 8:
			pass
		else :
			file_id = part
	if file_id == "":
		error =  "Error: Not a GDrive url"
		return error
	else :
		return base_direct_url + file_id

# Index of url argument
url_i = 1

if sys.argv[1] == "-o":
	url_i = 3

# Dictionary to store urls
direct_urls = {}
# Counter that will act as key suffix
i = 1
while url_i < len(sys.argv):
	original_url = ""
	key = ""
	url_arg = sys.argv[url_i]
	if "::" in url_arg:
		key, original_url = url_arg.split("::")
	else :
		original_url = url_arg
	direct_urls[key if len(key)>0 else 'link'+str(i)] = getDirectUrl(original_url)
	i = i + 1
	url_i = url_i + 1

if sys.argv[1] == '-o':
	json_out = json.dumps(direct_urls, indent=4)
	file = open(sys.argv[2],'w')
	print >> file, json_out
	print "Output written to " + sys.argv[2]

for key in direct_urls:
	print key+": " + direct_urls[key]

