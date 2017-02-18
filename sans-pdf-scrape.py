#!/usr/bin/python3
# Created by c@caine
# On: 17/02/2017
# Task: Retrieve all Sans whitepapers
# --- Preamble --- #
from bs4 import BeautifulSoup			                              # funtions for parsing html
from urllib.request import urlopen		                          # function for opening web page
from urllib.request import urlretrieve                          # function for saving pdfs to disk
# --- Definitions --- #
ingredients = 'https://uk.sans.org/reading-room/whitepapers/auditing/index.html'
root = ingredients[:19]				                                  # strip root url for use later 
# --- Functions --- #
def main():
  soup = BeautifulSoup(urlopen(ingredients), 'html.parser')     # open page
  for link in soup.find_all('a'):                               # find links
    link = (link.get('href'))                                   # find string in link
    if '/reading-room/whitepapers/auditing/' in link:           # we only want pdfs
      pdl = ('%s%s' % (root, link))                             # build full link to pdf
      pdf = ('%s.pdf' % (pdl[54:]))                             # save file as
      urlretrieve(pdl, pdf)                                     # retreive link, save ffile
# --- Main --- #
if __name__ == "__main__":
  main()
