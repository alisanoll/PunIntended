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

#region Web interface
app = Flask(__name__)             # create an app instance

@app.route("/Alisa")                   # at the end point /
def hello(name):                      # call method hello
    return "Hello " + name        # which returns "hello world"
if __name__ == "__main__":        # on running python app.py
    app.run(debug=True)                     # run the flask app
#endregion

# region Search databases
# user_input = "deer"
# if user_input in pun_repo:
#     print("Direct puns for " + user_input)
#     print("Puns: " + str(pun_repo[user_input]) + "\n")
#     print("Puns: " + pun_repo[user_input].values + "\n")