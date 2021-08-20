from os import environ, urandom
import hashlib
import datetime
from bottle import response, request
import jwt
import binascii
from functools import wraps
import models.auth as mauth







import json
from modules.storage import (
    store_string,
    store_bytes,
    query_storage,
    get_storage_file
)


#
# ...
#

def almacenar_vg(vg_id=None, nombre=None, genero=None, plataforma=None):
    #El siguiente modulo tiene como finalidad almacenar un videojuego nuevo
    #Utilizando vg_id, nombre, genero, plataforma
    #
    print("Desde modulo almacenar_vg")
    print(vg_id,nombre, genero, plataforma)
    para_almacenar = {"vg_id": vg_id,"nombre": nombre, "genero": genero, "plataforma":plataforma }
    nombre_de_archivo = f"{vg_id}-{nombre}.json"
    datos = store_string(
        "vg_info/Videojuegos",
        nombre_de_archivo,
        json.dumps(para_almacenar)
    )
    return datos








def almacenar_cheat(vg_id=None, cheat_id=None, cheat=None, username=None, VideojuegoNombre=None):
    #El siguiente modulo cumple la tarea de almacenar un cheat a un videojuego en especifico
    #vg_id, cheat_id, cheat, username, VideojuegoNombre
    #
    print("Desde modulo almacenar_cheat")
    #print(nombre, eda)
    para_almacenar = {"vg_id": vg_id,"cheat_id": cheat_id, "cheat": cheat, "username":username, "VideojuegoNombre": VideojuegoNombre }
    json_text = json.dumps(para_almacenar)
    nombre_de_archivo = f"{vg_id}-{cheat_id}-{VideojuegoNombre}.json"
    datos = store_string(
        "vg_info/Cheats",
        nombre_de_archivo,
        json.dumps(para_almacenar)
    )
    return datos



def almacenar_easter(vg_id=None, easter_id=None, EasterEgg=None, username=None, VideojuegoNombre=None):
    print("Desde modulo almacenar_easter")
    #El siguiente modulo cumple la tarea de almacenar un cheat a un videojuego en especifico
    #vg_id, easter_id, EasterEgg, username, VideojuegoNombre
    #print(nombre, eda)
    para_almacenar = {"vg_id": vg_id, "easter_id": easter_id, "EasterEgg": EasterEgg, "username":username, "VideojuegoNombre": VideojuegoNombre }
    json_text = json.dumps(para_almacenar)
    nombre_de_archivo = f"{vg_id}-{easter_id}-{VideojuegoNombre}.json"
    datos = store_string(
        "vg_info/EsterEggs",
        nombre_de_archivo,
        json.dumps(para_almacenar)
    )
    return datos


def almacenar_opinion(vg_id=None, opinion_id=None, opinion=None, username=None, VideojuegoNombre=None):
    #El seguiente modulo es para almacenar una opinion
    #Utilizando los siguientes datos
    #vg_id=None, opinion_id, opinion, username, VideojuegoNombre
    print("Desde modulo almacenar_opinion")
    #print(nombre, eda)
    para_almacenar = {"vg_id": vg_id, "opinion_id": opinion_id, "opinion": opinion, "username":username, "VideojuegoNombre": VideojuegoNombre }
    json_text = json.dumps(para_almacenar)
    nombre_de_archivo = f"{vg_id}-{opinion_id}-{VideojuegoNombre}.json"
    datos = store_string(
        "vg_info/Opiniones",
        nombre_de_archivo,
        json.dumps(para_almacenar)
    )
    return datos




def get_vg_list(videogames=None):
    #Modulo Get para consultar la lista de todos los videojuegos registrados
    query_result = query_storage(
        "vg_info/Videojuegos",
    )
    if videogames is  None:
        return query_result["content"]


def get_cheat_list(cheats=None):
    #Modulo Get para consultar la lista de todos los videojuegos registrados
    query_result = query_storage(
        "vg_info/Cheats",
    )
    if cheats is  None:
        return query_result["content"]


def get_easter_list(easter=None):
    query_result = query_storage(
        "vg_info/EasterEgg",
    )
    if easter is  None:
        return query_result["content"]

def get_opinion_list(opinion=None):
    query_result = query_storage(
        "vg_info/Opiniones",
    )
    if opinion is  None:
        return query_result["content"]


def get_vg(vg_id=None):
    query_result = query_storage(
        "vg_info/Videojuegos",
    )
    if vg_id is not None:
        return [
           r
           for r in query_result["content"]
           if vg_id in r
        ]
    print("Exito")





def get_cheat(cheat_id=None):
    query_result = query_storage(
        "vg_info/Cheats",
    )
    if cheat_id is not None:
        return [
           r
           for r in query_result["content"]
           if cheat_id in r
        ]
    print("Exito")




def get_easter(easter_id=None):
    query_result = query_storage(
        "vg_info/EsterEggs",
    )
    if easter_id is not None:
        return [
           r
           for r in query_result["content"]
           if easter_id in r
        ]
    print("Exito")


def get_opinion(opinion_id=None):
    query_result = query_storage(
        "vg_info/Opiniones",
    )
    if opinion_id is not None:
        return [
           r
           for r in query_result["content"]
           if opinion_id in r
        ]
    print("Exito")







def add_new_image(imageName=None, imageFile=None):
    filename = f"{imageName}.jpg"
    store_bytes(
        "vg_info/images",
        filename,
        imageFile.read()
    )
    return f"vg_info/images/{filename}"












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
