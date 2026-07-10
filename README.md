# Image to Logo

Este proyecto es un script en Python que toma una imagen y genera comandos del lenguaje **Logo** para dibujarla. Pixeliza la imagen reduciendo su resolución y crea un archivo de texto con las instrucciones necesarias.

## Requisitos

- Python 3.x
- Librería `Pillow`

## Instalación y Uso (Local)

1. Instala las dependencias:
   ```bash
   pip install Pillow
   ```
2. Ejecuta el script:
   ```bash
   python imageToLogo.py
   ```
3. Introduce la ruta de la imagen cuando se te solicite y elige el nivel de detalle. El resultado se guardará en `dibujo_logo_HD.txt`.

## Uso con Docker

Si no deseas instalar Python ni las dependencias, puedes usar **Docker**. El contenedor está configurado para poder leer imágenes de tu ordenador y guardar el archivo resultante directamente en tu disco.

1. **Construye la imagen Docker** (solo la primera vez):
   ```bash
   docker build -t image-to-logo .
   ```

2. **Ejecuta el contenedor**:
   Debes montar el directorio actual (`$PWD` en Linux/Mac o `%cd%` en Windows) dentro del contenedor para que pueda acceder a tu imagen y guardar el resultado.
   
   En **Linux/macOS**:
   ```bash
   docker run -it --rm -v "$PWD":/data image-to-logo
   ```

   En **Windows** (PowerShell):
   ```powershell
   docker run -it --rm -v "${PWD}:/data" image-to-logo
   ```
   
   En **Windows** (CMD):
   ```cmd
   docker run -it --rm -v "%cd%:/data" image-to-logo
   ```

3. Cuando el script te pregunte por la ruta de la imagen, simplemente escribe el nombre del archivo (si está en la misma carpeta desde donde ejecutaste el comando), por ejemplo: `mi_imagen.jpg`.
4. El archivo generado `dibujo_logo_HD.txt` aparecerá mágicamente en tu carpeta actual.
