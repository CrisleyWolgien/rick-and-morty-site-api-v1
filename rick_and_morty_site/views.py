from main import app
from flask import render_template, request
from flask import render_template

from api import fetch_data
from api import characters, episodes, location

characters = characters

episodes = episodes

locations = location

#ROUTES
@app.route("/")
def homepage():
    return render_template("homePage.html", characters=characters, episodes=episodes,locations=locations )


@app.route("/personagens")
def personagens():
    page = int(request.args.get("page", 1))
    characters = fetch_data("character", {"page": page})
    return render_template("characters.html", characters=characters, page=page)
