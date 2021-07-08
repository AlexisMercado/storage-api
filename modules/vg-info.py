from os import environ, urandom
import hashlib
import datetime
from bottle import response, request
import jwt
import binascii
from functools import wraps
import models.auth as mauth

videogames= []
def add_a_videogame(vg_codigo, nombre, Genero, plaforma):
    Videogame = {
        "vg_codigo": vg_codigo,
        "nombre": nombre,
        "Genero": Genero,
        "director": director,
        "plaforma": plaforma
    }
    videogames.append(videogames)
    return json.dumps(videogames)
