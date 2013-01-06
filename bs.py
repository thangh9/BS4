#-------------------------------------------------------------------------------
# Name:        Beautiful Soup 4 tutorial
# Purpose:     Learn how to write first scraping script
#
# Author:      Pham Thang
#
# Created:     06/01/2013
# Copyright:   (c) Pham Thang 2013
# Licence:     GNU licence
#-------------------------------------------------------------------------------

from bs4 import BeautifulSoup #import BeautifulSoup
import urllib2 #import urllib2 to open URL

"""
Before scraping through website, we have to analyze website's structure to find
the patterns to extracting the content.
"""

#open url
url = "http://www.utexas.edu/world/univ/alpha/"
page = urllib2.urlopen(url)
Reader = codecs.getreader("utf-8")
fh = Reader(page)
soup = BeautifulSoup(fh.read())

#find A tag
uni = soup.findAll('a', {'class':'institution'})

#print all url and university's name
for each in uni:
	print each['href'] +"\n")

#open file and write result to file
file = open("uni.txt",'w','utf-8')
for each in uni:
	file.write(each['href'] + "\n")
file.close()

def main():
    pass

if __name__ == '__main__':
    main()