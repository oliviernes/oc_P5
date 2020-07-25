
# Context:

The startup Pur Beurre Works is familiar with French eating habits. Their restaurant, Ratatouille, is gaining increasing success and is always attracting more visitors to the hill of Montmartre.

The team noticed that their users wanted to change their diet but were not sure where to start. Replace Nutella with a hazelnut paste, yes, but which one? And in which store to buy it? Their idea is therefore to create a program that would interact with the Open Food Facts database to recover the food, compare it and offer the user a healthier substitute for the food they want.

# Features:

* Fill the database.
* Display categories available.
* Select a category.
* Display products of the selected category.
* Select a product to replace.
* Display substitutes available.
* Select a substitute.
* Display information about the substitute.
* Choose to record or not the substitution in the database.
* Choose to display the recorded substitutes.

# Created with:

* python 3.7.4
* requests 2.22.0
* mysql-connector-python 8.0.19
* MariaDB

# Installation

* get the code: git clone git@github.com:oliviernes/MacGyver.git
* create a dedicated virtualenv: virtualenv -p python3 .venv; source .venv/bin/activate
* adds dependencies: pip install -r requirements.txt

# MariaDB config:

* create a database: CREATE DATABASE nom_base;
* grant privileges: GRANT ALL ON nom_base.* TO 'nom_utilisateur'@'localhost'; FLUSH PRIVILEGES; 
* replace DB_CONF values in config.py to suit your needs.

# Create the tables and fill the database:

* run install.py file: python install.py

# Run the program:

* run controller.py file: python controller.py
