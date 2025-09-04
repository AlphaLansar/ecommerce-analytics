import os

BASE_PATH = os.path.dirname(os.path.abspath(__file__))

SERVICE_ACCOUNT_FILE = os.path.join(BASE_PATH, "service_account.json")

DATA_RAW_CLIENTS_PATH = os.path.join(BASE_PATH, "../../../data/raw_data/clients")
DATA_RAW_PRODUCTS_PATH = os.path.join(BASE_PATH, "../../../data/raw_data/products")
DATA_PROCESSED_PATH = os.path.join(BASE_PATH, "../../../data/processed")
DATA_LOAD_PATH = os.path.join(BASE_PATH, "../../../data/load")
