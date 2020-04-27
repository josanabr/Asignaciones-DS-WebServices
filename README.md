# Monitoreo de Servidor via Web Services

Los Web Services que siguen el estilo arquitectural RESTful son bastante populares hoy en día. 
Muchas de las plataformas centradas en la nube ofrecen este tipo de servicios para que sus usuarios y terceros puedan sacar provecho de la información y los servicios que ellos proveen y gestionan.

El microframework Flask permite el fácil desarrollo y despliegue de servicios que siguen el esquema arquitectura RESTful.
Uno de los elementos centrales de la arquitectura RESTful es la identificación de un recurso para que este se pueda acceder como un *web service*.
Para efectos de este taller el recuro a modelar es un servidor.

## Información a exponer de parte del servidor
Para efectos de este taller usted deberá proveer un *web service* que brinde información de un servidor. 
La información que se desea se presente es la siguiente:

* Memoria RAM:
  * ¿Cuánta memoria RAM tiene el sistema?
  * ¿Cuánta memoria RAM esta usada por el sistema?

* Disco:
  * ¿Cuánto espacio en disco tiene asignado el punto de monte `/`?
  * ¿Cuánto espacio disponible tiene el punto de monte `/`?
  * ¿Cuántas particiones tiene montadas este servidor?
  * ¿Cuánto espacio en disco tiene asignada una partición 'X'?
  * ¿Cuánto espacio disponible tiene la partición 'X'?

* Procesamiento:
  * ¿Cuántas unidades de procesamiento tiene el servidor?
  * ¿Cuál es la carga del servidor en el último minuto, últimos cinco minutos, últimos quince minutos?
  * ¿Cuántos procesos están corriendo en el sistema?
  * ¿Cuántos usuarios están corriendo procesos en el sistema?
  * ¿Cuántos procesos el usuario 'X' está corriendo en el sistema?

* Características del servidor:
  * ¿Qué sistema operativo corre?
  * ¿Qué arquitectura tiene este computador?
  * ¿Qué distribución de Linux tiene (nombre y versión)? De no ser Linux, arrojar como respuesta 'Otro sistema'.

* El *web service* deberá permitirle al usuario ejecutar un comando arbitrario. **Si, es un riesgo de seguridad pero esta es una actividad académica.**


