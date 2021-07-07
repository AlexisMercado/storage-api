# VG Submits

  Este proyecto consiste en una plataforma donde los usuarios puedan compartir
  sus opiniones, comentarios, datos curiosos etc. del videojuego de su
  eleccion, creando asi una gran libreria con informacion de Videojuegos.



## Entidades
Las entidades que se tienen en mente para el proyecto son las
siguientes:

- Usuario (Nombre, apellido, fecha_nac, Nickname_id, steam_id, XboxLive_id, PSN_id)

- Videojuego (Nombre, Genero, plataformas, VG_Id )

- Cheats (vg_codigo, Usuario_Nickname_id, cheat, cheat_id )

- Easter Egg (vg_codigo, Usuario_Nickname_id, Easter_Egg, Easter_Egg_id)

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

          "Nombre": "Bill"

          "apellido": "Williams"

          "fecha_nac": "1998-01-08"

          "Nickname_id": "Bi11"

          "steam_id":    "Billpcma$ter"

          "XboxLive_id": "Billynator"

          "PSN_id":      "Kid10"

    }
```

### Respuesta de registro de usuario exitosa

```

     {

          "Nickname_id": "Bi11"
    }
```

### Mensaje de fallo

```

     {

          "Code": "500"
          "mesagge": "Error al capturar Usuario"
    }
```
### Implementacion de la ruta para los recursos


`POST /vg-info/addUser`

*Recibe una estructura de registro de Usuario*     
*201, registra al ususario y regresa el Nickname_id*
*D.O.M, regresa estructura de mensaje de fallo*

`GET  /vg-info/addUser/<Nickname_id>`

*200 regresa la informacion de un usuario*
*D.O.M, regresa mensaje de fallo*

`POST /vg-info/add`

*Recibe una estructura de registro de un Videojuego*     
*201, registra al ususario y regresa el vg_codigo*
*D.O.M, regresa estructura de mensaje de fallo*     

`GET  /vg-info/list`

*200 regresa una lista de todos los Videojuegos en la aplicacion*
*D.O.M, regresa mensaje de fallo*   

`GET  /vg-info/<vg_codigo>`

*201, regresa la informacion de un videojuego*
*D.O.M, regresa mensaje de fallo*   

`POST /vg-info/<vg_codigo>/Cheats/`

*Recibe una estructura de registro de el cheat que el usuario quiera agregar*     
*201, registra al ususario y regresa el cheat_id*
*D.O.M, regresa estructura de mensaje de fallo*  

`GET  /vg-info/<vg_codigo>/Cheats`

*200 regresa una lista de todos los cheats de un juego en especifico*
*D.O.M, regresa mensaje de fallo*      

`POST /vg-info/<vg_codigo>/Easter_Egg`

*Recibe una estructura de registro de el Easter_Egg que el usuario quiera agregar*     
*201, registra al ususario y regresa el Easter_Egg_id*
*D.O.M, regresa estructura de mensaje de fallo*

`GET  /vg-info/<vg_codigo>/Easter_Egg`

*200 regresa una lista de todos los Easter Eggs de un juego en especifico*
*D.O.M, regresa mensaje de fallo*  

`POST /vg-info/<vg_codigo>/Opinion`

*Recibe una estructura de registro de la Opinion que el usuario quiera agregar*     
*201, registra al ususario y regresa la opinion_id*
*D.O.M, regresa estructura de mensaje de fallo*

`GET  /vg-info/<vg_codigo>/Opinion`

*200 regresa una lista de todas las opiniones de un juego en especifico*
*D.O.M, regresa mensaje de fallo*  
