# Videogames Info

  Este proyecto consiste en una plataforma donde los usuarios puedan compartir
  sus opiniones, comentarios, datos curiosos etc. del videojuego de su
  eleccion, creando asi una gran libreria con informacion de Videojuegos.

## Rutas

|                |RUTA                          
|----------------|-------------------------------|
|Captura         |`/vg-info/capture`            |
|Consulta        |`/vg-info/consulte`            |

Cualquier individuo podra acceder a la plataforma e inmediatamente llenar un
tipo formulario (que a su vez llenera un json) en el cual se capturara; el
titulo del *Videojuego*, *Su reseña*, *La calificacion*

##Entidades
Las entidades que se tienen en mente para el proyecto son las
siguientes:

-Videojuego (Nombre, Genero, plataformas, Codigo )
-Usuario (Nombre, apellido, edad, Nickname_id)
-Reseña (videojuego_codigo, Usuario_Nickname_id, opinion, calificacion)
