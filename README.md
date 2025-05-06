# Dashboard Collaboratif de Visualisation et Analyse de Données

## 📌 Description

Ce projet est une application web collaborative conçue pour importer, analyser et visualiser des jeux de données de manière interactive. Elle prend en charge plusieurs utilisateurs avec une gestion de rôles, des fonctions d’audit, et la génération de rapports, simulant un environnement de travail en entreprise.

## 🚀 Fonctionnalités principales

- **Authentification sécurisée** avec gestion de rôles (admin, analyste)
- **Importation de données** via fichiers CSV ou Excel (XLSX)
- **Visualisation dynamique** avec graphiques interactifs et filtres
- **Analyse statistique** incluant corrélation, moyennes, détection d’anomalies
- **Export** de graphiques et rapports PDF
- **Historique des actions** utilisateur et audit complet

## 🛠️ Technologies utilisées

- Backend : API REST avec gestion JWT
- Base de données : PostgreSQL
- Frontend : React.js
- Sécurité : HTTPS, JWT, CORS

## 📂 Structure du projet

- `/api/` : endpoints pour authentification, import, analyse et audit
- `/frontend/` : application web avec tableaux, graphiques et filtres
- `/utils/` : scripts d’analyse statistique, export PDF, etc.

## 🔗 Endpoints API (principaux)

### 🔐 Authentification

- `POST /api/login/` : Authentifie l'utilisateur et retourne un token JWT
- `POST /api/logout/` : Invalide le token de session
- `GET /api/users/` : Liste des utilisateurs (admin uniquement)
- `POST /api/users/` : Crée un nouvel utilisateur
- `PUT /api/users/{id}/` : Modifie un utilisateur
- `DELETE /api/users/{id}/` : Supprime un utilisateur

### 📊 Données

- `POST /api/data/upload/` : Upload de fichiers CSV/XLSX
- `GET /api/data/preview/` : Aperçu des données importées
- `GET /api/data/visualize/` : Retourne les données formatées pour les graphiques

### 📈 Analyse

- `GET /api/analysis/stats/` : Renvoie moyenne, médiane, écart-type
- `GET /api/analysis/correlation/` : Analyse de corrélation entre colonnes
- `GET /api/analysis/anomalies/` : Détection d’anomalies

### 📄 Rapports

- `GET /api/report/pdf/` : Génère un rapport PDF des visualisations
- `GET /api/export/` : Export des données nettoyées

### 🕵️ Audit

- `GET /api/audit/logs/` : Liste des actions des utilisateurs

## ⚙️ Installation

```bash
# Cloner le dépôt
git clone https://github.com/votre-repo/dashboard-analyse.git
cd dashboard-analyse

# Installer les dépendances backend
cd api
pip install -r requirements.txt

# Lancer le serveur
python manage.py runserver

# Installer les dépendances frontend
cd ../frontend
npm install
npm start
```
