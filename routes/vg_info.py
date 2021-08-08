import json
from time import time
import bottle
from modules.bottles import BottleJson
from modules.auth import auth_required
from modules.storage import store_string, get_storage_file
from models.example import ExampleRecord
from modules.vg_info import almacenar_vg
from modules.vg_info import get_vg_list
from modules.vg_info import get_vg
from modules.vg_info import get_cheat
from modules.vg_info import get_easter
from modules.vg_info import get_opinion
from modules.vg_info import get_cheat_list
from modules.vg_info import get_easter_list
from modules.vg_info import get_opinion_list
from modules.vg_info import almacenar_cheat
from modules.vg_info import almacenar_easter
from modules.vg_info import almacenar_opinion




app = BottleJson()





#@app.get("/")
#def store_record(*args, **kwargs):
    #return dict(code= 501, message = "Not implemented")

#def index():
    #payload = bottle.request.query
    #print(bottle.request.query)
    #print(payload.dict)
    #raise bottle.HTTPError(501, 'Error')


@app.get("/")
###############################     Añadir un videojuego  ############################################################
# curl http://localhost:8080/vg_info/AddCheat -X POST -H 'content-Type: application/json' -d '{"vg_id":"212","nombre": "fifa","genero": "Deportes", "plataforma" : "xbox"}'




@app.post("/AddVg")
def AddVg(*args, **kwargs):

    payload = bottle.request.json
    print(payload)
    try:
        vg_id = str(payload['vg_id'])
        nombre = str(payload['nombre'])
        genero = str(payload['genero'])
        plaforma = str(payload['plataforma'])
        print("Datos validos")
        respuesta = almacenar_cheat(**payload)

    except:
        print("Datos invalidos")
        raise bottle.HTTPError(400)
    raise bottle.HTTPError(201, respuesta)
#####################################Lista de todos los videojuegos###############################################################################

#curl http://localhost:8080/vg_info/list -X GET
@app.get("/list")
def get_all_vg(*args, **kwargs):
    try:
       respuesta = get_vg_list()
    except:
        raise bottle.HTTPError(500, "Error interno")
    raise bottle.HTTPError(200, respuesta)

################################### Ver un juego por su id #########################################################
@app.get("/<vg_id>")
def get_vg_by_id(*args, vg_id=None, **kwargs):
    try:
        respuesta = get_vg(vg_id = vg_id)
    except:
        raise bottle.HTTPError(400)
    raise bottle.HTTPError(200, respuesta)
###################################### Añadir un cheat      ########################################################
#curl http://localhost:8080/vg_info/AddCheat -X POST -H 'Content-Type: application/json' -d '{"vg_id":"vg003","cheat_id": "Ch001","cheat": "Abajo del puente hay una moneda", "username" : "cochiloco"}'

@app.post("/<vg_id>/AddCheat")
def AddCheat(*args, **kwargs):

    payload = bottle.request.json
    print(payload)
    try:
        vg_id = str(payload['vg_id'])
        cheat_id = str(payload['cheat_id'])
        cheat = str(payload['cheat'])
        username = str(payload['username'])
        VideojuegoNombre= str(payload['VideojuegoNombre'])
        print("Datos validos")
        respuesta = almacenar_cheat(**payload)

    except:
        print("Datos invalidos")
        raise bottle.HTTPError(400)
    raise bottle.HTTPError(201, respuesta)

#####################################Lista de todos los Cheats###############################################################################

#curl http://localhost:8080/vg_info/Cheats/list -X GET
@app.get("/Cheats/list")
def get_all_cheat(*args, **kwargs):
    try:
       respuesta = get_cheat_list()
    except:
        raise bottle.HTTPError(500, "Error interno")
    raise bottle.HTTPError(200, respuesta)

###################################### Ver un cheat por su id #####################################################
#curl http://localhost:8080/vg_info/Cheats/Ch001 -X GET
@app.get("/Cheats/<cheat_id>")
def get_cheat_by_id(*args, cheat_id=None, **kwargs):
    try:
        respuesta = get_cheat(cheat_id = cheat_id)
    except:
        raise bottle.HTTPError(400)
    raise bottle.HTTPError(200, respuesta)
###################################### Añadir un EasterEgg     ########################################################
# curl http://localhost:8080/vg_info/212/AddEaster -X POST -H 'Content-Type: application/json' -d '{"vg_id":"212","easter_id": "ea0032","EasterEgg": "Abajo del puente hay una moneda", "username" : "cochiloco", "VideojuegoNombre":"Mario"}'


@app.post("/<vg_id>/AddEaster")
def Addeaster(*args, **kwargs):

    payload = bottle.request.json
    print(payload)
    try:
        vg_id = str(payload['vg_id'])
        cheat_id = str(payload['easter_id'])
        cheat = str(payload['EasterEgg'])
        username = str(payload['username'])
        VideojuegoNombre= str(payload['VideojuegoNombre'])
        print("Datos validos")
        respuesta = almacenar_easter(**payload)

    except:
        print("Datos invalidos")
        raise bottle.HTTPError(400)
    raise bottle.HTTPError(201, respuesta)

###################################### Mostrar easter egg por id #####################################################
#curl http://localhost:8080/vg_info/Easter/ea0032 -X GET
@app.get("/Easter/<easter_id>")
def get_easter_by_id(*args, easter_id=None, **kwargs):
    try:
        respuesta = get_easter(easter_id = easter_id)
    except:
        raise bottle.HTTPError(400)
    raise bottle.HTTPError(200, respuesta)


#####################################Lista de todos los easter eggs ###############################################################################

#curl http://localhost:8080/vg_info/Easter -X GET
@app.get("/Easter/list")
def get_all_Easter(*args, **kwargs):
    try:
       respuesta = get_easter_list()
    except:
        raise bottle.HTTPError(500, "Error interno")
    raise bottle.HTTPError(200, respuesta)

###################################### Añadir una opinion     ########################################################
#curl http://localhost:8080/vg_info/212/AddOpinion -X POST -H 'Content-Type: application/json' -d '{"vg_id":"212","opinion_id": "ea0032","opinion": "Abajo del puente hay una moneda", "username" : "cochiloco", "VideojuegoNombre":"Mario"}'

@app.post("/<vg_id>/AddOpinion")
def Addopinion(*args, **kwargs):

    payload = bottle.request.json
    print(payload)
    try:
        vg_id = str(payload['vg_id'])
        cheat_id = str(payload['opinion_id'])
        cheat = str(payload['opinion'])
        username = str(payload['username'])
        VideojuegoNombre= str(payload['VideojuegoNombre'])
        print("Datos validos")
        respuesta = almacenar_opinion(**payload)

    except:
        print("Datos invalidos")
        raise bottle.HTTPError(400)
    raise bottle.HTTPError(201, respuesta)



#####################################Lista de todos las opiniones###############################################################################

#curl http://localhost:8080/vg_info/Opinion/list -X GET
@app.get("/Opinion/list")
def get_all_opinion(*args, **kwargs):
    try:
       respuesta = get_opinion_list()
    except:
        raise bottle.HTTPError(500, "Error interno")
    raise bottle.HTTPError(200, respuesta)



###################################### Mostrar opinion por id #####################################################
#curl http://localhost:8080/vg_info/Opinion/op0032 -X GET
@app.get("/Opinion/<opinion_id>")
def get_opinion_by_id(*args, opinion_id=None, **kwargs):
    try:
        respuesta = get_opinion(opinion_id = opinion_id)
    except:
        raise bottle.HTTPError(400)
    raise bottle.HTTPError(200, respuesta)





































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
