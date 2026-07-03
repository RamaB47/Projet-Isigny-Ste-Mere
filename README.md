# 📊 Analyse prédictive de la collecte laitière & Risques climatiques (Scope 3)
## Cas d'étude : Coopérative Isigny Sainte-Mère

### 🌿 Contexte du Projet
Dans le cadre de la réglementation **CSRD** et des standards **GRI**, le changement climatique représente un enjeu matériel majeur (double matérialité : financière et d'impact) pour le secteur agroalimentaire. 

Ce projet indépendant a pour objectif d'analyser l'impact du dérèglement climatique — et plus particulièrement du stress thermique — sur la production de lait de la **Coopérative Isigny Sainte-Mère**. L'ambition finale est de proposer des recommandations basées sur la donnée pour optimiser la résilience de la **supply chain** et piloter l'impact environnemental (Scope 3).

---

### 🚀 Statut du Projet : En cours
* **Étape 1 : Data Preparation & Nettoyage (Validée ✅)**
* **Étape 2 : Analyse Exploratoire des Données / EDA (Validée ✅)**
* **Étape 3 : Modélisation prédictive avec Prophet (En cours 🛠️)**

---

### 📊 Données utilisées
L'analyse croise plusieurs sources de données publiques et sectorielles :
* **Données sectorielles :** Estimations et indicateurs du **CNIEL** (Centre National Interprofessionnel de l'Économie Laitière).
* **Données climatiques :** Historiques et relevés de stations **Météo-France** (températures, vagues de chaleur, anomalies thermiques).

---

### 🛠️ Focus Technique : Phase de Nettoyage (Data Prep)
Ce répertoire contient pour le moment les notebooks dédiés à la phase critique de préparation des données (le fameux "80% du temps" d'un projet data). 

**Principaux défis techniques relevés sous Python (Pandas) :**
* Filtrage ciblé des fonctionnalités et alignement des structures géographiques (`NOM_USUEL` des stations).
* Gestion des formats temporels complexes : traitement des chaînes de caractères (`string`) et conversion forcée au format standard `datetime` (résolution des anomalies de lignes isolées).
* Garantie de la structure des exports lors des phases de transition (reconstruction des headers de colonnes au format CSV).
* **Industrialisation :** Structuration d'un code robuste et réutilisable, permettant de dupliquer l'intégralité du pipeline de nettoyage sur une seconde station météo en moins de 30 secondes chrono.

---

### 🔮 Prochaines étapes
L'étape suivante consiste à injecter ces données nettoyées dans des modèles de **Machine Learning** (notamment l'algorithme de séries temporelles **Prophet**) afin de modéliser les prévisions de collecte laitière selon différents scénarios climatiques.

---
*Projet personnel mené de bout en bout dans le cadre d'une transition professionnelle vers l'analyse de données ESG et la transformation durable des supply chains.*
