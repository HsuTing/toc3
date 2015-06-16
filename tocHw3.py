#coding:utf-8
import sys
from findoutlinks import findoutlinks

"""main"""
if len(sys.argv) < 3:
	print "input number is not enough."
elif len(sys.argv) > 3:
	print "input numner is too much."
else:
	findoutlinks(sys.argv[1], int(sys.argv[2]))
