#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import view
from models import Db

database = Db()


def cli():

    view.greeting()

    breakpoint()

    records_cat = database.get_infos_category()

    view.display_categories(records_cat)

    choice = input("\nChoose the index of one of the categories: ")

    records_prod = database.get_infos_product(choice)

    view.display_category_product(choice, records_cat, records_prod)

    choice = input("\nChoose the index of one of the products: ")

    view.display_products(choice, records_prod)


cli()
