from flask import Flask

app = Flask(__name__)

@app.route("/<name>")
def hello_name(name):
    return "Hello" + name

if __name__=="__main__":
    app.run(debug=True)

git push origin master

cd ~/Desktop/Project
git init
git checkout -b develop
touch README.md