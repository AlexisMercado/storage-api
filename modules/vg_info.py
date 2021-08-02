from os import environ, urandom
import hashlib
import datetime
from bottle import response, request
import jwt
import binascii
from functools import wraps
import models.auth as mauth







import json
from modules.storage import *

#
# ...
#

def almacenar_vg(vg_id=None, nombre=None, genero=None, plataforma=None):
    print("Desde modulo almacenar_vg")
    print(nombre, genero, plataforma)
    para_almacenar = {"vg_id": vg_id,"nombre": nombre, "genero": genero, "plataforma":plataforma }
    nombre_de_archivo = f"{vg_id}-{title}.json"
    datos = store_string(
        "mi-carpeta3",
        nombre_de_archivo,
        json.dumps(para_almacenar)
    )
    return "Exito"








def almacenar_cheat(vg_id=None, cheat_id=None, cheat=None, username=None):
    print("Desde modulo almacenar_cheat")
    #print(nombre, eda)
    para_almacenar = {"vg_id": vg_id,"cheat_id": cheat_id, "cheat": cheat, "username":username }
    json_text = json.dumps(para_almacenar)
    store_string('mi-carpeta', nombre, para_almacenar)
    return "Exito"



def almacenar_easter(vg_id=None, easter_id=None, EasterEgg=None, username=None):
    print("Desde modulo almacenar_cheat")
    #print(nombre, eda)
    para_almacenar = {"vg_id": vg_id, "easter_id": easter_id, "EasterEgg": EasterEgg, "username":username }
    json_text = json.dumps(para_almacenar)
    store_string('mi-carpeta', nombre, para_almacenar)
    return "Exito"


def almacenar_opinion(vg_id=None, opinion_id=None, opinion=None, username=None):
    print("Desde modulo almacenar_cheat")
    #print(nombre, eda)
    para_almacenar = {"vg_id": vg_id, "opinion_id": opinion_id, "opinion": opinion, "username":username }
    json_text = json.dumps(para_almacenar)
    store_string('mi-carpeta', nombre, para_almacenar)
    return "Exito"















#videogames= []
#def add_a_videogame(vg_codigo, nombre, Genero, plaforma):
#    Videogame = {
#        "vg_codigo": vg_codigo,
#        "nombre": nombre,
#        "Genero": Genero,
#        "director": director,
#        "plaforma": plaforma
#    }
#    videogames.append(videogames)
#    return json.dumps(videogames)
