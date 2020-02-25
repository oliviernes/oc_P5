    #!/usr/bin/env python3
# -*- coding: utf-8 -*-

import mysql.connector
from mysql.connector import errorcode
import requests
import json
# ~ import pdb
from config import DB_CONF

################
#   DATABASE   #
################


class Db:
    """Manage the database"""

    def __init__(self):
        """
        Connect to MySQL Server
        :Tests:
        >>> DB_CONF["user"] = 'bob'
        >>> Db.__init__(Db)
        Something is wrong with your user name or password
        >>> DB_CONF['user'] = 'off_user'
        >>> DB_CONF['db'] = 'foobar'
        >>> Db.__init__(Db)
        1044 (42000): Access denied for user 'off_user'@'localhost' to database 'foobar'
        """


        con_conf = {
            "host": DB_CONF["host"],
            "user": DB_CONF["user"],
            "password": DB_CONF["password"],
            "database": DB_CONF["db"],
            "autocommit": DB_CONF["autocommit"],
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
                print(sql_command + ";")
                cursor.execute(sql_command + ";")       
            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                    print("Table already exists.")
                else:
                    print(err.msg)
            else:
                print("OK")
        
        #~ cursor.close()
    

    def input_data(self, db):

        search_param = {
            "search_terms": ", biscuits,",
            "search_tag": "categories_tag",
            "page_size": 10,
            "json": 1,
            "page": 1,
        }

        API_URL = "https://fr-en.openfoodfacts.org/cgi/search.pl?"
        products = []
        # initialize to page 1 of search result
        page = 1
        req = requests.get(API_URL, params=search_param)

        # output of request as a json file
        req_output = req.json()
        # list of product of the output
        products_output = req_output["products"]
        # store product classes
        # ~ for product in products_output:
        # ~ products.append(Product_API(product))

        prod0 = products_output[0]

        prod_reduit = {}
        cat_stage = {}

        prod_reduit["name"] = prod0["product_name_fr"]
        prod_reduit["nutrition_grades"] = prod0["nutrition_grades"]
        prod_reduit["energy_100"] = prod0["nutriments"]["energy_100g"]

        cat_stage["name"] = "biscuits"

        prod_names = []

        for prod in products_output:
            prod_names.append(prod["product_name_fr"])

        #########################

        sql_list = []
        insert_cat = """INSERT INTO category (`name`) VALUES ('{}');"""
        insert_prod = """INSERT INTO product (`name`, `nutrition_grades`, `energy_100`, `category_id`) \
        SELECT "{name}", "{nutrition_grades}", "{energy_100}", id AS category_id \
        FROM category \
        WHERE name = "{cat}";"""

        # insert category
        sql_list.append(insert_cat.format("biscuits",))

        # insert products
        for idx, val in enumerate(req_output["products"]):
            sql_list.append(
                insert_prod.format(
                    name=val["product_name_fr"],
                    nutrition_grades=val["nutrition_grades"],
                    energy_100=val["nutriments"]["energy_100g"],
                    cat="biscuits",
                )
            )

        # ~ db = models.Db()

        connection = db.cnx
        cursor = connection.cursor()

        # ~ print(sql_list)

        try:
            for command in sql_list:
                print(command)
                cursor.execute(command)
            cursor.close()
        except mysql.connector.Error as error:
            print(f"Failed to insert record to MySQL table: {error}")
            print(error)
