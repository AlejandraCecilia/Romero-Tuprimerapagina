Entrega Final
Web Django con patrón MVT: Mi primer aplicación.

1. Breve Descripción:
Se trata de una web para un consultorio médico donde se atienden distintas especialidades. La funcionalidad relacionada con las especialidades está en la aplicacion 'inicioceci' y todo lo relacionado con usuario y autenticación esta en la aplicación 'users'.
Acceso a video: 
https://drive.google.com/file/d/12SldQOU9yea71dNvHz7OC42ufC3afxMh/view?usp=sharing


2. Puntos trabajados

* Entrega individual
* subir a github
* readme como la entrega 3
* video de maximo 10 min que muestre la pagina y sus funcionalidades (con o sin audio)
* Uso de herencia de templates
* Exista gitignore
* Existencia del archivo requirements.txt actualizado.
* Uso de minimo 2 clases basadas en vista.
* Uso de minimo un mixin en una CBV y un decorador en una view comun.
* Hacer uso de Estaticos (carpeta static con la carga de templates desde bootstrap)
* Una vista de inicio
* Crear un modelo principal que contenga los siguiente campos como minimo: 3 Charfield (o 2 Charfield y un Integerfield), 1 campo de imagen, 1 de fecha
* Vista de listado de los objetos del modelo principal (modelo a eleccion). En la cual cada objeto mostrara solo alguno de sus datos
* Mensaje que de aviso en caso de no haber ningun objeto creado o al utilizar el buscador no encontrar tampoco algun objeto
* Desde el listado:
-poder acceder a una vista que muestre el detalle de el objeto seleccionado
-poder acceder a una vista de creacion, una de edicion y una de borrado de los objetos del listado

* Registrar en el apartado de admin todos los modelos creados

* Tener una app para el manejo de todas las vistas relacionadas al usuario/autenticacion

* Desarrollar las vistas para un login, un logout y el registro de un usuario al cual se le solicite: username, email, password



3. Pasos Creación Proyecto Django.

1. creamos una carpeta donde vamos a meter el proyecto

2. entramos en la carpeta y la abrimos con vscode

3. inicializamos git

4. creamos el archivo .gitignore le guardamos lo generado por la pagina gitignore.io seleccionando lo que van a utilizar (en nuestro caso visualstudiocode, python y django)

5. creamos el entorno virtual python -m venv <nombre_de_la_carpeta_que_contiene_el_entorno_virtual>

6. agregar el nombre del entonrno virtual al .gitignore (no lo agregué porque usé el genérico)

7. conectamos nuestro repositorio con el repositorio en la nube (github u otro)

8. creamos el primer commit

9. hacemos el primer push (me pidió un especie de autenticación github)

10. activo el entorno virtual

11. instalo Django

12. crear el requirements.txt con los datos de las dependencias usando el comando pip freeze > requirements.txt

13. crear el proyecto django donde estamos trabajando con el comando django-admin startproject <nombre_del_proyecto> .
14. probamos el proyecto ejecutando primero python manage.py migrate y luego python manage.py runserver

15. creamos nuestra app principal con el comando python manage.py startapp <nombre_de_la_app>. Mi app se llama inicioceci

16. agregamos la app a el archivo settings.py

17. creamos el archivo urls.py dentro de nuestra app inicioceci

18. agregamos el path que conecta al urls.py de la carpeta donde esta el settings.py al de nuestra app con el codigo path('<url_que_quieran_poner>', include('<nombre_de_la_app>.urls'))
En mi caso: path('', include('inicioceci.urls'))

19. agregamos el valor BASE_DIR / 'templates' a la lista en la key DIRS de la variable TEMPLATES en el archivo settings.py

20. creamos la carpeta templates a la altura de la apps (inicioceci)

21. crear vistas

 -crear el path que conectara con su vista en el archivo urls.py de la app que corresponda

 -crear la vista en el archivo views.py de la app que corresponda

 -crear el template que se utilizará para la vista dentro de la carpeta templates
 
 -agregar el link (etiqueta a) al path que corresponde a la vista

22. crear modelos

-crear modelo dentro de el archivo models.py
-heredan de models.Model
-los atributos los completan con los Fields que les brinda models ejemplo models.CharField(max_length=20)
-generar una migracion con el comando python manage.py makemigrations
-plasmar la migracion en la bd con el comando python manage.py migrate
-importar el modelo creado en el views.py que corresponda para utilizarlo en las vistas

23. crear formularios

-crear el archivo forms.py dentro de la app que corresponda en caso que no este creado
-crear el formulario
-heredan de forms.Form
-importar el formulario creado en el views.py que corresponda para utilizarlo en las vistas
