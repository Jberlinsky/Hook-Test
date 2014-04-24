# -*- coding: utf-8 -*-
#
# Copyright (C) 2013 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Command-line skeleton application for CustomSearch API.
Usage:
  $ python sample.py

You can also get help on all the command-line flags the program understands
by running:

  $ python sample.py --help

"""

import httplib2
import sys

import os
from apiclient import discovery
from apiclient.errors import HttpError

cseID = '012090963210376400561:mm4liotbq2e'

importantUrlsNum = 10
unimportantUrlsNum = 10

def getUrlList():
  # Create an httplib2.Http object to handle our HTTP requests .
  http = httplib2.Http()

  # Construct the service object for the interacting with the CustomSearch API.
  service = discovery.build('customsearch', 'v1',  developerKey='AIzaSyAdyilmupLnvCqvoP8pMdU29mKSNhDXHFY', http=http)

  print "Here is a list of queries we used and urls we fetch using Google customer search"

  urls = []
  totalImportantUrlNum = 0

  with open(os.path.dirname(os.path.abspath(__file__))+'/queries.txt') as queries:
	for query in queries:
		try:
			print 'query: ' + query
			res = service.cse().list(
			  	q = query,
			  	cx = cseID,
			  	num = importantUrlsNum,
			).execute()

			for value in res:
				#print value
				if 'items' in value:
					for result in res[value]:
						urls.append(result['formattedUrl'])
						print 'find top hit urls:' + result['formattedUrl']
						totalImportantUrlNum = totalImportantUrlNum + 1
		except HttpError:
			continue

		try:
			res = service.cse().list(
				q = query,
				cx = cseID,
				num = unimportantUrlsNum,
				start = 50,
			).execute()

			for value in res:
				#print value
				if 'items' in value:
					for result in res[value]:
						urls.append(result['formattedUrl'])
						print 'find hit urls that are not top 50:' + result['formattedUrl']
		except HttpError:
			continue

	result = [urls, totalImportantUrlNum]
	return result

# For more information on the CustomSearch API you can visit:
#
#   https://developers.google.com/custom-search/v1/using_rest
#
# For more information on the CustomSearch API Python library surface you
# can visit:
#
#   https://developers.google.com/resources/api-libraries/documentation/customsearch/v1/python/latest/
#
# For information on the Python Client Library visit:
#
#   https://developers.google.com/api-client-library/python/start/get_started
if __name__ == '__main__':
  getUrlList()
