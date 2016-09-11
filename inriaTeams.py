from bs4 import BeautifulSoup
import urllib2
import re

html_page = urllib2.urlopen("https://www.inria.fr/en/research/research-teams/find-a-team")
soup = BeautifulSoup(html_page,"lxml")
for link in soup.findAll('a'):
    if ("/teams/" in link.get('href')):
		teamPage = urllib2.urlopen('https://www.inria.fr'+link.get('href'))
		sp = BeautifulSoup(teamPage,"lxml")
		for link2 in sp.findAll('a'):
			if link2.getText() == "Team's website":
				print link2.get('href')