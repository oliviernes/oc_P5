import mysql.connector
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
            "database": DB_CONF["db"],
        }

        try:
            self.cnx = mysql.connector.connect(**con_conf)

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        else:
            pass

    def make_sql_list(self, sql_file=DB_CONF["file"]):
        """Make a list of sql commands"""

        with open(sql_file, "r") as file:
            # Split file in list
            ret = file.read().split(";")
            # drop last empty entry
            ret.pop()
            return ret

    def create_tables(self):
        """Initialize the database"""

        sql_list = self.make_sql_list()

        # ~ Open cursor linked to DB (self)
        connection = self.cnx
        cursor = connection.cursor()
                
        length=len(sql_list)
        n=0
        
        for sql_command in sql_list:
            n+=1    
            try:
                table=""
                for letter in sql_command[13:]:
                     table+=letter
                     if table[-2:]==" (":
                          table=table[:-2]
                          break
                if n<length:
                     print(f'Creating table:{table} -', end='')
                cursor.execute(sql_command + ";")       
            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                    print("Table already exists.")
                else:
                    print(err.msg)
            else:
                print("OK")
