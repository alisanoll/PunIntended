#When ready to send to git, open Git Bash, use git commit -m "message" test.py THEN git push -u origin master
#Navigate to \Noll Alisa\PycharmProjects\punintendedv1
#Install flask (web apps), requests and beautifulsoup4 (web scraping) in the terminal using pip
#https://github.com/gmarmstrong/python-datamuse/ Repo for similar word search

#region Imports
import requests
from bs4 import BeautifulSoup
import urllib
import re
import json
import csv
#endregion

#region Pun web scraping
pun_links = []
URL = 'https://punpedia.org/'
site = requests.get(URL)      #Import category page
main_page = BeautifulSoup(site.text,'html.parser') #Parse with BeautifulSoup

for ultag in main_page.findAll('ul')[1:]:      #Iterate through unstructured list, skipping initial paragraph
     for litag in main_page.findAll('li'):     #Iterate through all lines in unstructred list
         if "category" in litag.a.get("href"):  # Ignore a few intro lines that are duplicate entries
             pass
         else:
            pun_links.append(litag.a.get("href"))   #Copy link to list

#Run through each pun page to create pun dict
pun_repo = {} #Create pun list

for link in pun_links:
    page = requests.get(link)      #Import page from pun links list
    soup = BeautifulSoup(page.text,'html.parser') #Parse with BeautifulSoup
    #print(soup.prettify ()) #View page content to determine what to scrape
    category = link.replace("https://punpedia.org/","").replace("-puns/","")
    pun_repo[category]=[]  #Establish category as list
    i=0
    for ultag in soup.findAll('ul')[1:]:      #Iterate through unstructured list, skipping initial paragraph
        for litag in ultag.findAll('li'):     #Iterate through all lines in unstructred list
            pun_repo[category].append(litag.text.replace(u'\xa0', u' ').replace(u'\n', u' '))

#Create json
#pun_repo_saved = json.dumps(pun_repo, default=set_default)
with open('pun_dict.json', 'w') as outfile:
    json.dump(pun_repo, outfile)
#endregion
