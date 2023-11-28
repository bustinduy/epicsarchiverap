#!/usr/bin/env python
"""
- small chages to work in python3 (2023)
|__ urllib2 -> urllib.request.urlopen
|__ urllib.urlencode  -> urllib.parse.urlencode
- correct tab spacing
"""
import urllib
#import urllib2
import json
import sys

PVPatterns = []

if(len(sys.argv) > 1):
	PVPatterns.extend(sys.argv[1:])

finalPVList = []
applianceMGMTUrl = 'http://archiver.slac.stanford.edu:17665/mgmt/bpl/getAllPVs'
if len(PVPatterns) > 0:
	for pattern in PVPatterns:
	resp = urllib.request.urlopen(url=applianceMGMTUrl + "?" + urllib.parse.urlencode({"pv" : pattern}))
	matchingPVs = json.load(resp)
	finalPVList.extend(matchingPVs)
else:
	resp = urllib.request.urlopen(url=applianceMGMTUrl)
	matchingPVs = json.load(resp)
	finalPVList.extend(matchingPVs)
	

for pv in sorted(finalPVList):
	print pv

