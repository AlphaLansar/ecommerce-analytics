# Ecommerce Analytics - Projet ETL

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Pandas](https://img.shields.io/badge/Pandas-1.6.2-lightgrey)
![Google API](https://img.shields.io/badge/Google-API-green)

## 📌 Contexte

Ce projet a été réalisé dans le cadre de la formation **Data Engineering**. L'objectif est de mettre en place un **pipeline ETL complet** pour collecter, transformer et charger des données e-commerce provenant de Google Drive, puis les préparer pour analyse.

Le pipeline prend en charge :
- Les données clients (plusieurs fichiers CSV).
- Les données produits (fichier CSV unique).

## 📁 Structure du projet

```
ecommerce-analytics/
│
├─ data/
│  ├─ raw_data/
│  │  ├─ clients/          # Fichiers clients téléchargés depuis Google Drive
│  │  └─ products/         # Fichier produits téléchargé depuis Google Drive
│  ├─ processed/           # Fichiers transformés (nettoyés et concaténés)
│  └─ load/                # Fichiers finaux prêts pour utilisation ou analyse
│
├─ src/
│  ├─ dags/
│  │  └─ common/
│  │     ├─ extract.py     # Extraction depuis Google Drive
│  │     ├─ transform.py   # Transformation et nettoyage des fichiers
│  │     └─ load.py        # Chargement des fichiers transformés
│  └─ config.py            # Configuration des chemins et Service Account
│
├─ main.py                 # Script principal pour lancer l'ETL complet
└─ README.md
```

## ⚙️ Fonctionnement du pipeline ETL

Le pipeline comprend trois étapes : **Extraction, Transformation et Chargement**.

### 1. Extraction (extract.py)
- Récupère les fichiers clients et produits depuis Google Drive.
- Télécharge les fichiers dans `data/raw_data/clients` et `data/raw_data/products`.
- Gestion des erreurs pour fichiers non trouvés ou inaccessibles.

### 2. Transformation (transform.py)
- Clients : concaténation de tous les CSV, suppression des doublons, vérification des fichiers vides.
- Produits : lecture du fichier unique, suppression des doublons et gestion des erreurs.
- Sauvegarde des fichiers transformés dans `data/processed/`.

### 3. Chargement (load.py)
- Déplace les fichiers transformés vers `data/load/` pour utilisation ou analyse.
- Fichiers finaux :
  - `clients_final.csv`
  - `products_final.csv`

## 🛠️ Prérequis

- Python 3.10 ou supérieur
- Bibliothèques :
```bash
pip install pandas google-api-python-client google-auth google-auth-httplib2 google-auth-oauthlib
```
- Service Account Google Drive configuré avec accès aux fichiers CSV.

## 🚀 Instructions pour exécuter le projet

1. **Cloner le dépôt**
```bash
git clone <URL_DE_TON_REPO>
cd ecommerce-analytics
```

2. **Créer les dossiers nécessaires**
```bash
mkdir -p data/raw_data/clients data/raw_data/products data/processed data/load
```

3. **Supprimer les fichiers compilés Python (optionnel)**
```bash
find . -type f -name "*.pyc" -delete
find . -type d -name "__pycache__" -exec rm -r {} +
```

4. **Exporter le PYTHONPATH**
```bash
export PYTHONPATH=$(pwd)/src
```

5. **Lancer le pipeline ETL complet**
```bash
python main.py
```

6. **Vérifier les fichiers finaux**
- `data/load/clients_final.csv`
- `data/load/products_final.csv`

## ⚠️ Gestion des erreurs

- Fichiers clients vides ou invalides : warning et ignorés.
- Fichiers produits vides ou invalides : erreur affichée.
- Les logs détaillent chaque étape pour faciliter le debug.

## 💡 Auteur

**Alpha Lansar**
Formation Data Engineering
Projet réalisé dans le cadre du TP `ecommerce-analytics`.

