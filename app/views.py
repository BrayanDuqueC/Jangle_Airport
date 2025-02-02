from app import app
from datetime import datetime
from flask import render_template, request, redirect
# contendra todas nuestra vistas

# * you can create custom filter in a new file and import them into your __init__


@app.template_filter("clean_date")  # -this is a custom template
def clean_date(dt):
    return dt.strftime("%d %b %Y")


@app.route("/")
def index():
    return render_template("public/index.html")


@app.route('/jinja')
def jinja():  # -Pasing python objects to the base template html
    my_name = "Jeison"
    age = 24
    langs = ["python", "java", "html", "css"]
    pets = {
        "Sasha": 4,
        "Mishu": 5,
        "Lucky": 8
    }
    colors = ("red", "green", 14)
    cool = True

    class GitRemote:
        def __init__(self, name, description, url) -> None:
            self.name = name
            self.description = description
            self.url = url

        def pull(self):
            return f"Pullin repo {self.name}"

        def clone(self):
            return f"Cloning into {self.url}"

    my_remote = GitRemote("flask Jinja", "Template desing tutorial", "https://github.com/jeison-AK/The_Flask_Course")

    def repeat(x, times):
        return x*times

    date = datetime.utcnow()
    return render_template("public/jinja.html", name=my_name,  # tienen que ser key=value para que pueda funcionar
                           age=age, langs=langs, pets=pets,
                           colors=colors, cool=cool,
                           GitRemote=GitRemote, my_remote=my_remote,  # podemos pasar una instance de la clase o la clase en si
                           repeat=repeat, date=date)


@app.route("/about")  # todo
def about():
    return render_template("public/about.html")


@app.route('/sign_up', methods=["GET", "POST"])  # to use this get post you need to import requests
def sing_up():
    # get to get the content and post to post it into our server
    # this code wiil execute only when the route recieve a post request
    if request.method == "POST":
        req = request.form
        # here we have several alternative to store what's in the form inside variables:
        username = req["username"]
        email = req.get("email")
        password = request.form["password"]
        print(username, email, password)
        return redirect(request.url)
    return render_template("public/sign_up.html")
