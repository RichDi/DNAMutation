## Instalacion

# Unix OS - Local Deploy
 
Paso 1: 
    
    Instalar las Dependencias

        $ sudo apt-get install python3
        $ sudo apt-get install python3-pip
        $ pip install virtualenv
    
Paso 2:

    Crear el entorno virtual

    Para hacer una instalacion limpia, lo mejor es instalar las dependencias en un entorno virtual

        $ virtualenv .venv
        $ source .venv/bin/activate

Paso 3:

    Instalar Django

        $ pip install django

Paso 4:

    Ejecutar el servidor

    Ir a la carpeta principal donde se encuentra ubicado manage.py

        $ python manage.py runserver

    














