from flask import Flask,render_template,request
import requests


app = Flask(__name__)
base_url = "https://api.github.com/users/"

@app.route("/",methods=["GET","POST"])
def index():
    if request.method =="POST":
        githubname = request.form.get("githubname")
        response_user = requests.get(base_url+githubname)
        response_repos = requests.get(base_url+githubname+"/repos")
        userInfo = response_user.json()
        repos = response_repos.json()
        if "message" in userInfo:
            return render_template("index.html",error = "Belə bir istifadəçi tapılmadı və ya yoxdur!")

        return render_template("index.html",profile=userInfo,repos = repos)
    else:
        return render_template("index.html")

if __name__ == '__main__':
    app.run(debug = True)