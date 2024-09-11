# Diagnostic du Cancer du Sein par Apprentissage Profond

Ce projet utilise des techniques d'apprentissage profond, en particulier des réseaux de neurones convolutifs (CNN) et des machines à vecteurs de support (SVM), pour le diagnostic du cancer du sein à partir d'images histopathologiques. Le projet se concentre sur l'utilisation de la base de données BreakHis.

## Structure du Projet

- `code/` : Contient les scripts Python pour l'apprentissage des modèles. Chaque script correspond à un modèle entraîné sur des images avec un zoom optique spécifique (40X, 100X, 200X, 400X).
  
- `dataset/` : Ce dossier contient les données d'entraînement et de test issues de la base de données BreakHis. Les images sont classées en fonction du niveau de zoom (40X, 100X, 200X, 400X) et sont réparties en deux catégories : bénignes et malignes.

- `interface_graphique/` : Contient le code pour l'interface graphique permettant aux utilisateurs de tester de nouvelles images histopathologiques. Cette interface comprend :
  - Une page d'authentification.
  - Une page d'inscription.
  - Une page de test pour soumettre une image et obtenir une classification.

## Détails sur la Base de Données

La base de données utilisée est [BreakHis](https://www.kaggle.com/datasets/ambarish/breakhis?select=BreaKHis_v), qui contient des images microscopiques de biopsies de tumeurs mammaires, tant bénignes que malignes. Voici quelques caractéristiques des données :

- **Dimensions des images** : 700 x 460 pixels, RGB, 24 bits.
- **Grossissements optiques** : 40X, 100X, 200X, 400X.

### Distribution des Données

**Zoom optique 400X**:
- Apprentissage : 371 bénignes, 777 malignes
- Test : 176 bénignes, 369 malignes

**Zoom optique 200X**:
- Apprentissage : 353 bénignes, 901 malignes
- Test : 192 bénignes, 477 malignes

**Zoom optique 100X**:
- Apprentissage : 383 bénignes, 943 malignes
- Test : 261 bénignes, 477 malignes

**Zoom optique 40X**:
- Apprentissage : 370 bénignes, 835 malignes
- Test : 255 bénignes, 535 malignes

## Fonctionnalités

- **Classification** : Les modèles CNN-SVM et CNN-MLP permettent de classer les images en tumeurs bénignes ou malignes.
- **Interface Graphique** : L'utilisateur peut tester de nouvelles images via une interface simple et intuitive.

## Installation et Exécution

1. Cloner le dépôt :
   ```bash
   git clone https://github.com/Chaymahadded/D-tection-du-cancer-du-sein-par-deep-learning.git
