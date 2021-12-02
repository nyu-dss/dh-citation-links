import time
import requests
from bs4 import BeautifulSoup

# this script takes a list of links to DHQ journal issue homepages
# and returns (to stdout) the title and URL for each article contained within that issue
# n.b. multilingual issues (e.g. 12:1 and 14:2) will need to be deduplicated

# insert links for issue homepage, or call separate file to iterate over
issues = ['put links here']

for issue in issues:
	# put issue homepage code into BS4 object
	response = requests.get(issue)
	soup = BeautifulSoup(response.text)
	# select the wrapper for each article
	article = soup.select('.articleInfo a')
	# iterate over every other list item
	# because article returns 2 links, the first is the actual link to the article
	for links in article[::2]:
		print ("http://digitalhumanities.org" + links.get("href"))
	# be nice and use a time delay between requests
	time.sleep(2)