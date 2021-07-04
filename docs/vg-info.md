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

- Opinion (vg_codigo, Usuario_Nickname_id, Opinion, calificacion, calificacion_id)



## API

|PATH                                     |                                                                  |
|-----------------------------------------|------------------------------------------------------------------|
|POST /vg-info/addUser                    |`Agregar usuario`                                                 |
|GET  /vg-info/addUser/<Nickname_id>      |`Consultar informacion del usuario`                               |
|POST /vg-info/add                        |`Capturar toda la informacion de un Videojuego`                   |
|GET  /vg-info/list                       |`Lista de videojuegos`                                            |
|GET  /vg-info/<vg_codigo>                |`Informacion de un Videojuego`                                    |
|POST /vg-info/<vg_codigo>/Cheats         |`Registrar un cheat de un videojuego`                             |
|GET  /vg-info/<vg_codigo>/Cheats         |`Mostrar todos los cheats registrados en un Videojuego`           |
|POST /vg-info/<vg_codigo>/Easter_Egg     |`Registrar un cheat de un videojuego`                             |
|GET  /vg-info/<vg_codigo>/Easter_Egg     |`Mostrar todos los cheats registrados en un Videojuego`           |
|POST /vg-info/<vg_codigo>/Opinion        |`Registrar un cheat de un videojuego`                             |
|GET  /vg-info/<vg_codigo>/Opinion        |`Mostrar todos los cheats registrados en un Videojuego`           |






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

## Estructura de solicitud y respuesta

### Registro de usuario

`{

  "Nombre": "Bill"

  "apellido": "Williams"

  "fecha_nac": "1998-01-08"

  "Nickname_id": "Bi11"

  "steam_id":    "Billpcma$ter"

  "XboxLive_id": "Billynator"

  "PSN_id":      "Kid10"

}`
