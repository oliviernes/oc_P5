from mysql.connector import errorcode
import requests

# ~ import pdb
from config import DB_CONF

################
#   DATABASE   #
################


class Db:
    """Manage the database"""

    def __init__(self):

        con_conf = {
            "host": DB_CONF["host"],
            "user": DB_CONF["user"],
            "password": DB_CONF["password"],
        }

        try:
            cnx = mysql.connector.connect(**con_conf)

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            cnx.close()
