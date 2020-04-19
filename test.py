#When ready to send to git, open Git Bash, use git commit -m "message" test.py THEN git push -u origin master
#Navigate to \Noll Alisa\PycharmProjects\punintendedv1
#Install flask (web apps), requests and beautifulsoup4 (web scraping) in the terminal using pip
#https://github.com/gmarmstrong/python-datamuse/ Repo for similar word search

#Imports
import requests
from bs4 import BeautifulSoup
import urllib
import re

#Pun web scraping
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
    #print(soup.prettify()) #View page content to determine what to scrape
    category = link.replace("https://punpedia.org/","").replace("-puns/","")
    pun_repo[category]={}  #Establish category as nested dictionary
    i=0
    for ultag in soup.findAll('ul')[1:]:      #Iterate through unstructured list, skipping initial paragraph
        for litag in ultag.findAll('li'):     #Iterate through all lines in unstructred list
            if "Here are related puns" in litag.text: #Ignore a few intro lines that aren't actually puns
                pass
            elif "Here are some puns" in litag.text: #Ignore a few intro lines that aren't actually puns
                pass
            elif "ve included" in litag.text: #Ignore a few intro lines that aren't actually puns
                pass
            elif "ve got some" in litag.text: #Ignore a few intro lines that aren't actually puns
                pass
            else:
                pun_repo[category][i]= {litag.text.replace(u'\xa0', u' ')}
                i=i+1

print(pun_repo)

#Web interface
# app = Flask(__name__)
#
# @app.route("/<name>")
# def hello_name(name):
#     return "Hello" + name
#
# if __name__=="__main__":
#     app.run(debug=True)

