# pruebaUsuario


1.Crear Ambiente virtual con:

python -m venv env

2.Porfavor instalar las dependencias necesarias del archivo requirements.txt  desde la raiz del projecto, con el siguiente comando

pip install -r requirements.txt

Para tener en cuenta, en Pruebas con PostMan:
        Crear usuario
Para crear un Usuario,Se usa la direccion:
http://127.0.0.1:8000/user/

Metodo: POST

Con la siguiente estructura:

{
    "documento":"1051449969",
    "password":"admin",
    "username": "hugo",
    "email": "hugomarrugopolo28@hotmail.com",
    "nombres": "Hugo Andres",
    "apellidos":"Marrugo Polo"
}

    Ver detalle Usuario
Para ver en detalle un usuario, se usa el documento,en la siguiente direccion:
Metodo GET

http://127.0.0.1:8000/user/1051449968


    Login
Para Hacer un Login, se usa la direccion:
Metodo POST
http://127.0.0.1:8000/login/

Para loguearse se usa el username
se ingresa en el body:
{
    "username":"hugoA",
    "password":"****"
}
