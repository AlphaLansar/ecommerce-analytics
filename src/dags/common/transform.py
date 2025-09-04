import pandas as pd
import os
from .config import DATA_RAW_CLIENTS_PATH, DATA_RAW_PRODUCTS_PATH, DATA_PROCESSED_PATH

def transform_clients():
    os.makedirs(DATA_PROCESSED_PATH, exist_ok=True)
    all_files = [os.path.join(DATA_RAW_CLIENTS_PATH, f) for f in os.listdir(DATA_RAW_CLIENTS_PATH) if f.endswith(".csv")]
    
    df_list = []
    for f in all_files:
        try:
            df = pd.read_csv(f)
            if not df.empty:
                df_list.append(df)
            else:
                print(f"[WARNING] Fichier vide ignoré : {f}")
        except pd.errors.EmptyDataError:
            print(f"[WARNING] Fichier invalide ignoré : {f}")
    
    if df_list:
        df_clients = pd.concat(df_list, ignore_index=True)
        df_clients = df_clients.drop_duplicates()
        df_clients.to_csv(os.path.join(DATA_PROCESSED_PATH, "clients_processed.csv"), index=False)
        print("Clients transformés et enregistrés.")
    else:
        print("[ERROR] Aucun fichier client valide trouvé.")

def transform_products():
    os.makedirs(DATA_PROCESSED_PATH, exist_ok=True)
    products_file = os.path.join(DATA_RAW_PRODUCTS_PATH, "products.csv")
    try:
        df_products = pd.read_csv(products_file)
        if not df_products.empty:
            df_products = df_products.drop_duplicates()
            df_products.to_csv(os.path.join(DATA_PROCESSED_PATH, "products_processed.csv"), index=False)
            print("Produits transformés et enregistrés.")
        else:
            print(f"[ERROR] Fichier produit vide : {products_file}")
    except pd.errors.EmptyDataError:
        print(f"[ERROR] Fichier produit invalide : {products_file}")
