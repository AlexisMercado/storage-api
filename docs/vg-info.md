# VG Submits

  Este proyecto consiste en una plataforma donde los usuarios puedan compartir
  sus opiniones, comentarios, datos curiosos etc. del videojuego de su
  eleccion, creando asi una gran libreria con informacion de Videojuegos.



## Entidades
Las entidades que se tienen en mente para el proyecto son las
siguientes:

- Usuario (Nombre, apellido, edad, Nickname_id, steam_id, XboxLive_id, PSN_id)

- Videojuego (Nombre, Genero, plataformas, VG_Id )

- Cheats (vg_codigo, Usuario_Nickname_id, cheat, )

- Easter Egg (vg_codigo, Usuario_Nickname_id, Easter_Egg)

- Opinion (vg_codigo, Usuario_Nickname_id, Opinion, calificacion)



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
- Solicitar el nombre, apellido y edad
- El usuario podra elegir so propio Nickname_id

### Operaciones de Aporte
**Ingresar una aporte**
- Se solicitara el Nickname_id del usuario que va a realizar un Aporte

- Se solicitara ingresar el codigo del juego al cual se quiere agregar un aporte

- Se ingresaran el aporte del usuario sobre el videojuego.
