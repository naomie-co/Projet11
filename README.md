# Projet_11

## Le projet
La plateforme Pur Beurre permet de recommander des produits qui possèdent un nutriscore élevé au sein d’un catégorie de produits, à partir de l’API d’OpenFoodFacts. Les magasins qui vendent les produits en France métropolitaine sont affichés sur une carte, dans la page de détail des produits. 

## Le parcours utilisateur 
Les recherches peuvent être lancées à partir de la page d’accueil ou à partir de toutes les pages du site, via la barre de navigation. 

Lorsqu’une recherche de produits est lancée, l’utilisateur arrive sur une page de résultats qui propose les 6 produits ayant le nutriscore le plus élevé dans leur catégorie. 

Dans la page de résultats, l’utilisateur peut :
-	consulter la page de détail d’un produit dans laquelle il peut visualiser les lieux de vente du produit,
-	sauvegarder un produit s’il est déjà connecté à son espace personnel, 
-	se connecter à son espace personnel. S’il clique sur le lien, il peut :
o	se connecter à son espace personnel,
o	cliquer sur le lien de création de compte et créer son compte.

L’utilisateur peut consulter ses produits sauvegardés en cliquant sur l’icône « carotte ». 

## Si vous souhaitez installer la plateforme en local :

### 1 – Création de l’environnement virtuel
Cloner ce repo 

Ce programme est exécuté en Python et utilise le Framework Django.

Pour l’exécuter, il est recommandé de créer au préalable, un environnement virtuel. 

Une fois l’environnement virtuel créé, lancez l’installation des dépendances avec la commande :

	pip install -r requirements.txt

### 2 – Créer la base de données PostgreSQL 

Le programme est lié à une base de données PostgreSQL.

Vous pouvez installer PostgreSQL en suivant les instructions disponibles à l’adresse suivante : https://www.postgresql.org/download/

Une fois l’installation terminée, créez une base de données avec la commande suivante :

	createdb -O yourusername plateforme

La base de données doit également être déclarée dans le projet Django. Pour lancer le projet en mode dévelopement, configurez une variable d'environnement (ENV=DEV) ainsi qu'une secret key (S_KEY="votre secret key"). Pour lancer la déclaration de la base de données, modifiez le dossier settings/developement.py avec les informations suivantes :

	DATABASES = {
	    'default': {
	        'ENGINE': 'django.db.backends.postgresql',
	        'NAME': 'plateforme',
	        'USER': 'Yourusername',
	        'PASSWORD': YOUPASSWORD, 
	        'HOST': '',
	        'PORT': '5432',
	    }
	}
### 3 – Lancer l’initialisation de la base de données

Pour installer la base de données lancez la commande suivante :

	plateforme_project\manage.py migrate

	plateforme_project\manage.py init_db

### 4 – Lancer le serveur 
Pour accéder à la plateforme, lancez le serveur PostgreSQL puis le serveur Django avec la commande suivante :

	plateforme_project\manage.py runserver

Lancez l’adresse donnée par le serveur dans un navigateur :

### Vérification PEP 8 et informations sur les tests
Si vous souhaitez lancer les vérifications de conformité à la PEP 8 sans les erreurs liées à Django :

-	Installez dans l’environnement virtuel :

		pip install pylint-Django

-	Lancez la commande 

		pylint test file.py --load-plugins pylint_Django

Le fichier de tests de l’application search comprend des tests fonctionnels qui utilisent Sélénium. 

Pour installer Sélénium dans le projet, exécutez la fonction suivante : 

	pip install selenium

Installez le driver correspondant au navigateur Firefox (https://github.com/mozilla/geckodriver/releases). 

Remplacez le lien vers geckodriver dans le fichier de tests par le vôtre.


## Lien vers le site
Si vous souhaitez tester le plateforme Pur Beurre, cliquez sur ce lien :
	[https://plateforme-project.herokuapp.com/]
