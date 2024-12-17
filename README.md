# examen-Capi1Paso 
1: Crear la aplicación Flask

Crea un nuevo directorio para tu aplicación:
mkdir mi_app
cd mi_app

1.2. Crear la aplicación Flask (app.py)
Ahora, crea el archivo principal de tu aplicación Flask. Usaremos un archivo básico de Flask que muestra una página con una lista de tareas.

nano app.py

2. Agrega la estructura básica
bre el archivo README.md en tu editor de texto o IDE favorito y empieza con la estructura básica del documento.

Aquí te dejo un ejemplo que puedes adaptar según tu proyecto.
# Flask Docker App

Este proyecto es una aplicación web Flask conteneurizada con Docker. La aplicación está configurada para ejecutarse en un entorno de Docker con una imagen de Python oficial. Aquí están las instrucciones para ejecutarla localmente y dentro de un contenedor Docker.

## Requisitos

- Python 3.x
- Docker (si deseas ejecutar la aplicación en un contenedor)

### Instalación y Ejecución Local

1. Clona este repositorio en tu máquina local:

   ```bash
   git clone https://github.com/Maykel2402/flask-docker-app.git
   cd flask-docker-app

   Crea y activa un entorno virtual:
   python -m venv venv
source venv/bin/activate  # Para Linux y macOS
venv\Scripts\activate     

Instala las dependencias del proyecto:
pip install -r requirements.txt

Ejecuta la aplicación localmente:
flask run
Abre tu navegador y ve a http://localhost:5000.

Ejecución con Docker
Requisitos:
Docker instalado en tu sistema.

Pasos para ejecutar el contenedor:
Clona este repositorio:
git clone https://github.com/Maykel2402/flask-docker-app.git
cd flask-docker-app

Construye la imagen Docker:
docker build -t maykel2402/examen:latest .

Corre el contenedor:
docker run -p 5000:5000 maykel2402/examen:latest
abre tu navegador y visita http://localhost:5000.

Ejecutar imagen desde Docker Hub
También puedes descargar y ejecutar la imagen desde Docker Hub sin necesidad de construirla localmente:
docker pull maykel2402/examen:latest
docker run -p 5000:5000 maykel2402/examen:latest

Verifica que Docker esté funcionando
Para confirmar que el contenedor funciona en multiplataforma (por ejemplo, en Windows o Linux):

Abre Docker Desktop en tu sistema operativo preferido (Windows, Linux).
Sigue los pasos de Ejecución con Docker para asegurarte de que la aplicación funciona en tu sistema.

Estructura del Proyecto
flask-docker-app/
│
├── app.py                 # Archivo principal de la aplicación Flask
├── Dockerfile             # Archivo Docker para crear la imagen
├── requirements.txt       # Dependencias del proyecto
├── README.md              # Instrucciones del proyecto
└── venv/                  # Entorno virtual (no se incluye en el repositorio)

Créditos
Este proyecto fue desarrollado por Maykel2402.

### 3. **Guarda y haz commit de tu README.md**

Guarda el archivo, y luego haz un commit del mismo a tu repositorio de GitHub. Ejecuta los siguientes comandos desde tu terminal:

```bash
git add README.md
git commit -m "Agregado archivo README.md con instrucciones"
git push origin main

. Verifica el README en GitHub
Una vez subido el archivo README.md, ve a tu repositorio en GitHub para verificar que se muestre correctamente en la página principal del repositorio.

¡Con esto tendrás un archivo README.md bien estructurado que documenta tu proyecto y las instrucciones para ejecutarlo!
