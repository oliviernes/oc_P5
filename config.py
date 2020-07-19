# DATABASE
DB_CONF = {
    "host": "localhost",
    "user": "off_user",
    "password": "XXX",
    "db": "off_base",
    "autocommit": True,
    "file": "open_food_db.sql",
}

# API
CATEGORIES = [
    "Biscuits",
    "Yaourts",
    "Pâtisseries",
    "Glaces",
    "Tartes",
]

API_URL = "https://fr-en.openfoodfacts.org/cgi/search.pl?"

INSERT_CAT = "INSERT INTO category (`name`) VALUES ('{}');"

INSERT_PROD = """INSERT INTO product (`name`, \
`nutrition_grades`, `energy_100`, `stores`, `url`, \
`category_id`) SELECT "{name}", "{nutrition_grades}", \
"{energy_100}", "{stores}", "{url}", id AS category_id \
FROM category WHERE name = "{cat}";"""
