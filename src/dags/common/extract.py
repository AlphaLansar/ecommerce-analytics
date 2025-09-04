import os
import io
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload
from google.oauth2 import service_account
from src.dags.common.config import (
    SERVICE_ACCOUNT_FILE,
    DATA_RAW_CLIENTS_PATH,
    DATA_RAW_PRODUCTS_PATH
)

SCOPES = ["https://www.googleapis.com/auth/drive.readonly"]

def get_service():
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES
    )
    return build("drive", "v3", credentials=credentials)

def list_files(service, folder_id):
    query = f"'{folder_id}' in parents"
    results = service.files().list(q=query, fields="files(id, name)").execute()
    return results.get("files", [])

def download_file(file_id, dest_path, is_sheet=False):
    service = get_service()
    if is_sheet:
        request = service.files().export_media(fileId=file_id, mimeType="text/csv")
    else:
        request = service.files().get_media(fileId=file_id)

    fh = io.FileIO(dest_path, "wb")
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while not done:
        status, done = downloader.next_chunk()
        if status:
            print(f"Téléchargé {int(status.progress() * 100)}%")
    print(f"Fichier enregistré : {dest_path}")

def extract_clients():
    print("=== Extraction des clients ===")
    service = get_service()
    folder_id = "13f1lr1lWPkreYGf84kbQXP7O6ykWrmjm"  # dossier clients sur Drive

    files = list_files(service, folder_id)
    if not files:
        print("Aucun fichier client trouvé.")
        return

    os.makedirs(DATA_RAW_CLIENTS_PATH, exist_ok=True)
    for f in files:
        dest_path = os.path.join(DATA_RAW_CLIENTS_PATH, f["name"].replace("Copy of ", ""))
        download_file(f["id"], dest_path, is_sheet=False)

def extract_products():
    print("=== Extraction des produits ===")
    service = get_service()
    folder_id = "1tkR3F16D4bUXFeSvMLx_BtiNaXmmTZwo"  # dossier products sur Drive

    files = list_files(service, folder_id)
    if not files:
        print("Aucun fichier produit trouvé.")
        return

    os.makedirs(DATA_RAW_PRODUCTS_PATH, exist_ok=True)
    # On prend le premier ; ajoute de la logique si plusieurs
    filename = files[0]["name"].replace("Copy of ", "")
    dest_path = os.path.join(DATA_RAW_PRODUCTS_PATH, filename)
    download_file(files[0]["id"], dest_path, is_sheet=False)
