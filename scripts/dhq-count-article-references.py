import time
import requests
from bs4 import BeautifulSoup
import csv

# this script takes a list of links to DHQ articles, 
# return the number of references contained within each article
# and writes these 2 pieces of data to a csv file

# insert list of links, or call separate file to iterate over
articles = ['put links here']

# initiate csv
f = open('filename.csv', mode='w')
writer = csv.writer(f)

for code in articles:
	# put article page code into BS4 object
	response = requests.get(code)
	soup = BeautifulSoup(response.text, features="html.parser")
	# div class="bibl" is the unique wrapper for an individual reference
	citations = soup.find_all(lambda tag: tag.name == 'div' and tag.get('class') == ['bibl'])
	# count number of references found
	numCitation = (len(citations))
	# write 2 columns to csv; 1 for the article URL, 1 for number of references
	row = [code, numCitation]
	writer.writerow(row)
	# be nice and use a time delay
	time.sleep(2)

f.close()
