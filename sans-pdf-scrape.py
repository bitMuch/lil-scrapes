#!/usr/bin/python3
# Created by c@caine
# On: 17/02/2017
# Task: Retrieve all Sans whitepapers
# --- Preamble --- #
from bs4 import BeautifulSoup			# funtions for parsing html
from urllib.request import urlopen		# functions for d/l web page
from urllib.request import urlretrieve
# --- Definitions --- #
ingredients = 'https://uk.sans.org/reading-room/whitepapers/auditing/index.html'
root = ingredients[:19]				# strip root url for use later 
# --- Functions --- #
def main():
  soup = BeautifulSoup(urlopen(ingredients), 'html.parser')
  for link in soup.find_all('a'):
    link = (link.get('href'))
    if '/reading-room/whitepapers/auditing/' in link:
      pdl = ('%s%s' % (root, link))
      pdf = ('%s.pdf' % (pdl[54:]))
      urlretrieve(pdl, pdf)
# --- Main --- #
if __name__ == "__main__":
  main()
