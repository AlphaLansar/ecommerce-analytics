import os
import shutil
from .config import DATA_PROCESSED_PATH, DATA_LOAD_PATH

def load_clients():
    os.makedirs(DATA_LOAD_PATH, exist_ok=True)
    src_file = os.path.join(DATA_PROCESSED_PATH, "clients_processed.csv")
    dest_file = os.path.join(DATA_LOAD_PATH, "clients_final.csv")
    if os.path.exists(src_file):
        shutil.copy(src_file, dest_file)
        print(f"Clients chargés dans {dest_file}")
    else:
        print(f"[ERROR] Fichier clients introuvable : {src_file}")

def load_products():
    os.makedirs(DATA_LOAD_PATH, exist_ok=True)
    src_file = os.path.join(DATA_PROCESSED_PATH, "products_processed.csv")
    dest_file = os.path.join(DATA_LOAD_PATH, "products_final.csv")
    if os.path.exists(src_file):
        shutil.copy(src_file, dest_file)
        print(f"Produits chargés dans {dest_file}")
    else:
        print(f"[ERROR] Fichier produits introuvable : {src_file}")
