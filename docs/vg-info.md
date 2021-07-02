# Videogames Info

  Este proyecto consiste en una plataforma donde los usuarios puedan compartir
  sus opiniones, comentarios, datos curiosos etc. del videojuego de su
  eleccion, creando asi una gran libreria con informacion de Videojuegos.

## API


|PATH                |                         
|----------------|-------------------------------|
|/vg-info/user/         |`informacion del usuario`               |
|/vg-info/vg/  |`Informacion basica de un videojuego`             |
|/vg-info/review/  |`La informacion del videojuego junto con los datos aportados por el usuario`               |


Cualquier individuo podra acceder a la plataforma e inmediatamente llenar un
tipo formulario (que a su vez llenera un json) en el cual se capturara; el
titulo del *Videojuego*, *Su reseña*, *La calificacion*

## Entidades
Las entidades que se tienen en mente para el proyecto son las
siguientes:

- Usuario (Nombre, apellido, edad, Nickname_id)

- Videojuego (Nombre, Genero, plataformas, Codigo )

- Opinion (videojuego_codigo, Usuario_Nickname_id, opinion, calificacion)

## Operaciones de Almacenamiento de datos
### Operaciones de Videojuegos

**Registrar un Videojuego**
- Solicitar el Nombre, Genero, plataformas
- El codigo del juego se generara de forma automatica
**Actualizacion del estatus del videojuego**
- Eliminar videojuego

### Operaciones de Usuario
**Registrar un usuario**
- Solicitar el nombre, apellido y edad
- El usuario podra elegir so propio Nickname_id

### Operaciones de Reseñas
**Ingresar una reseña**
- Se solicitara el Nickname_id del usuario que va a realizar la Reseña

- Se solicitara ingresar el codigo del juego el cual se quiere reseñar

- Se ingresaran la opinion del usuario sobre el videojuego y una calificacion del 1 al 10.
