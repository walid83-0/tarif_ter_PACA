# Importation des librairies nécessaires
import pandas as pd  # Pour la manipulation des données
import plotly.express as px  # Pour la visualisation graphique
import plotly.io as pio  # Pour la configuration des rendus graphiques

# Configuration de l'affichage des graphiques dans le navigateur web
pio.renderers.default = 'browser'

# Chargement des données depuis un fichier CSV avec le séparateur point-virgule
df = pd.read_csv("tarifs-ter-paca.csv", sep=';')

# Filtrage pour ne garder que les tarifs normaux
df_normal = df[df["Type tarif"] == "Tarif normal"]

# Calcul du prix moyen par gare d'origine, avec arrondi à 2 décimales
prix_moyen_par_gare_origine = (
    df_normal.groupby("Origine")["Prix"]  # Groupement par gare d'origine
    .mean()  # Calcul de la moyenne
    .round(2)  # Arrondi à 2 décimales
    .reset_index()  # Réinitialisation de l'index pour avoir un DataFrame standard
    .sort_values(by="Prix", ascending=False)  # Tri décroissant par prix
)

# Création d'un graphique en barres avec Plotly Express
fig = px.bar(
    prix_moyen_par_gare_origine,  # DataFrame source
    x="Origine",  # Axe X: noms des gares
    y="Prix",  # Axe Y: prix moyens
    title="Prix moyen des billets TER par gare de départ - Tarif normal",  # Titre
    labels={"Origine": "Gare d'origine", "Prix": "Prix moyen (€)"},  # Labels des axes
    color="Prix",  # Couleur des barres basée sur le prix
    color_continuous_scale='Oranges',  # Échelle de couleur orange
    text="Prix"  # Affichage des valeurs sur les barres
)

# Personnalisation de la mise en page
fig.update_layout(
    xaxis_tickangle=90,  # Rotation des étiquettes de l'axe X à 90°
    uniformtext_minsize=8,  # Taille minimale du texte affiché
    uniformtext_mode='hide'  # Masquage du texte si trop long pour éviter le chevauchement
)

# Formatage des valeurs affichées sur les barres
fig.update_traces(
    texttemplate='%{text:.2f}€',  # Formatage à 2 décimales avec le symbole €
    textposition='outside'  # Positionnement du texte à l'extérieur des barres
)

# Affichage du graphique dans le navigateur
fig.show()

# Sauvegarde du graphique au format HTML pour partage
fig.write_html("graphique_prix_moyen.html")