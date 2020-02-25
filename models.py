import pymysql.cursors
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

        self.get_connection()

    def get_connection(self):
               
        con_conf = {
            "host": DB_CONF["host"],
            "user": DB_CONF["user"],
            "password": DB_CONF["password"],
            "autocommit": DB_CONF["autocommit"],
            "database": DB_CONF["db"],
        }

        self.cnx = pymysql.connect(**con_conf)
        
        print ("connect successful!!")
        
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
        with connection:
            cur = connection.cursor()

        print("Creating tables")

        for sql_command in sql_list:
            try:
                cur.execute(sql_command + ";")
                print(sql_command[0:20])
            #~ except mysql.connector.Error as err:
                #~ if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                    #~ print("Table Already exists.")
                       # Duplicate entry
            except pymysql.err.IntegrityError as except_detail:
                response = "0, {}".format(except_detail)
            #~ else:
                #~ print(pymysql.err)

    def input_data(self, db):

        search_param = {"search_terms": ", biscuits,",
                        "search_tag": "categories_tag",
                        "page_size": 10,
                        "json": 1,
                        "page": 1}

        API_URL = 'https://fr-en.openfoodfacts.org/cgi/search.pl?'
        products = []
        # initialize to page 1 of search result
        page = 1
        req = requests.get(
            API_URL,
            params=search_param)
            
        # output of request as a json file
        req_output = req.json()
        # list of product of the output
        products_output = req_output['products']
        # store product classes
        #~ for product in products_output:
        #~ products.append(Product_API(product))

        prod0=products_output[0]

        prod_reduit={}
        cat_stage={}

        prod_reduit['name']=prod0['product_name_fr']
        prod_reduit['nutrition_grades']=prod0['nutrition_grades']
        prod_reduit['energy_100']=prod0['nutriments']['energy_100g']

        cat_stage['name']='biscuits'

        prod_names=[]

        for prod in products_output:
            prod_names.append(prod['product_name_fr'])

        #########################

        sql_list = []
        insert_cat = "INSERT INTO category (`name`) VALUES ('{}');"
        insert_prod = """INSERT INTO product (`name`, `nutrition_grades`, `energy_100`, `category_id`) \
        SELECT "{name}", "{nutrition_grades}", "{energy_100}", id AS category_id \
        FROM category \
        WHERE name = "{cat}";"""

        # insert category
        sql_list.append(insert_cat.format("biscuits",))

        # insert products
        for idx, val in enumerate(req_output['products']):
            sql_list.append(
                insert_prod.format(
                    name=val['product_name_fr'],
                    nutrition_grades=val['nutrition_grades'],
                    energy_100=val['nutriments']['energy_100g'],
                    cat="biscuits",
                )
            )

        #~ db = models.Db()

        connection = db.cnx
        cursor = connection.cursor()

        #~ print(sql_list)

        try:
            for command in sql_list:
                print(command)
                cursor.execute(command)
            #~ cursor.close()
        #~ except mysql.connector.Error as error:
            #~ print(f'Failed to insert record to MySQL table: {error}')
            #~ print(error)
                # For warnings, do not catch "Data truncated…" as expected
        except pymysql.err.Warning as except_detail:
            response = "Warning: «{}»".format(except_detail)
        # Duplicate entry
        except pymysql.err.IntegrityError as except_detail:
            response = "0, {}".format(except_detail)

        except pymysql.err.ProgrammingError as except_detail:
            response = "ProgrammingError: «{}»".format(except_detail)

        except pymysql.err.MySQLError as except_detail:
            response = "MySQLError: «{}»".format(except_detail)

