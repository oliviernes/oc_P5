import pytest
import view
from config import DB_CONF
from models import Db

### Connexion to the db:


def test_connexion1():
    DB_CONF["user"] = "bob"

    with pytest.raises(AssertionError):
        assert (
            Db.__init__(Db)
            == "Something is wrong with your user name\
         or password"
        )


def test_connexion2():
    DB_CONF["user"] = "off_user"
    DB_CONF["db"] = "foobar"

    with pytest.raises(AssertionError):
        assert (
            Db.__init__(Db)
            == "1044 (42000): Access denied for user \
        'off_user'@'localhost' to database 'foobar'"
        )


def test_get_infos_category():
    DB_CONF["db"] = "off_base"
    database = Db()
    rec_cat = database.get_infos_category()

    assert rec_cat[1][1] == "Yaourts"


def test_get_infos_product():
    database = Db()
    rec_prod = database.get_infos_product(2)
    for prod in rec_prod:
        assert prod[6] == 2


def test_cleaning_product():
    database = Db()
    rec_cat = database.get_infos_category()
    rec_prod = [
        (11, "", "b", 387, 2),
        (12, "", "a", 188, 2),
        (13, "", "c", 435, 2),
        (14, "Skyr", "a", 238, 2),
        (15, "", "a", 226, 2),
        (16, "P'tit Yop, Goût Fraise", "b", "", 2),
        (17, "", "c", 393, 2),
        (18, "", "c", 435, "Carrefour", "", 2),
        (19, "Yaourt à la grecque nature", "c", 414, "Auchan", "https://fr-en.openfoodfacts.org/product/7622210601988/yahourt", 2),
        (20, "Gourmand et végétal au lait de coco", "c", 456, "", "https", 2),
    ]
    records_prod = view.display_category_product(3, rec_cat, rec_prod)
    for val in records_prod:
        for col in val:
            assert col != ""


def test_display_products():
    database = Db()
    rec_prod = [
        (31, "Ice Tea saveur Pêche", "d", 82, "Auchan", "https://fr-en.openfoodfacts.org/product/7622210601988/yahourt"),
        (32, "Ice Tea pêche", "d", 82, "Auchan", "https://fr-en.openfoodfacts.org/product/7622210601988/yahourt"),
        (33, "Thé glacé pêche intense", "d", 79, "Auchan", "https://fr-en.openfoodfacts.org/product/7622210601988/yahourt"),
        (34, "Thé infusé glacé, Thé noir parfum pêche blanche", "d", 84, "Auchan", "https://fr-en.openfoodfacts.org/product/7622210601988/yahourt"),
        (35, "Thé vert infusé glacé saveur Menthe", "d", 84, "Auchan", "https://fr-en.openfoodfacts.org/product/7622210601988/yahourt"),
        (36, "Thé noir évasion pêche & saveur hibiscus", "d", 79, "Auchan", "https://fr-en.openfoodfacts.org/product/7622210601988/yahourt"),
        (37, "Thé glacé pêche intense", "d", 79, "Auchan", "https://fr-en.openfoodfacts.org/product/7622210601988/yahourt"),
        (38, "FROSTIES", "d", 1569, "Auchan", "https://fr-en.openfoodfacts.org/product/7622210601988/yahourt"),
        (39, "Sucre glace", "d", 1674, "Auchan", "https://fr-en.openfoodfacts.org/product/7622210601988/yahourt"),
        (40, "fuze tea pêche intense (thé glacé)", "d", 79, "Auchan", "https://fr-en.openfoodfacts.org/product/7622210601988/yahourt"),
    ]
    prod_displayed = view.display_products(38, rec_prod)
    for prod in prod_displayed:
        assert prod[0] != 38
