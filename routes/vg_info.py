import json
from time import time
import bottle
from modules.bottles import BottleJson
from modules.auth import auth_required
from modules.storage import store_string, get_storage_file
from models.example import ExampleRecord
from modules.vg_info import almacenar_vg
from modules.vg_info import almacenar_cheat





app = BottleJson()

import random
def uniqueid():
    seed = random.getrandbits(32)
    while True:
       yield seed
       seed += 1



#@app.get("/")
#def store_record(*args, **kwargs):
    #return dict(code= 501, message = "Not implemented")

#def index():
    #payload = bottle.request.query
    #print(bottle.request.query)
    #print(payload.dict)
    #raise bottle.HTTPError(501, 'Error')



###############################     Añadir un videojuego  ############################################################
#curl http://localhost:8080/vg_info/AddVg -X POST -H 'Content-Type: application/json' -d '{"nombre": "Fifa","genero": "Deportes", "plataforma" : "xbox"}'
@app.post("/")
@app.get("/")





@app.post("/AddVg")
def AddVg(*args, **kwargs):

    payload = bottle.request.json
    print(payload)
    try:
        vg_id = str(payload['vg_id'])
        nombre = str(payload['nombre'])
        genero = str(payload['genero'])
        plaforma = str(payload['plataforma'])
        if len(nombre) == 0:
            raise Exception()
        print("Datos validos")
        respuesta = almacenar_vg(**payload)
        raise HTTPError(201, respuesta)
    except:
        print("Datos invalidos")
        raise bottle.HTTPError(400)
    raise bottle.HTTPError(500)


###################################### Añadir un cheat      ########################################################
#curl http://localhost:8080/vg_info/AddVg -X POST -H 'Content-Type: application/json' -d '{"cheat_id": "Ch001","cheat": "Abajo del puente hay una moneda", "username" : "cochiloco"}'


@app.post("<vg_id>/AddCheat")
def AddCheat(*args, **kwargs):

    payload = bottle.request.json
    print(payload)
    try:
        vg_id = str(payload['vg_id'])
        cheat_id = str(payload['cheat_id'])
        cheat = str(payload['cheat'])
        username = str(payload['username'])
        if len(cheat) == 0:
            raise Exception()
        print("Datos validos")
        respuesta = almacenar_cheat(**payload)
        raise HTTPError(201, respuesta)
    except:
        print("Datos invalidos")
        raise bottle.HTTPError(400)
    raise bottle.HTTPError(500)


###################################### Añadir un EasterEgg     ########################################################
#curl http://localhost:8080/vg_info/AddVg -X POST -H 'Content-Type: application/json' -d '{"cheat_id": "Ch001","cheat": "Abajo del puente hay una moneda", "username" : "cochiloco"}'


@app.post("<vg_id>/AddEaster")
def AddCheat(*args, **kwargs):

    payload = bottle.request.json
    print(payload)
    try:
        vg_id = str(payload['vg_id'])
        cheat_id = str(payload['easter_id'])
        cheat = str(payload['EasterEgg'])
        username = str(payload['username'])
        if len(cheat) == 0:
            raise Exception()
        print("Datos validos")
        respuesta = almacenar_easter(**payload)
        raise HTTPError(201, respuesta)
    except:
        print("Datos invalidos")
        raise bottle.HTTPError(400)
    raise bottle.HTTPError(500)



###################################### Añadir una opinion     ########################################################
@app.post("<vg_id>/AddOpinion")
def AddCheat(*args, **kwargs):

    payload = bottle.request.json
    print(payload)
    try:
        vg_id = str(payload['vg_id'])
        cheat_id = str(payload['opinion_id'])
        cheat = str(payload['opinion'])
        username = str(payload['username'])
        if len(cheat) == 0:
            raise Exception()
        print("Datos validos")
        respuesta = almacenar_opinion(**payload)
        raise HTTPError(201, respuesta)
    except:
        print("Datos invalidos")
        raise bottle.HTTPError(400)
    raise bottle.HTTPError(500)







































@app.post("/vg_info/list")
def get_videogame_list(*arg, **kwargs):
    payload = bottle.request.query
    print(payload.dict)
    #bottle.response.status = 501
    #bottle.response.content_type = "application/json"
    #return dict(code=501, message="Not implemented")

@app.post("/vg_info/add")
def get_videogame_list(*arg, **kwargs):
    payload = bottle.request.json
    print(payload)





#from json import dumps as json_dumps
#from os import environ
#import bottle
#from modules.cors import enable_cors
#import modules.utils as utils
#from modules.auth import auth_required

#app = bottle.Bottle()

## Add a user
@app.post("/vg_info/addUser")
def add_a_user(*args, **kwargs):
    bottle.response.status = 501
    bottle.response.content_type = "application/json"
    return dict(code=501, message="Not implemented")

## Get user info
@app.get("/vg_info/addUser/<Nickname_id>")
def get_user(*args, **kwargs):
    bottle.response.status = 501
    bottle.response.content_type = "application/json"
    return dict(code=501, message="Not implemented")

## Add a videogame
@app.post("/vg_info/add")
def add_a_videogame(*args, **kwargs):
    bottle.response.status = 501
    bottle.response.content_type = "application/json"
    return dict(code=501, message="Not implemented")

## Get videogames List
#@app.get("/vg_info/list")
#def get_videogame_list(*args, **kwargs):
#    bottle.response.status = 501
#    bottle.response.content_type = "application/json"
#    return dict(code=501, message="Not implemented")

## Get the info for a videogame
@app.get("/vg_info/<vg_codigo>")
def get_a_videogame(*args, **kwargs):
    bottle.response.status = 501
    bottle.response.content_type = "application/json"
    return dict(code=501, message="Not implemented")

## Add cheat for a videogame
@app.post("/vg_info/<vg_codigo>/Cheats/")
def add_a_cheat(*args, **kwargs):
    bottle.response.status = 501
    bottle.response.content_type = "application/json"
    return dict(code=501, message="Not implemented")

## Add easter egg for a videogame
@app.post("/vg_info/<vg_codigo>/Easter_Egg")
def add_a_easter_egg(*args, **kwargs):
    bottle.response.status = 501
    bottle.response.content_type = "application/json"
    return dict(code=501, message="Not implemented")


## Add reviews for a videogame
@app.post("/vg_info/<vg_codigo>/Opinion")
def add_a_review(*args, **kwargs):
    bottle.response.status = 501
    bottle.response.content_type = "application/json"
    return dict(code=501, message="Not implemented")





## Get all the cheats of a videogame
@app.post("/vg_info/<vg_codigo>/Cheats/")
def get_a_cheat_list(*args, **kwargs):
    bottle.response.status = 501
    bottle.response.content_type = "application/json"
    return dict(code=501, message="Not implemented")



## Get all the easter eggs of a videogame
@app.post("/vg_info/<vg_codigo>/Easter_Egg")
def get_a_easteregg_list(*args, **kwargs):
    bottle.response.status = 501
    bottle.response.content_type = "application/json"
    return dict(code=501, message="Not implemented")



## Get all the reviews of a videogame
@app.post("/vg_info/<vg_codigo>/Opinion")
def get_a_review_list(*args, **kwargs):
    bottle.response.status = 501
    bottle.response.content_type = "application/json"
    return dict(code=501, message="Not implemented")
