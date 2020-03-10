#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import mysql.connector
from mysql.connector import errorcode
import requests
import json
from config import DB_CONF, API_URL

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
        1044 (42000): Access denied for user 'off_user'@'localhost' to \
database 'foobar'
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

        length = len(sql_list)
        n = 0

        for sql_command in sql_list:
            n += 1
            try:
                table = ""
                for letter in sql_command[13:]:
                    table += letter
                    if table[-2:] == " (":
                        table = table[:-2]
                        break
                if n < length-1:
                    print(f"Creating table:{table} -", end="")

                cursor.execute(sql_command + ";")
            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                    print("Table already exists.")
                else:
                    print(err.msg)
            else:
                if n < length-1:
                    print("OK")

    def update_data(self, product, substitute):
        
        connection = self.cnx
        cursor = connection.cursor()
        query= f"UPDATE product SET substitute_id={substitute}\
 WHERE id={product};"
        cursor.execute(query)
        connection.commit()
        cursor.close()
        
    def drop_table(self, table):
        """ DROP TABLE Products"""

        connection = self.cnx
        cursor = connection.cursor()
        query = f"DROP TABLE IF EXISTS {table};"
        cursor.execute(query)
        connection.commit()
        cursor.close()

    def get_infos_category(self):
        """ Get infos from the category table """

        sql_select_Query = "select * from category"
        connection = self.cnx
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        self.records_cat = cursor.fetchall()
        return self.records_cat

    def get_infos_product(self, choice):
        """ Get infos from the category table """

        sql_select_Query = f"select * from product where category_id=\
        {choice}"
        connection = self.cnx
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)
        self.records_prod = cursor.fetchall()
        return self.records_prod


###########################
#       Category          #
###########################


class Category:
    """ Class generating a category"""

    def __init__(self, cat_name):
        self.name = cat_name

    def parameters(self, page):

        search_param = {
            "search_terms": self.name,
            "search_tag": "categories_tag",
            "sort_by": "unique_scans_n",
            "page_size": 10,
            "json": 1,
            "page": page,
        }

        return search_param

    def input_data(self, db):

        # initialize to page 1 of search result
        page = 1
        req = requests.get(API_URL, params=self.parameters(page))

        # output of request as a json file
        req_output = req.json()
        # list of product of the output
        products_output = req_output["products"]

        sql_list = []
        insert_cat = "INSERT INTO category (`name`) VALUES ('{}');"
        insert_prod = """INSERT INTO product (`name`, \
        `nutrition_grades`, `energy_100`, `category_id`) \
        SELECT "{name}", "{nutrition_grades}", "{energy_100}", \
        id AS category_id FROM category WHERE name = "{cat}";"""

        params = self.parameters(page)

        # insert category
        sql_list.append(insert_cat.format(params["search_terms"]))

        # insert products

        for prod in req_output["products"]:
            sql_list.append(
                insert_prod.format(
                    name=prod.get("product_name_fr", ""),
                    nutrition_grades=prod.get("nutrition_grades", ""),
                    energy_100=prod["nutriments"]["energy_100g"],
                    cat=params["search_terms"],
                )
            )

        connection = db.cnx
        cursor = connection.cursor()

        try:
            for command in sql_list:
                # ~ print(command)
                cursor.execute(command)
            cursor.close()
        except mysql.connector.Error as error:
            print(f"Failed to insert record to MySQL table: {error}")
            print(error)
