#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import view
from models import Db

database = Db()

def check_input(question, records):
	
	select=[]
	
	for elements in records:
		select.append(elements[0])
	
	num = input(question)

	while True:
		try:
			val = int(num)
			if val>0 and val in select:
				break;
			elif val>0 and val not in select:
				num=input("Input must be one of the index displayed.\
	Try again.")
			else:
				num=input("Input must be a positive integer.\
 Try again: ")
		except ValueError:
			try:
				float(num)
				num=input("Input is an float number. You must enter an \
interger number. Please, try again: ")
			except ValueError:
				num=input("This is not a number.\
 Please enter a valid number. Try again: ")
	
	return val
	
def cli():

    view.greeting()

    records_cat = database.get_infos_category()

    view.display_categories(records_cat)

    #~ choice = input("\nChoose the index of one of the categories: ")

    choice=check_input("\nChoose the index of one of the categories: "\
    , records_cat)

    os.system('clear')
		
    records_prod = database.get_infos_product(choice)

    records_prod=view.display_category_product(choice, records_cat, records_prod)

    choice=check_input("\nChoose the index of one of the products: "\
    , records_prod)

    os.system('clear')

    view.display_products(choice, records_prod)

    choice=check_input("\nChoose the index of a product to substitute:"\
    , records_prod)
	
cli()

		
	
