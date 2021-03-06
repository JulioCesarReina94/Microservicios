Integrantes: 

Julio Cesar Reina      20201099045

Cristian Gonzalez   20201099032

Andres Lozano          20201099038

# Microservicios


## 1. DEFINICIONES
### MICROSERVICIOS

Según James Lewis y Martin Fowler (los creadores del concepto) los microservicios son un enfoque para desarrollar una única aplicación como un conjunto de pequeños servicios, cada uno ejecutándose en su propio proceso y comunicándose con mecanismos ligeros, a menudo una API a través de HTTP.

Estos servicios se desarrollan alrededor de capacidades de negocio y se pueden implementar de forma independiente y completamente automatizada. Existe un mínimo de administración centralizada de estos servicios, que puede escribirse en diferentes lenguajes de programación y utilizando diferentes tecnologías de almacenamiento de datos.

Los microservicios se adaptan perfectamente a los requerimientos de agilidad, escalabilidad y confiabilidad de las aplicaciones modernas en la nube.

### FLASK

Flask es auto denominado como un microframework de python para crear aplicaciones web, es decir, páginas web dinamicas, APIs, etc. Una de las principales características de Flask es que se pueden crear aplicaciones web rápidamente y con un mínimo número de líneas de código.

### CONFIGURATION SERVICE

#### DOCKER

Docker es una plataforma de software que le permite crear, probar e implementar aplicaciones rápidamente. Docker empaqueta software en unidades estandarizadas llamadas contenedores que incluyen todo lo necesario para que el software se ejecute, incluidas bibliotecas, herramientas de sistema, código y tiempo de ejecución. Con Docker, puede implementar y ajustar la escala de aplicaciones rápidamente en cualquier entorno con la certeza de saber que su código se ejecutará.

Algunos de los comandos más utilizados en Docker son:

- docker pull NOMBREIMAGEN. Este comando sirve para descargar una imagen

- docker images  muestra imágenes que tenemos descargadas

- docker ps -a    muestra que contenedores están funcionando

- docker rmi  IMAGE_ID  Elimina (y desmarca) una o más imágenes del nodo host.

- docker info  Muestra información de las imágenes, tamaño, fecha creación  nombre...

- docker search NAME   para buscar in docker

- docker inspect <friendly-name|container-id> . para saber acerca del contenedor

- docker logs <friendly-name|container-id> Comandos para el contenedor.

- docker start: Iniciar uno o más contenedores detenidos.

- docker stop: Detener uno o más contenedores en ejecución.

- docker kill: Mata uno o más contenedores en funcionamiento.

- docker rm: Retira uno o más contenedores.

- docker run : ejecuta el proceso de contenedor. Para iniciar un contenedor en segundo plano, use simplemente la -d opción.

### API GATEWAY

Un API Gateway proporciona un punto central de acceso a todos los clientes para gestionar, supervisar y asegurar el acceso a los servicios backend expuestos, que ofrecen los productos digitales.

#### KONG

Kong es una API Gateway encargada de unificar la publicación de APIs para que sean consumidas por otras aplicaciones o por los desarrolladores.

- Kong Server: Es la pieza que hace de proxy de todas las peticiones. Consta de una capa pública por la cual le llegan las peticiones para acceder a las APIs que expone y otra privada para la administración y configuración de las mismas. Además nos permite habilitar, deshabilitar y configurar los plugins instalados.

- Kong Datastore: Es una base de datos externa que sirve como almacenamiento de todas las configuraciones de Kong y sus plugins o APIs. Los datastore soportados por defecto son Cassandra y PostgreSQL.

![FIGURA 15](Imagenes/Figura15.png)


Figura 1.  Estructura Api Gateway -Kong 

#### TYK

Tyk es un API Gateway open-source que nació en 2014. Tyk está desarrollado en Golang y utiliza el servidor HTTP del propio lenguaje.
Si queremos utilizar Tyk disponemos de varias opciones: Cloud, Hybrid (GW en infraestructura propia) y On-Premises.
Existen varias formas de instalar Tyk: paquetería estándar de Ubuntu y RHEL, tarball o contenedor de Docker.
Tyk está compuesto por 3 piezas:

- Gateway: El proxy por el que pasa todo el tráfico de nuestras aplicaciones.

- Dashboard: La interfaz desde la cual podemos administrar Tyk, visualizar las métricas y organizar las API.

- Pump: Es el encargado de persistir los datos de las métricas y exportarlas a MongoDB (instalación de serie), ElasticSearch, InfluxDB entre otros.

### BALANCEO DE CARGA 

#### KONG

Kong proporciona múltiples formas de solicitudes de equilibrio de carga a múltiples servicios de back-end: un método directo basado en DNS y un equilibrador de anillo más dinámico que también permite el registro del servicio sin necesidad de un servidor DNS

#### RIBBON 

Parte del stack tecnológico de Netflix OSS. El cual permite realizar el balanceo de carga por medio de Eureka.

#### NGINX

Pronunciado como “engine-ex”, es un servidor web de código abierto que, desde su éxito inicial como servidor web, ahora también es usado como proxy inverso, caché de HTTP, y balanceador de carga.

### CENTRALIZACION DE LOGS 

#### FLUENTD

Es un recolector de datos, es decir, se dedica a buscar y recoger toda la información que generan las diferentes aplicaciones de tu sistema. Su principal característica es la conexión de distintas fuentes de datos con múltiples destinos (desde bases de datos a servicios web, otros ficheros, etc.).

#### GRAYLOG

Es una solución de software de código abierto para el almacenamiento y visualización de los logs generados. Permite, además, realizar consultas sobre los datos, crear cuadros de mando, alarmas y muchas otras funcionalidades interesantes en entornos de TI y programación. Se compone de tres componentes fundamentales:

- Mongo DB: Es el almacén de configuraciones y metadatos.

- ElasticSearch: Actúa como motor de búsquedas y almacenamiento.

- Graylog Server: Es el propio servidor de Graylog que incluye todas sus funcionalidades y una interfaz de usuario web (Graylog UI).

### SERVIDOR DE AUTORIZACION

#### Plugin LDAP Authentication (KONG)

Es un plugin de kong que permite implementar el servicio de autorización, este permite verificar las credenciales válidas en el encabezado, es compatible con solicitudes de los protocolos http y https.

### CLIENTE

#### POSTMAN 

Es una herramienta que nos permite crear peticiones sobre APIs de una forma muy sencilla y poder, de esta manera, probar las APIs. Todo basado en una extensión de Google Chrome. El usuario de Postman puede ser un desarrollador que esté comprobando el funcionamiento de una API para desarrollar sobre ella o un operador el cual esté realizando tareas de mnonitorización sobre un API.


## 	2. INSTALACION

###	KONG
Para Instalar Kong con Docker primero se deben establecer una base de datos, puede ser cassandra  o postgres, el siguiente comando permite realizar su creación: 

- **docker run -d --name kong-database -p 5432:5432 -e "POSTGRES_USER=kong" -e "POSTGRES_DB=kong" postgres:9.5**

Una vez creada, podemos ejecutar el comando para instalar Kong:

- **docker run -d --name kong --link kong-database:kong-database -e KONG_DATABASE=postgres -e KONG_PG_HOST=kong-database -p 8000:8000 -p 8443:8443 -p 8001:8001 -p 7946:7946 -p 7946:7946/udp kong:0.10.1**


Si todo a salido bien, en el dashboard de Docker se podrán visualizar los dos contenedores

![FIGURA 1](Imagenes/Figura1.png)

Figura 2.  Contenedores para Kong y su base de datos en Docker


###	API CON FLASK
Para crear los microservicios con Flask, primero se debe tener instalado python y basta con hacer una importación para poderlo usarlo. A continuación, se pude visualizar un servicio en Flask en donde se importa flask y jsonify, request para manejar respuestas en formato json para el servicio.
Cada marco web comienza con el concepto de servir contenido en una URL determinada, así pues, se incluye la notación @app. route, en donde se define una ruta y el tipo de método para acceder a esta como POST o GET. Enseguida se define una función y se procede la realizar la respectiva lógica del servicio.
En este archivo, también se define el host y el puerto a través del cual el servicio estará expuesto, para el caso es localhost y el puerto 100

![FIGURA 2](Imagenes/Figura2.png)

Figura 3. Archivo Multiplicacion.py

Es importante resaltar que se debe tener un archivo para cada uno de los servicios que se quiere exponer, en donde solo varia el nombre de la ruta, la lógica del servicio y el puerto en donde se quiere desplegar, como se puede visualizar en la siguiente imagen:


![FIGURA 3](Imagenes/Figura3.png)

Figura 4. Archivo Resta.py

Una vez que ya se tienen los servicios a desplegar se procede a crear un archivo llamado Dockerfile, un archivo de texto plano que contiene las instrucciones necesarias para automatizar la creación de una imagen que será utilizada posteriormente para la ejecución de instancias específicas.
Así pues, en este archivo se define principalmente un sistema operativo Linux, para el caso es Alpine en su versión 3.10, enseguida se ejecuta el administrador de paquetes apk para agregar o instalar Python y de igual forma pip. Para se mas automático el proceso, se crea una carpeta o directorio llamada app, en ella se copia todos los archivos utilizados. 

![FIGURA 4](Imagenes/Figura4.png)

Figura 5. Archivo Dockerfile

También es necesario instalar los componentes necesarios para correr la aplicación, para el caso Flask, es por esto que se debe crear un archivo llamado requeriments.txt y ejecutarlo. Una vez que todo esta instalo se procede a correr la aplicación con el comando CMD.

![FIGURA 5](Imagenes/Figura5.png)

Figura 6. Archivo requeriments.txt

Una vez, ya se tiene todo configurado, se procede a generar la imagen en Docker a través del siguiente comando:

![FIGURA 6](Imagenes/Figura6.png)

Figura 7. Comando generación de imagen en Docker

Este comando creara una nueva imagen y realizara todos los pasos o sentencia definidos en el archivo Dockerfile. Enseguida se debe ejecutar la imagen creada, esto a través del comando:


![FIGURA 7](Imagenes/Figura7.png)

Figura 8. Comando ejecución imagen en Docker

Se debe resaltar que en este comando se define el nombre de la imagen, y además con que puerto se quiere relacionar, es decir, en el contenedor la aplicación se expondrá en el puerto 100, pero en nuestra maquina local no tenemos acceso a este, por lo cual se debe relacionar. Para el caso se relaciona el puerto 100 con el puerto 100. 
Si todo se ejecuta correctamente tendremos un nuevo contenedor y podremos probar el servicio publicado, para el caso se puede utilizar el software Postman:


![FIGURA 8](Imagenes/Figura8.png)

Figura 9. Contenedor en Docker para el servicio de multiplicación.


![FIGURA 9](Imagenes/Figura9.png)

Figura 10. Servicio que cumple la función de multiplicar.

Así pues, ya se tiene el servicio de multiplicar expuesto y funcionando. Para crear los servicios de las demás operaciones matemáticas se debe hacer el mismo procedimiento con los demás archivos, configurando en el archivo Dockerfile, la aplicación que se quiere iniciar, y teniendo en cuenta los puertos de exposición. 

Para el caso se creó el contenedor división expuesto en el puerto 70, multiplicación en el puerto 100, resta en el puerto 90 y por ultimo la suma en el puerto 80.


![FIGURA 10](Imagenes/Figura10.png)
Figura 11. Contenedores creados en Docker.


###	CONFIGURACION KONG

Para la configuración de Kong se utilizó el software KongDash, esto con el fin de hacerlo más gráfico y visual. En este software se procede a configurar cada una de las Apis a gestionar. Así pues, para teniendo en cuenta el api de multiplicación se define un nombre, el host donde se expondrá y la URI y Upstream URL a donde se redireccionará las peticiones, como se puede ver en la imagen.

![FIGURA 11](Imagenes/Figura11.png)

Figura 12. Creación de api en Kong.

Una vez configurado se procede a probar el servicio desde el Gateway, para el caso el host es localhost, el puerto 8000 y la URI definida


![FIGURA 12](Imagenes/Figura12.png)

Figura 13. Prueba servicio multiplicación desde el Gateway

Teniendo una prueba satisfactoria, se procede a crear las Apis para los demás servicios en Kong
 

![FIGURA 13](Imagenes/Figura13.png)
Figura 14. Apis creadas en Kong

Para finalizar se podrá ver todos los contenedores en Docker funcionado correctamente

![FIGURA 14](Imagenes/Figura14.png) 
Figura 15. Contenedores creados en Docker

Conclusiones

- En su mayoria las aplicaciones basadas en microservicios deberían consumirse mediante una API Gateway, para que interactúe como un único punto de entrada en el conjunto de microservicios, enrutando las solicitudes y la traducción de protocolos.

- Cada servicio componente en una arquitectura de microservicios se puede desarrollar, implementar, operar y escalar sin afectar el funcionamiento de otros servicios. Los servicios no necesitan compartir ninguno de sus códigos o implementaciones con otros servicios. 


Referencias Web


- https://blog.mdcloud.es/que-son-los-microservicios-definicion-caracteristicas-y-retos/

- https://aws.amazon.com/es/docker/

- https://danielcastanera.com/comandos-utiles-en-docker/docker 

- http://www.arquitectoit.com/postman/que-es-postman/

- https://www.bbva.com/es/tyk-kong-analizamos-estos-dos-api-gateways/

- https://medium.com/@jovaniarzate/apis-y-microservicios-en-empresas-monol%C3%ADticas-api-gateway-y-management-6-69ba6dd0080c
