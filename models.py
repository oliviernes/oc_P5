import pymysql.cursors
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

        cnx = pymysql.connect(**con_conf)
        
        print ("connect successful!!")
    
