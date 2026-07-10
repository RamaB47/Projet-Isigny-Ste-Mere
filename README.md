📊 Modélisation Prédictive & Impact Climatique : Supply Chain Isigny Sainte-Mère

📌 Présentation du Projet
Ce projet a pour objectif d'analyser, de modéliser et de prévoir les volumes de collecte et de production d'Isigny Sainte-Mère face aux enjeux du dérèglement climatique. En combinant des techniques avancées de Data Science et une approche RSE, ce travail met en lumière l'impact direct des variables environnementales (stress thermique, instabilité climatique post-2022) sur l'amont agricole afin d'apporter des solutions de pilotage stratégiques pour la Supply Chain.

🛠️ Stack Technique & Compétences Déployées
Langage & Analyse de Données : Python (Pandas, NumPy) – Nettoyage rigoureux, gestion des types de données brutes (AAAAMM), traitement des valeurs manquantes.

Modélisation Prédictive & Séries Temporelles : Prophet (Meta) & Régression Linéaire Multiple (Scikit-Learn).

Dataviz & Business Intelligence : Matplotlib, Seaborn, et conception d'un Dashboard interactif Power BI.

Contrôle de Version : Git & GitHub.

📈 Démarche Scientifique & Résultats
1. Modélisation de la Saisonnalité (Baseline)
Une première modélisation de la saisonnalité historique de la collecte a été réalisée, validant la forte régularité des cycles laitiers traditionnels (pic de lactation printanier).

Fiabilité du modèle : R 
2
 =0,92

2. Intégration du Facteur Climatique (Régression Multiple & Prophet)
Pour mesurer l'impact réel du dérèglement climatique, les données de Températures Moyennes (TM) et de Pluviométrie (RR) ont été intégrées comme régresseurs externes.

Fiabilité du modèle étendu : R 
2
 =0,85

Corrélation Climat / Production : Le modèle isole un coefficient d'impact significatif négatif lors des anomalies de chaleur estivale, confirmant l'effet du stress thermique immédiat sur le cheptel.

3. Analyse des Phénomènes Récents (Post-2022)
L'analyse approfondie via prophet.plot_components met en évidence une rupture comportementale à partir de 2022 :

Accentuation marquée des extrêmes (pics plus hauts, creux plus profonds).

Essoufflement des modèles de prévision historiques linéaires face à l'instabilité climatique contemporaine en Normandie.

4. Confrontation des Variables (Température VS Pluviométrie)
L'intégration conjointe de la pluie (RR) et de la température (TM) dans Prophet a démontré des courbes de prédiction quasi-identiques au modèle basé sur la température seule.

Conclusion Métier : La température est le signal dominant et immédiat (stress thermique direct sur l'animal à court terme), tandis que la pluviométrie agit sur un temps plus long (pousse de l'herbe).

💻 Structure du Dépôt GitHub
Plaintext
├── data/                  # Données historiques (Production, Météo)
├── notebooks/             # Notebooks Jupyter d'exploration et de test
├── src/
│   ├── data_cleaning.py   # Script de parsing des dates et typage automatique
│   └── forecasting.py     # Script d'entraînement et d'extraction des coefficients Prophet
├── dashboard/             # Fichier .pbix (Rapport Power BI)
└── README.md              # Présentation du projet

🚀 Prochaines Étapes & Perspectives
🔹 Business Intelligence (En cours)
Déploiement d'un Dashboard Power BI à destination des décideurs Supply Chain et RSE pour :

Visualiser l'historique réel vs les prédictions de Prophet (avec tunnels de confiance).

Suivre les indicateurs clés de performance (KPIs) de stabilité de la collecte.

Simuler des scénarios prospectifs d'anomalies thermiques.

🔹 Prospective RSE & Comptabilité Carbone (Juillet 2026)
Dans le cadre d'une formation spécialisée avec Carbone 4 (Comptabilité Carbone) et des standards GRI / ESRS (CSRD) :

Traduction des scénarios de baisse ou de hausse de collecte en impacts carbone (tCO₂e) sur le Scope 3 (Amont agricole).

Modélisation de trajectoires de réduction adaptatives pour les éleveurs partenaires (agroforesterie, adaptation des rations).

Projet réalisé de bout en bout, de l'extraction de la donnée brute à la modélisation prédictive et sa restitution business.
