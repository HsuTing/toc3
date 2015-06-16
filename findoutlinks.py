#coding:utf-8
import json

def findoutlinks(filename, top):
	fp = open(filename, "r")

	for line in fp:
		if top > 0:
			print line
			top = top - 1

	fp.close()
