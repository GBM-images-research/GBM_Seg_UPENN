import os
import shutil
import random

def copiar_archivos(casos, ruta_original, ruta_destino, set_type):
    for caso in casos:
        # Crear estructura de carpetas en el nuevo dataset
        os.makedirs(os.path.join(ruta_destino, set_type, "labels"), exist_ok=True)
        os.makedirs(
            os.path.join(
                ruta_destino,
                set_type,
                "images",
                "images_structural",
                f"UPENN-GBM-{str(caso).zfill(5)}_11",
            ),
            exist_ok=True,
        )

        # Copiar archivos de automated_segm a ./train/labels
        archivo_segm_origen = (
            f"UPENN-GBM-{str(caso).zfill(5)}_11_automated_approx_segm.nii.gz"
        )
        archivo_segm_destino = os.path.join(
            ruta_destino, set_type, "labels", archivo_segm_origen
        )
        shutil.copy2(
            os.path.join(ruta_original, "automated_segm", archivo_segm_origen),
            archivo_segm_destino,
        )
        print(f"Copiando {archivo_segm_origen} a {archivo_segm_destino}")

        # Copiar archivos de images_structural a ./train/images
        carpeta_origen = os.path.join(
            ruta_original, "images_structural", f"UPENN-GBM-{str(caso).zfill(5)}_11"
        )
        carpeta_destino = os.path.join(
            ruta_destino,
            set_type,
            "images",
            "images_structural",
            f"UPENN-GBM-{str(caso).zfill(5)}_11",
        )

        for archivo in os.listdir(carpeta_origen):
            archivo_origen = os.path.join(carpeta_origen, archivo)
            archivo_destino = os.path.join(carpeta_destino, archivo)
            shutil.copy2(archivo_origen, archivo_destino)
            print(f"Copiando {archivo} a {archivo_destino}")


# Definir casos y rutas
total_casos = 611

# Calcular el número de casos para entrenamiento y validación
porcentaje_entrenamiento = 0.85
num_casos_entrenamiento = int(total_casos * porcentaje_entrenamiento)
num_casos_validacion = total_casos - num_casos_entrenamiento

# Generar una lista de casos del 1 al 611
todos_casos = list(range(1, total_casos + 1))

# Seleccionar de forma aleatoria los casos para entrenamiento y validación
casos_train = random.sample([caso for caso in todos_casos if caso != 509], num_casos_entrenamiento)
casos_valid = random.sample([caso for caso in todos_casos if caso != 509], num_casos_validacion)

print("Número de casos para entrenamiento:", len(casos_train))
print("Número de casos para validación:", len(casos_valid))

ruta_dataset_original = "D:\\CIA_UPENN_GBM\\NIfTI-files"
ruta_dataset_destino = "D:\\CIA_UPENN_GBM\\Dataset_new"

# Llamar a la función de copia
copiar_archivos(casos_train, ruta_dataset_original, ruta_dataset_destino, set_type="train")
copiar_archivos(casos_valid, ruta_dataset_original, ruta_dataset_destino, set_type="valid")