import os
from PIL import Image


def pixelar_y_llenar_canvas():
    ruta_imagen = input(
        "Introduce la ruta de la imagen (ej. mi_imagen.jpg): "
    ).strip()

    if not os.path.exists(ruta_imagen):
        print("¡Error! El archivo no existe.")
        return

    try:
        img_original = Image.open(ruta_imagen)
    except Exception as e:
        print(f"No se pudo abrir la imagen: {e}")
        return

    LIENZO_X = 500
    LIENZO_Y = 500

    print("\n¿A qué resolución deseas pixelar?")
    print("1. Fuerte (25x25 bloques grandes)")
    print("2. Medio  (50x50 bloques medianos - Estilo Retro)")
    print("3. Suave  (100x100 bloques pequeños)")
    print("4. Alta definición (250x250 bloques mini - ¡Mucho detalle!)")
    opcion = input("Elige una opción (1, 2, 3 o 4): ").strip()

    if opcion == "1":
        nueva_res = 25
    elif opcion == "3":
        nueva_res = 100
    elif opcion == "4":
        nueva_res = 250
    else:
        nueva_res = 50  # Por defecto por si eligen la opción 2 o cualquier otra cosa

    #Paso 1: Pixelación real reduciendo resolución
    img_pixelada = img_original.resize(
        (nueva_res, nueva_res), resample=Image.Resampling.BILINEAR
    )
    img_pixelada = img_pixelada.convert("RGB")
    ancho_img, alto_img = img_pixelada.size

    #Calcular el tamaño de cada bloque (Para 250x250, esto dará exactamente 2)
    tamano_bloque_x = LIENZO_X // ancho_img
    tamano_bloque_y = LIENZO_Y // alto_img

    lineas_logo = []
    lineas_logo.append("cs pu rt 90")

    #Si el bloque mide 2, le sumamos 1 para que el grosor sea 3 y se solapen perfectamente
    grosor_lapiz = tamano_bloque_y + (1 if tamano_bloque_y < 5 else 1)
    lineas_logo.append(f"setpensize [{grosor_lapiz} {grosor_lapiz}]")

    print(f"\nGenerando bloques sólidos para {nueva_res}x{nueva_res}...")

    for y in range(alto_img):
        #Posición Y exacta
        pos_y = int(y * tamano_bloque_y) + (grosor_lapiz // 2)

        x = 0
        while x < ancho_img:
            r, g, b = img_pixelada.getpixel((x, y))

            #Compresión por color: contar píxeles idénticos seguidos
            píxeles_iguales = 1
            while (x + píxeles_iguales < ancho_img) and (
                img_pixelada.getpixel((x + píxeles_iguales, y)) == (r, g, b)
            ):
                píxeles_iguales += 1

            #Posición X de inicio exacta
            pos_x_inicio = int(x * tamano_bloque_x)
            lineas_logo.append(f"setxy {pos_x_inicio} {pos_y}")

            #Longitud del trazo horizontal
            distancia_avance = int(píxeles_iguales * tamano_bloque_x)

            #Pintar tramo continuo
            lineas_logo.append(f"color [{r} {g} {b}] pd fd {distancia_avance} pu")

            x += píxeles_iguales

    archivo_salida = "dibujo_logo_HD.txt"
    with open(archivo_salida, "w") as f:
        f.write("\n".join(lineas_logo))

    print(f"\n¡Listo! Tu archivo de LOGO se ha guardado en: {archivo_salida}")


if __name__ == "__main__":
    pixelar_y_llenar_canvas()
