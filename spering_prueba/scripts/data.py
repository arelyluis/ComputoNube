import kaggle
import os


# Definir la carpeta de destino dentro del proyecto
data_dir = os.path.join(os.path.dirname(__file__), "../public_html/data")
print(data_dir)

# Asegurar que la carpeta existe
os.makedirs(data_dir, exist_ok=True)

# Nombre del dataset en Kaggle
dataset_name = "ashaychoudhary/social-media-and-entertainment-dataset"

# Descargar el dataset en la carpeta de destino
print(f"Descargando {dataset_name} en {data_dir}...")
kaggle.api.dataset_download_files(dataset_name, path=data_dir, unzip=True)

print(" Descarga completa :)")

