import pytest
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
