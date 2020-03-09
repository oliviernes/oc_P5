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
        assert prod[4] == 2

def test_cleaning_product():
    database = Db()
    rec_cat = database.get_infos_category()
    rec_prod = [(11, '', 'b', 387, 2), (12, '', 'a', 188, 2), \
(13, '', 'c', 435, 2), (14, 'Skyr', 'a', 238, 2), (15, '', 'a', 226, 2)\
, (16, "P'tit Yop, Goût Fraise", 'b', '', 2), (17, '', 'c', 393, 2), \
(18, '', 'c', 435, 2), (19, 'Yaourt à la grecque nature', 'c', 414, 2),\
 (20, 'Gourmand et végétal au lait de coco', 'c', '', 2)]
    records_prod=view.display_category_product(3, rec_cat, rec_prod)
    for val in records_prod:
        for col in val:
            assert col != ""

