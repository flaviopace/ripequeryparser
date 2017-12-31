import json
from pprint import pprint
import sys

data = open("allroute", 'r')
json = json.load(data)

#print json["data"]["prefixes"]

for item in json["data"]["prefixes"]:
	ip = item["prefix"]
	#print ip + "\n"
	if "::" not in ip:
		print "route {} 255.255.255.0".format(ip[:-3])
