# Analyse des tarifs TER en région Sud Provence-Alpes-Côte d'Azur

## 🎯 Objectif

Ce projet vise à analyser les **prix moyens des billets TER** en fonction des **gares de départ** dans la région **Sud Provence-Alpes-Côte d’Azur**, à partir de données ouvertes de la SNCF.

## 💻 Technologies utilisées

- Python 3.13
- Pandas
- Plotly
- Jupyter Notebook / Script Python

## 📊 Question 

> Quel est le **prix moyen** d’un billet **TER** par **gare de départ** en région PACA, en ne considérant que les **tarifs normaux** ?

## 📁 Contenu du repository
.
│ └── tarifs-ter-paca.csv # Jeu de données nettoyé
│ └── analyse_prix_ter.py # Script d'analyse et visualisation 
│ ├── graphique_prix_moyen.html # Version interactive [la télécharger et l'exécuter]
│ └── graphique_prix_ter.png # Export statique
└── README.md # Ce ficher 

## 📁 Données

Les données utilisées proviennent du portail Open Data SNCF(https://data.sncf.com/explore/dataset/tarifs-ter-paca/table/?sort=origine) 
après nettoyage elles comprennent les colonnes suivantes :
- **Origine** : gare de départ
- **Libellé tarif**
- **Type tarif**
- **Prix**

> 🔎 Seuls les trajets dont le **type de tarif** est **"Tarif normal"** ont été conservés pour cette analyse.

## 🧪 Méthodologie

1.J'ai aprés l'avoir télécharger nettoyer le fichier CSV garder les données les plus importantes: Origine| Type tarif| Prix

2. Filtrage sur les lignes où `Type tarif == "Tarif normal"`
3. Groupement par `Origine`
4. Calcul du **prix moyen** pour chaque gare de départ
5. Visualisation interactive avec **Plotly**

## 📌 Résultats principaux

L’analyse met en évidence des écarts significatifs de prix moyen selon les gares de départ. Certaines gares présentent des tarifs moyens autour de **5 €**, tandis que d’autres dépassent les **20 €**.

Ainsi parmi les cas les plus marquants, la gare de **Briançon** affiche un prix moyen de **29,81 €**, la plaçant parmi les plus chères de la région.

Je pense que cette spécificité s’explique par sa situation géographique : gare de montagne enclavée, terminus de ligne, avec des trajets longs vers les grandes villes régionales, souvent facturés entre **40 et 60 €**.

À l’inverse, certaines gares comme **La Pomme** présentent un prix moyen très bas (**3,90 €**) , parce qu’elles sont **rattachées à une seule ou peux de liaison** (ici  par exemple seulement vers **Marseille**) et que c'est des trajets courts . Cela montre que la diversité des destinations et des distances est un facteur structurant dans la variation des prix moyens.






