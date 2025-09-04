# main.py
from src.dags.common.extract import extract_clients, extract_products
from src.dags.common.transform import transform_clients, transform_products
from src.dags.common.load import load_clients, load_products

def main():
    print("=== Extraction des clients ===")
    extract_clients()

    print("=== Extraction des produits ===")
    extract_products()

    print("=== Transformation des clients ===")
    transform_clients()

    print("=== Transformation des produits ===")
    transform_products()

    print("=== Chargement des clients ===")
    load_clients()

    print("=== Chargement des produits ===")
    load_products()

    print("=== Pipeline ETL terminé ===")

if __name__ == "__main__":
    main()
