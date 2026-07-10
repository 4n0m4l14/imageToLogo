FROM python:3.11-slim

# Directorio donde se guardará el script
WORKDIR /app

# Instalar Pillow
RUN pip install --no-cache-dir Pillow

# Copiar el script al contenedor
COPY imageToLogo.py /app/

# Cambiar el directorio de trabajo a /data
# Aquí es donde montaremos el volumen del sistema anfitrión
WORKDIR /data

# Ejecutar el script desde la ruta absoluta
CMD ["python", "/app/imageToLogo.py"]
