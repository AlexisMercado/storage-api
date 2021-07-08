from json import dumps as json_dumps
from os import environ
import bottle
from modules.cors import enable_cors
import modules.utils as utils
from modules.auth import auth_required

app = bottle.Bottle()

## Add a user
@app.post("/vg-info/addUser")
def add_a_user(*args, **kwargs):
    bottle.response.status = 501
    bottle.response.content_type = "application/json"
    return dict(code=501, message="Not implemented")

## Get user info
@app.get("/vg-info/addUser/<Nickname_id>")
def get_user(*args, **kwargs):
    bottle.response.status = 501
    bottle.response.content_type = "application/json"
    return dict(code=501, message="Not implemented")

## Add a videogame
@app.post("POST /vg-info/add")
def add_a_videogame(*args, **kwargs):
    bottle.response.status = 501
    bottle.response.content_type = "application/json"
    return dict(code=501, message="Not implemented")

## Get videogames List
@app.get("/vg-info/list")
def get_videogame_list(*args, **kwargs):
    bottle.response.status = 501
    bottle.response.content_type = "application/json"
    return dict(code=501, message="Not implemented")

## Get the info for a videogame
@app.get("/vg-info/<vg_codigo>")
def get_a_videogame(*args, **kwargs):
    bottle.response.status = 501
    bottle.response.content_type = "application/json"
    return dict(code=501, message="Not implemented")

## Add cheat for a videogame
@app.post("/vg-info/<vg_codigo>/Cheats/")
def add_a_cheat(*args, **kwargs):
    bottle.response.status = 501
    bottle.response.content_type = "application/json"
    return dict(code=501, message="Not implemented")

## Add easter egg for a videogame
@app.post("/vg-info/<vg_codigo>/Easter_Egg")
def add_a_easter_egg(*args, **kwargs):
    bottle.response.status = 501
    bottle.response.content_type = "application/json"
    return dict(code=501, message="Not implemented")


## Add reviews for a videogame
@app.post("/vg-info/<vg_codigo>/Opinion")
def add_a_review(*args, **kwargs):
    bottle.response.status = 501
    bottle.response.content_type = "application/json"
    return dict(code=501, message="Not implemented")





## Get all the cheats of a videogame
@app.post("/vg-info/<vg_codigo>/Cheats/")
def get_a_cheat_list(*args, **kwargs):
    bottle.response.status = 501
    bottle.response.content_type = "application/json"
    return dict(code=501, message="Not implemented")



## Get all the easter eggs of a videogame
@app.post("/vg-info/<vg_codigo>/Easter_Egg")
def get_a_easteregg_list(*args, **kwargs):
    bottle.response.status = 501
    bottle.response.content_type = "application/json"
    return dict(code=501, message="Not implemented")



## Get all the reviews of a videogame
@app.post("/vg-info/<vg_codigo>/Opinion")
def get_a_review_list(*args, **kwargs):
    bottle.response.status = 501
    bottle.response.content_type = "application/json"
    return dict(code=501, message="Not implemented")
