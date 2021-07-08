# VG Submits

  Este proyecto consiste en una plataforma donde los usuarios puedan compartir
  sus descubrimientos ya sean Easter Eggs o Cheats ademas de tener la oportunidad
  de agragar su opinion de un Videojuego en especifico creando asi una gran libreria
  con informacion de Videojuegos. Este proyecto esta enfocado 100% en el sector gamer.



## Entidades
Las entidades que se tienen en mente para el proyecto son las
siguientes:

- Usuario (Nombre, apellido, fecha_nac, Nickname_id, steam_id, XboxLive_id, PSN_id)

- Videojuego (Nombre, Genero, plataformas, vg_codigo )

- Cheats (vg_codigo, Usuario_Nickname_id, cheat, cheat_id )

- EasterEgg (vg_codigo, Usuario_Nickname_id, Easter_Egg, Easter_Egg_id)

- Opinion (vg_codigo, Usuario_Nickname_id, Opinion, calificacion, opinion_id)



## API

|PATH                                     | Descripcion                                                      |
|-----------------------------------------|------------------------------------------------------------------|
| /vg-info/addUser                    |`Agregar usuario`                                                 |
| /vg-info/addUser/<Nickname_id>      |`Consultar informacion del usuario`                               |
| /vg-info/add                        |`Capturar toda la informacion de un Videojuego`                   |
| /vg-info/list                       |`Lista de videojuegos`                                            |
| /vg-info/<vg_codigo>                |`Informacion de un Videojuego`                                    |
| /vg-info/<vg_codigo>/Cheats         |`Registrar un cheat de un videojuego`                             |
| /vg-info/<vg_codigo>/Cheats         |`Mostrar todos los cheats registrados en un Videojuego`           |
| /vg-info/<vg_codigo>/Easter_Egg     |`Registrar un cheat de un videojuego`                             |
| /vg-info/<vg_codigo>/Easter_Egg     |`Mostrar todos los cheats registrados en un Videojuego`           |
| /vg-info/<vg_codigo>/Opinion        |`Registrar un cheat de un videojuego`                             |
| /vg-info/<vg_codigo>/Opinion        |`Mostrar todos los cheats registrados en un Videojuego`           |






## Operaciones de Almacenamiento de datos
### Operaciones de Videojuegos

**Registrar un Videojuego**
- Solicitar el Nombre, Genero y plaformas en las que esta disponible.
- El codigo del juego se generara de forma automatica

**Actualizacion del estatus del videojuego**
- Eliminar videojuego

### Operaciones de Usuario
**Registrar un usuario**
- Solicitar el nombre, apellido y fecha de nacimiento.
- El usuario podra elegir su propio Nickname_id

### Operaciones de cheats
**Ingresar un cheat**
- Se solicitara el vg_codigo del videojuego al que se agregara el Cheat y el Nickname_id del usuario que hara el aporte,
  depues se describira el aporte.
- El cheat_id se generara automaticamente.

### Operaciones de Easter Eggs
**Ingresar un Easter Egg**
- Se solicitara el vg_codigo del videojuego al que se agregara el easter egg y el Nickname_id del usuario que hara el aporte,
  depues se escribira el aporte.
- El Easter_Egg_id se generara automaticamente.

### Operaciones de opiniones
**Ingresar una opinion**
- Se solicitara el vg_codigo del videojuego al que se agregara la opinion y el Nickname_id del usuario que hara el aporte,
  depues se escribira el aporte.
- El Easter_Egg_id se generara automaticamente.

## Operaciones de consulta de datos

### Solicitar datos de un usuario

- Su Nickname

### Lista de juegos
- Todos

### Solicitar datos de un Videojuego

- Su informacion basica
- Con todos sus cheats
- Con todos sus Easter eggs.
- Con todas sus opiniones

## Estructura de solicitud y respuesta

### Registro de usuario



```

     {

          "Nombre": "Bill",

          "apellido": "Williams",

          "fecha_nac": "1998-01-08",

          "Nickname_id": "Bi11",

          "steam_id":    "Billpcma$ter",

          "XboxLive_id": "Billynator",

          "PSN_id":      "Kid10"

    }
```

#### Respuesta de registro de usuario exitosa

```

     {

          "Nickname_id": "Bi11"
    }
```

#### Mensaje de fallo

```

     {

          "Code": "500",
          "mesagge": "Error al capturar Usuario"
    }
```


### Registro de Videojuego



```

     {

          "Nombre": "Fifa 2021"

          "Genero": "Deportes"

          "Plataforma": "PS4"


    }

```

#### Mensaje de registro de videojuego exitoso

```

     {

          "vg_codigo": "VG001"
    }
```


#### Mensaje de fallo

```

     {

          "Code": "500",
          "mesagge": "Error al capturar el videojuego"
    }
```


### Registro de un cheat



```

     {

          "vg_codigo": "VG001"

          "Usuario_Nickname_id": "Bi11"

          "Cheat": "Cuando vayas perdiendo en un partido solo pon pausa y cambiate al otro equipo para anotar unos autogoles y luego regresas a tu equipo."


    }

```

#### Mensaje de registro de Cheat exitoso

```

     {

          "cheat_id": "CH001"
    }
```
#### Mensaje de fallo

```

     {

          "Code": "500",
          "mesagge": "Error al capturar el cheat"
    }
```



### Registro de un Easter egg.



```

     {

          "vg_codigo": "VG001"

          "Usuario_Nickname_id": "Bi11"

          "Easter_Egg": "Aquir va un easter egg bien interesante"


    }

```

#### Mensaje de registro de Easter egg exitoso

```

     {

          "cheat_id": "EA001"
    }
```

#### Mensaje de fallo


```

     {

          "Code": "500",
          "mesagge": "Error al capturar el Easter egg"
    }
```


### Registro de una opinion.



```

     {

          "vg_codigo": "VG001",

          "Usuario_Nickname_id": "Bi11",

          "opinion": "Es exactamente igual al anterior lo cual es perfecto",

          "calificacion": "10"



    }

```

#### Mensaje de registro de una opinion exitoso

```

     {

          "cheat_id": "O001"
    }
```

#### Mensaje de fallo


```

     {

          "Code": "500",
          "mesagge": "Error al capturar la opinion"
    }
```






### Interaccion con el servidor


`POST /vg-info/addUser`

Recibe una estructura de registro de Usuario     
201, registra al ususario y regresa el Nickname_id
D.O.M, regresa estructura de mensaje de fallo

`GET  /vg-info/addUser/<Nickname_id>`

200 regresa la informacion de un usuario
D.O.M, regresa mensaje de fallo

`POST /vg-info/add`

Recibe una estructura de registro de un Videojuego     
201, registra al ususario y regresa el vg_codigo
D.O.M, regresa estructura de mensaje de fallo     

`GET  /vg-info/list`

200 regresa una lista de todos los Videojuegos en la aplicacion
D.O.M, regresa mensaje de fallo   

`GET  /vg-info/<vg_codigo>`

201, regresa la informacion de un videojuego
D.O.M, regresa mensaje de fallo   

`POST /vg-info/<vg_codigo>/Cheats/`

Recibe una estructura de registro de el cheat que el usuario quiera agregar     
201, registra al ususario y regresa el cheat_id
D.O.M, regresa estructura de mensaje de fallo  

`GET  /vg-info/<vg_codigo>/Cheats`

200 regresa una lista de todos los cheats de un juego en especifico
D.O.M, regresa mensaje de fallo      

`POST /vg-info/<vg_codigo>/Easter_Egg`

Recibe una estructura de registro de el Easter_Egg que el usuario quiera agregar    
201, registra al ususario y regresa el Easter_Egg_id
D.O.M, regresa estructura de mensaje de fallo

`GET  /vg-info/<vg_codigo>/Easter_Egg`

200 regresa una lista de todos los Easter Eggs de un juego en especifico
D.O.M, regresa mensaje de fallo  

`POST /vg-info/<vg_codigo>/Opinion`

Recibe una estructura de registro de la Opinion que el usuario quiera agregar     
201, registra al ususario y regresa la opinion_id
D.O.M, regresa estructura de mensaje de fallo

`GET  /vg-info/<vg_codigo>/Opinion`

200 regresa una lista de todas las opiniones de un juego en especifico
D.O.M, regresa mensaje de fallo  

## Autenticacion y autorizacion de usuarios

Los usuarios esta autorizados de realizar aportes como los son Cheats, easter eggs y opiniones y editar unicamente los aportes que sean propios.

('app:cheats:read:all', 'app:Cheats:write:self)

('app:Easter_Egg:read:all', 'app:Easter_Egg:write:self)

('app:Opinion:read:all', 'app:Opinion:write:self)


-------------falta ejemplo curl-------------------------------------





# Documento de Plan de Implementacion

## Aspecto General

Desde la creacion de los videojuegos siempre a existido una comunidad ansiosa
por compartir sus opiniones, descubrimientos y experiencias de un videojuego.
Este proyecto busca satisfacer esas necesidades de los gamers de hoy en dia,
dentro de una comunidad con la misma pasion e interes por estos temas.

La solucion especifica que plantea esta proyecto es el poder tener una
plataforma donde los gamers puedan compartir y expresar sus descubrimientos
y opiniones de sus videojuegos favoritos.

**Recursos**

Para la realizacion de este proyecto se necesitara de las habilidades de un talentoso
programador web, con experiencia en http, base de datos etc. Adememas de contar
con el equipo de computo adecuado para realizar multitareas sin ningun problema.

**Una vez terminado**

Ya que el proyecto este terminado y funcionando, el encargado de monitoriar
y mantenerlos tendra distintas responsabilidades, como lo es el moderar a los usuarios
y revisiar que todos los aportes a la plataforma sean legitimos y utiles.

## Aspecto Tecnico


## Computo en la Nube

### Crear unfork del proyectostorage-api

Crear unfork del proyectostorage-api
- **Entregable**, señalar cual es elcommit-hash, apartir del que ustedes realizaron el fork.

|Descripcion                |Commit hash                       
|----------------|-------------------------------|
|**Creacion del Fork:**         |`9104973e4fbeed90718214f2fbda302d73250b8a`             |

Crear los archivos correspondientes a su proyecto, y someterlos a control de versiones
- Entregable, señalar el commit-hash que contiene la creación de dichos archivos.–Archivos en./docs,./routes,./modules,./models, nombrados con el slug de su proyecto.
- NOTA: dentro de docs son archivos tipo markdown (.md), y dentro de las demás son archivos tipo python(.py)

|Descripcion                |Commit hash                          
|----------------|-------------------------------|
|**Creacion de docs/vg-info.md:**    |`9104973e4fbeed90718214f2fbda302d73250b8a` |   


Crear todas las rutas especificadas en su archivo de documentación dentro de su archivo en la carpeta routes, y todas deben de responder 501, con Content-Type: application/json, y un cuerpo de respuesta en formato json con 2 llaves,code y message, el message debe contener el mensaje, Not Implemented.
- Entregable,señalarelcommit-hashque contiene la codificacion de las rutas.

|Descripcion                |Commit hash                          
|----------------|-------------------------------|
|**Creacion de routes/VG-info.py:**    |`6811f51b316950d7dd71c6e7822d9dea34f547d9` |    

Crear en su carpeta de modulos funciones que emulen las interacciones con el almacén de archivos o datos, es decir que si necesitas una función de consulta, crear una función que retorne una consulta simulada con datos codificados como constantes, y si necesitas crear objetos funciones que retornen simulando una creación exitosa.

- Entregable,señalar el commit-hash que contiene la codificacion de estas funciones asistentes.


|                |RUTA                          
|----------------|-------------------------------|
|**Creacion de modules/VG-info.py:**  |`7b92f18209ea32988fdeafe33956d3bf1bd440fe`    |

**Creacion de models/VG-info.py:**
