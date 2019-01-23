#!/usr/bin/env python

import re

shakes = open("text.txt", "r")

for line in shakes:
    if "dangle1" in line :
		if "dangle10" in line :
			#print line
			ok = line.split(" ")
			print ok[0]

