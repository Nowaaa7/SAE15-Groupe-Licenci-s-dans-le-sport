# SAE 15 : Traitement et Visualisation de Données (Clubs Sportifs)

## Équipe du projet
* **Noa Jodry** : Responsable technique (GitLab) & Extraction des données (Extract).
* **Mark Sukhoverkhov** : Responsable du code Python & visualisation ASCII.
* **Galilee Mugenzi Kayumba** : Responsable de la visualisation & Présentation (Load).

---

## Description du projet
Ce script a pour but d'automatiser la récupération et l'analyse de données publiques provenant de *data.gouv.fr*.

**Sujet choisi :** Licenciés dans le sport
**Objectif :** Nous récupérons le fichier CSV, calculons, et générons un graphique via l'API QuickChart.

---

## Pré-requis techniques
Pour faire fonctionner ce projet, vous avez besoin de :
* Python 3 installé.
* Les bibliothèques Python suivantes :
    * `pandas`
    * `requests`
    * `os`
    * `json`

---

## Installation et Lancement

1. **Cloner et lancer le projet**
   ```bash
   git clone https://gitlab.univ-artois.fr/noa_jodry/sae15-groupe-licencies-dans-le-sport.git
   cd sae15-groupe-licencies-dans-le-sport/src
   ./make_chart [-h] [-l [LINK]] [-n [NUMBER]] [-a [ASCII]] [-q [QUICKCHART]] [-o [OPEN_QUICKCHART]]
   
