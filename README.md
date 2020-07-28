# MinTIC-DS4A-Project---Team-14

**Código del proyecto DS4A Clasificador de células de sangre periférica team 14**

***¿Como correr?**

* Instala Git https://git-scm.com/book/es/v2/Inicio---Sobre-el-Control-de-Versiones-Instalación-de-Git
* Clona este repositorio *git clone https://github.com/Fag42/MinTIC-DS4A-Project---Team-14*
* Entra en la carpeta del código *cd /MinTIC-DS4A-Project---Team-14*

**Si tienes instalado Docker:

* Crea la imagen de docker (si es necesario como administrador o sudo) *docker build -t ds4a . --no-cache*
* Ejecuta la aplicación (si es necesario como administrador o sudo) *sudo docker run -p 8080:8050 --name ds4a -v $(pwd):/var/www/app/public ds4a*
* La plicación debería ejecutarse en tu computador (localhost) y deberías poder verla en http://0.0.0.0:8080

**Si no tienes Docker:

* Asegurate de tener Python3.8 y pip3 instalado 
* Instala las librerias necesarias listadas en requirements.txt *pip3 install -r requirements.txt*
* Ejecuta la aplicación *python3 app1.py*
* La plicación debería ejecutarse en tu computador (localhost) y deberías poder verla en http://0.0.0.0:8050

**instrucciones para Construir la imagen del servidor, instalar librerias en el servidor y ejecutar pruebas en el servidor de azure (Próximamente..)
