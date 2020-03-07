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
    DB_CONF["db"]="off_base"
    Db.__init__(Db)
    rec_cat=Db.get_infos_category(Db)
    
    assert rec_cat[1][1] == "Yaourts"

def test_get_infos_product():
    rec_prod=Db.get_infos_product(Db, 2)
    for prod in rec_prod:
        assert prod[4]==2

def test_cleaning_product():
    rec_cat=Db.get_infos_category(Db)
    rec_prod=Db.get_infos_product(Db, 3)                        
    view.display_category_product(3, rec_cat, rec_prod)
    for val in rec_prod:
        for col in val:
            assert col != ""

