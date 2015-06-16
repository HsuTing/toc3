#coding:utf-8
import sys
import json

"""main"""
if len(sys.argv) < 3:
	print "input number is not enough."
elif len(sys.argv) > 3:
	print "input numner is too much."
else:
	fp = open(sys.argv[1], "r")
	top = int(sys.argv[2])
	output = {}

	for line in fp:
		content = json.loads(line)

		if content["Envelope"]["Payload-Metadata"]["HTTP-Response-Metadata"]["HTML-Metadata"].has_key("Links"):
			links = content["Envelope"]["Payload-Metadata"]["HTTP-Response-Metadata"]["HTML-Metadata"]["Links"]
			maxtemp = 0

			for i in range(0, len(links)):
				if links[i].has_key("url") or links[i].has_key("href"):
					maxtemp = maxtemp + 1

			output[ content["Envelope"]["WARC-Header-Metadata"]["WARC-Target-URI"] ] = maxtemp

	output = sorted(output.items(), key=lambda x: x[1], reverse=True)

	for i in range(0, top):
		print output[i][0] + ":" + str(output[i][1])
	for i in range(top, len(output)):
		if output[i][1] == output[top - 1][1]:
			print output[i][0] + ":" + str(output[i][1])
	fp.close()
