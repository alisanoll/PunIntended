#When ready to send to git, open Git Bash, use git commit -m "message" test.py THEN git push -u origin master
#Navigate to \Noll Alisa\PycharmProjects\punintendedv1
#Install flask (web apps), requests and beautifulsoup4 (web scraping) in the terminal using pip
#https://github.com/gmarmstrong/python-datamuse/ Repo for similar word search


#region Imports
import json
from flask import Flask           # import flask
#endregion


# region Lyric API (skipped for now)
# # lyric_search = Song.find_song(user_input)
# # print(lyric_search)
# endregion

#region Import Puns
f = open('pun_dict.json', "r")

# Reading from file
puns = json.loads(f.read())

# Closing file
f.close()
#endregion