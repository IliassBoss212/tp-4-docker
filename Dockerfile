# Utilise une image officielle de Python
FROM python:3.11-slim

# Crée un dossier pour l'application
WORKDIR /app

# Copie les fichiers nécessaires
COPY simple_math.py .
COPY test_simple_math.py .

# Installe les dépendances
RUN pip install --upgrade pip && pip install pylint

# Commande exécutée au lancement du conteneur : lancer les tests
CMD ["python", "-m", "unittest", "discover"]
