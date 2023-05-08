FROM ubuntu:latest

# Actualiza el sistema y añade las dependencias necesarias
RUN apt-get update && \
    apt-get install -y python3-pip python3-dev && \
    apt-get install -y build-essential libssl-dev libffi-dev python3-setuptools

# Crea y cambia al directorio de trabajo de la aplicación
RUN mkdir /app
WORKDIR /app

# Copia los archivos necesarios a la imagen de Docker
COPY requirements.txt /app/
COPY . /app/

# Instala las dependencias de la aplicación
RUN pip3 install -r requirements.txt

# Expone el puerto 8000 para acceder a la aplicación
EXPOSE 8000

# Define el comando para ejecutar la aplicación
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
