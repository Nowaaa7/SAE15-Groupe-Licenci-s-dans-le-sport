# Portfolio Individuel - SAE 15

**Étudiant :** Noa Jodry
**Groupe :** A2
**Rôle :** Responsable Technique (GitLab) & Extraction des données (Extract)
**Projet :** Analyse des Clubs Sportifs en France (ETL)

---

## 1. Introduction et Contexte
Dans le cadre de la SAE 15, notre équipe (composée de Mark Sukhoverkhov, Galilee Mugenzi Kayumba et moi-même) a dû réaliser un script d'automatisation de traitement de données.

Mon rôle spécifique au sein du groupe était celui de **l'Architecte des Données**. J'étais responsable de :
1. La mise en place de l'environnement de travail collaboratif (GitLab).
2. L'étape "Extract" du pipeline ETL : récupérer automatiquement le fichier CSV depuis le serveur du gouvernement (data.gouv.fr) via Python.

---

## 2. Bilan des Compétences Acquises

Durant ce projet, j'ai développé des compétences techniques précises :

### Gestion de version (Git & GitLab)
* **Initialisation de dépôt :** J'ai créé le projet, configuré la visibilité et géré les invitations des membres et de l'enseignant.
* **Gestion des conflits :** J'ai appris à gérer les fichiers `.gitignore` pour éviter de polluer le serveur avec des fichiers temporaires Python (`__pycache__`).
* **Bonnes pratiques :** J'ai veillé à ce que l'arborescence (`src/`, `data/`, `doc/`) soit respectée par l'équipe.

### Programmation Python (Module Requests)
* Utilisation de la bibliothèque `requests` pour effectuer des requêtes HTTP (GET).
* Gestion des codes de retour HTTP (vérifier si `status_code == 200` avant de lancer la suite du script).
* Manipulation de flux de données brutes avec `io.StringIO` pour passer le contenu téléchargé directement à Pandas sans passer par un fichier temporaire sur le disque dur.

---

## 3. Journal de Bord (Suivi Hebdomadaire)

### Semaines 1-2 : Démarrage et Configuration
* **Tâches réalisées :**
    * Création du projet sur le GitLab de l'Université d'Artois.
    * Création de la structure des dossiers et du premier `README.md`.
    * Recherche du jeu de données : nous avons validé le fichier `clubs-data-2023.csv` car il contenait les colonnes nécessaires (Fédérations, Régions, Nombre de clubs).
* **Défi technique :** Comprendre comment inviter l'enseignant avec les bons droits sur GitLab.

### Semaines 3-4 : Développement de l'Extraction (Mon cœur de métier)
* **Tâches réalisées :**
    * Développement du script `download_data.py` (intégré ensuite dans le `main.py`).
    * Test de connexion avec l'URL de data.gouv.fr.
    * Lecture du CSV avec Pandas.
* **Problème majeur résolu :** Le fichier CSV utilisait des points-virgules (`;`) comme séparateur et non des virgules. Au début, Pandas ne voyait qu'une seule colonne. J'ai corrigé cela en ajoutant le paramètre `sep=';'` dans la fonction de lecture.

### Semaines 5-6 : Intégration et Fusion
* **Tâches réalisées :**
    * Collaboration avec Mark (qui s'occupait des calculs) pour relier mon module de téléchargement à son module de traitement.
    * Vérification que le script fonctionne sur une machine vierge (sans le fichier CSV pré-téléchargé).
    * Mise à jour du `README.md` avec les instructions d'installation (`pip install requests pandas`).

### Semaines 7-8 : Finalisation
* **Tâches réalisées :**
    * Nettoyage du code final.
    * Préparation de la partie "Architecture Technique" pour la présentation orale.
    * Vérification finale du dépôt GitLab avant l'évaluation.

---

## 4. Focus : Difficultés et Solutions

| Difficulté Rencontrée | Solution Apportée |
| :--- | :--- |
| **Erreur de lecture CSV** | Le fichier ne s'ouvrait pas correctement. J'ai inspecté le fichier brut avec un éditeur de texte, j'ai vu les `;` et j'ai adapté le code Python (`read_csv(..., sep=';')`). |
| **Organisation Git** | Au début, nous avions peur d'écraser notre travail. J'ai imposé une règle : chacun travaille sur des parties différentes du code avant de tout réunir à la fin. |
| **Gestion des erreurs Web** | Si Internet coupe, le script plante. J'ai ajouté une condition `if response.status_code == 200` pour afficher un message d'erreur propre au lieu de faire crasher le programme. |

---

## 5. Conclusion
Ce projet m'a permis de comprendre l'importance de l'étape "Extraction" dans un projet de Data Science. Si les données sont mal récupérées au début, tout le reste du projet (calculs et graphiques) ne peut pas fonctionner.
Je suis particulièrement satisfait d'avoir réussi à automatiser le téléchargement, ce qui rend notre script autonome et durable.