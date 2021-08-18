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
| /addVG                    |Agregar un videojueo usuario                                                 |
| /<vg_id>/GetVg      |Consultar informacion de un Videojuego                               |
| /list      |Consultar la lista de todos los videojuegos registrados                            |
| /<vg_id>/AddCheat                       |Agregar un Cheat a un Videojuego                   |
| /Cheatslist                      |Lista de todos lo cheats registrados                                            |
| /<cheat_id>/Cheatslist       |Consultar un cheat por su id          |
| /<vg_id>/AddEaster               |Agregar un Easter Egg a un videojueo                                    |
| /<easter_id>/Easterlist         |Mostrar todos los cheats registrados en un Videojuego           |
| /Easterlist    |Consultar la lista de los Easter Eggs Registrados          |
| /<vg_id>/AddOpinion"       |Agregar un una opinion a un videojuego          |
| /Opinionlist       |Consultar la lista de las opiniones          |
| /<opinion_id>/Opinionlist       |Consultar una opinion en especifico por medio de si id          |






## Operaciones de Almacenamiento de datos
### Operaciones de Videojuegos

**Registrar un Videojuego**
- Solicitar el Nombre, Genero y plaformas en las que esta disponible.
- El codigo del juego se generara de forma automatica





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

- Recibe una estructura de registro de Usuario     
- 201, registra al ususario y regresa el Nickname_id
- D.O.M, regresa estructura de mensaje de fallo

`GET  /vg-info/addUser/<Nickname_id>`

- 200 regresa la informacion de un usuario
- D.O.M, regresa mensaje de fallo

`POST /vg-info/add`

- Recibe una estructura de registro de un Videojuego     
- 201, registra al ususario y regresa el vg_codigo
- D.O.M, regresa estructura de mensaje de fallo     

`GET  /vg-info/list`

- 200 regresa una lista de todos los Videojuegos en la aplicacion
- D.O.M, regresa mensaje de fallo   

`GET  /vg-info/<vg_codigo>`

- 201, regresa la informacion de un videojuego
- D.O.M, regresa mensaje de fallo   

`POST /vg-info/<vg_codigo>/Cheats/`

- Recibe una estructura de registro de el cheat que el usuario quiera agregar     
- 201, registra al ususario y regresa el cheat_id
- D.O.M, regresa estructura de mensaje de fallo  

`GET  /vg-info/<vg_codigo>/Cheats`

- 200 regresa una lista de todos los cheats de un juego en especifico
- D.O.M, regresa mensaje de fallo      

`POST /vg-info/<vg_codigo>/Easter_Egg`

- Recibe una estructura de registro de el Easter_Egg que el usuario quiera agregar    
- 201, registra al ususario y regresa el Easter_Egg_id
- D.O.M, regresa estructura de mensaje de fallo

`GET  /vg-info/<vg_codigo>/Easter_Egg`

- 200 regresa una lista de todos los Easter Eggs de un juego en especifico
- D.O.M, regresa mensaje de fallo  

`POST /vg-info/<vg_codigo>/Opinion`

- Recibe una estructura de registro de la Opinion que el usuario quiera agregar     
- 201, registra al ususario y regresa la opinion_id
- D.O.M, regresa estructura de mensaje de fallo

`GET  /vg-info/<vg_codigo>/Opinion`

- 200 regresa una lista de todas las opiniones de un juego en especifico
- D.O.M, regresa mensaje de fallo  

## Autenticacion y autorizacion de usuarios

Los usuarios esta autorizados de realizar aportes como los son Cheats, easter eggs y opiniones y editar unicamente los aportes que sean propios.

('app:cheats:read:all', 'app:Cheats:write:self)

('app:Easter_Egg:read:all', 'app:Easter_Egg:write:self)

('app:Opinion:read:all', 'app:Opinion:write:self)



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

### Modulos de codigos necesarios

De entro de estos modulos se encuentra uno de los mas importantes y mas comentados en este documento que
son las **rutas** ya que son las encargadas de la navegacion de los datos entra las entidades y sin unas rutas bien definidas el programa puede tener un sin fin de errores.

Otro aspecto importante son las funcion es de almacenamiento puesto que la idea principal del proyecto gira entorno a aguardar y consultar datos. Ademas es importante mencionar las funcionalidades del API que consiste en agregar Videojuegos, cheats, easter eggs etc.

### Plan para la codificacion de los Modulos

Antes de empezar a programar es importante tener un esquema de como estara organizado todo, en este caso los Mock-ups seran de gran ayuda. Una vez teniendo las vistas, se puede empezar a planificar la codificacion.

### Plan para la verificacion de la calidad del producto

Antes de terminar el proyecto debemos de tener planeado ciertos parametros a cumplir con respecto a la funcionalidad. Este plan consistira en el monitoreo regular de plataforma y asegurarse de su correcto funcionamiento como uso de parte de los usuarios.



## Historial de Edicion

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
- Entregable, señalarelcommit-hashque contiene la codificacion de las rutas.

|Descripcion                |Commit hash                          
|----------------|-------------------------------|
|**Creacion de routes/VG-info.py:**    |`6811f51b316950d7dd71c6e7822d9dea34f547d9` |    

Crear en su carpeta de modulos funciones que emulen las interacciones con el almacén de archivos o datos, es decir que si necesitas una función de consulta, crear una función que retorne una consulta simulada con datos codificados como constantes, y si necesitas crear objetos funciones que retornen simulando una creación exitosa.

- Entregable, señalar el commit-hash que contiene la codificacion de estas funciones asistentes.


| Descripcion               |Commit hash                          
|----------------|-------------------------------|
|**Creacion de modules/VG-info.py:**  |`7b92f18209ea32988fdeafe33956d3bf1bd440fe`    |

| Descripcion               |Commit Hash                          
|----------------|-------------------------------|
|**Mock-Ups y sus descriciones**  |`3038ef66dba9ead18e22aeb762e9c5ccdff2e4e3`    |

## Planificacion de Front End (Mock-Ups).

Para planear el desarollo del Frontend es necesario tener en cuenta las herramientas que se
utilizaran y la estructura y diseño que tendran cada pestaña en la que el usuario estara utilizando. Es muy importante que el Frontend sea realizado teniendo en mente las funcionalidades ya implementadas en el Backend.

La estructura de la pagina sera realizada por medio de HTML y CSS.

#### La ventana principal
Esta sera la primer ventana con la que el usuario se topara al ingresar a la plataforma.

La imagen `vg-info-0001-videogames_list.PNG` muestra el listado de juegos registrados en la plataforma, dentro de este menu el usuario podra elegir el videojueo en el quiere consultar informacion o realizar un aporte, notese que en el listado se muestra la informacion basica de todos los  videojuegos registrado.

![Image text](https://github.com/AlexisMercado/storage-api/blob/master/docs/assets/vg-info-0001-videogames_list.PNG)

#### Menu de un Videojuego
Al seleccionar y hacer clic en una de los videojuegos de la lista nos llevara a la siguiente ventana.

La imagen `vg-info-0002-Videogame_menu.PNG` Muestra el menu una vez seleccionado el juego, este menu tendra una combo box que nos dejara elegir el tipo de aportes que queremos consultar ya sea cheat, easter egg o opiniones, ademas de que en la parte baja se puede ver el boton que te dejara realizar el aporte dependiendo la informacion que estes consultando.


![Image text](https://github.com/AlexisMercado/storage-api/blob/master/docs/assets/vg-info-0002-Videogame_menu.PNG)

Al hacer clic en el boton ADD nos llevara a la seguiente ventana que es en la cual el usuario podra realizar su aporte (Dependiendo si en la ventana anterior estaba consultando cheats, Easter Egg u Opiniones)

La imagen  `vg-info-0003-videogamesa_addcheat.PNG` no muestra un recuadro para ingresar el texto que en este caso seria un cheat.

![Image text](https://github.com/AlexisMercado/storage-api/blob/master/docs/assets/vg-info-0003-videogamesa_addcheat.PNG)



# Casos de uso.

### Agregar un videojuego.

El Usuario puede agregar el videojuego de su eleccion, tomando en cuenta el nombre del videojuego, la plataforma el genero y el id.

```
curl http://localhost:8080/vg_info/AddVg -X POST -H 'content-Type: application/json' -d '{"vg_id":"VG009","nombre": "The Legend Of Zelda Ocarina Of Time","genero": "Aventura", "plataforma" : "Nintendo"}'
```


### Lista de todos los videojuego agregados.

El Usuario puede consultar la lista de todos los Videojuegos registrados en el sistema.

```
curl http://localhost:8080/vg_info/list -X GET
```

### Consultar un videojuego en especifico.

El Usuario puede consultar la un videojuego en especifico utilizando el id de este.

```
curl http://localhost:8080/vg_info/VG009/GetVg -X GET
```


### Añadir un Cheat

El usuario agregara un Cheat al videojuego de su eleccion tomando en cuenta su id y los siguientes datos para el cheat: id del cheat ,nombre del videojuego, el cheat y el nombre de usuario .

```
curl http://localhost:8080/vg_info/VG001/AddCheat -X POST -H 'Content-Type: application/json' -d '{"vg_id":"VG009","cheat_id": "CH002","cheat": "Cuando sueltes unos bugs usa tu botella para capturar uno. Ahora mira tu botella y tendras 3 de ellos.", "username" : "ZeldaLover", "VideojuegoNombre" : "The legend Of Zelda Ocarina Of Time"}'
```

### Consultar la lista de todos los cheats.

El Usuario puede consultar la lista de todos los cheats registrados en el sistema.

```
curl http://localhost:8080/vg_info/Cheatslist -X GET
```



### Consultar la informacion de un cheat en especifico.

El Usuario puede consultar la informacion un de un cheat de un videojuego en especifico utilizando el id de este.

```
curl http://localhost:8080/vg_info/CH002/Cheatslist -X GET
```



### Añadir un Easter Egg

El usuario agregara un Easter Egg al videojuego de su eleccion tomando en cuenta su id y los siguientes datos para el Easter Egg: id del Easter Egg ,nombre del videojuego, el Easter Egg y el nombre de usuario .

```
 curl http://localhost:8080/vg_info/212/AddEaster -X POST -H 'Content-Type: application/json' -d '{"vg_id":"VG009","easter_id": "EA002","EasterEgg": "cuando te encuentras en el patio del castillo de Hyrule, justo antes de hablar con Zelda, si fisgoneas en las ventanas podrás ver varios retratos de Mario, Peach e incluso Bowser,", "username" : "ZeldaLover", "VideojuegoNombre":"The Legend Of Zelda Ocarina Of Time"}'
```



### Consultar la lista de todos los Easter Eggs.

El Usuario puede consultar la lista entera de todos los Easter Egg registrados

```
curl http://localhost:8080/vg_info/Easterlist -X GET
```


### Consultar un Easter Egg en especifico.

El Usuario puede consultar un Easter Egg en especifico utilizando su id.

```
curl http://localhost:8080/vg_info/EA002/Easterlist -X GET
```

### Añadir una opinion

El usuario agregara una Opinion al videojuego de su eleccion tomando en cuenta su id y los siguientes datos para la Opinon: id de la opinion ,nombre del videojuego, el Opinion y el nombre de usuario .


```
curl http://localhost:8080/vg_info/VG008/AddOpinion -X POST -H 'Content-Type: application/json' -d '{"vg_id":"VG009","opinion_id": "OP002","opinion": "Increible juego el tiempo pasa volando de lo divertido que es", "username" : "MansyX3", "VideojuegoNombre":"The Legend Of Zelda Ocarina Of Time"}'

```



### Consultar la lista de todos las opiniones.

El Usuario puede consultar la lista entera de todos las opiniones registradas

```
curl http://localhost:8080/vg_info/Opinionlist -X GET
```


### Consultar una opinionn en especifico.

El Usuario puede consultar una una opinion en especifico utilizando su id.

```
curl http://localhost:8080/vg_info/OP002/Opinionlist -X GET
```

### Agregar una imagen

El usuario podra subir una imagen al sistema.

```
curl http://localhost:8080/vg_info/image/new/001 -X POST -H 'Content-Type: multipart/form-data' -F 'image_file=@/C/Users/alexi/Pictures/Fifa.jpg'
```
# Documentacion para continuacion del proyecto
Una vez finalizado el codigo se puede llegar a la conclusion que hay varia area de oportunidad asi como mas funciones que facilmente podrian agregarse al proyecto, entre ellos se encuentran los siguientes.

- Funcion para editar Videojuegos, Cheats, Easter Eggs y Opiniones.
- Funcion para eliminar Videojuegos, Cheats, Easter Eggs y Opiniones.
