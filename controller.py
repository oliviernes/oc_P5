#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from models import Db
from view import Display

database = Db()


def substitution(substitutes):

    selection = [(1, 1), (2, 2)]

    if len(substitutes[0]) == 0:
        print("There is no substitutes recorded")
    elif len(substitutes[0]) > 0:
        answer = check_input(
            "\nSome substitutes are available. Do you \
want to visit them?\n\n1:no\n2:yes\n\nYour answer: ",
            selection,
        )
        if answer == 2:
            print("\nHere are your substitutes: ")
            for subs in substitutes[0]:
                for prods in substitutes[1]:
                    if subs[0] == prods[0]:
                        prod_name = prods[1]
                    elif subs[1] == prods[0]:
                        subs_name = prods[1]
                print("\n", prod_name, " can be replaced by ", subs_name)
    print("\nHere are the categories available for screening:\n")


def check_input(question, records):

    select = []

    for elements in records:
        select.append(elements[0])

    num = input(question)

    while True:
        try:
            val = int(num)
            if val > 0 and val in select:
                break
            elif val > 0 and val not in select:
                num = input(
                    "Input must be one of the index displayed.\
 Try again: "
                )
            else:
                num = input(
                    "Input must be a positive integer.\
 Try again: "
                )
        except ValueError:
            try:
                float(num)
                num = input(
                    "Input is a float number. You must enter an \
interger number. Please, try again: "
                )
            except ValueError:
                num = input(
                    "This is not a number.\
 Please enter a valid number. Try again: "
                )

    return val


def cli():

    display = Display()

    display.greeting()

    continu = True

    while continu:

        substitutes = database.get_substitute()

        substitution(substitutes)

        records_cat = database.get_infos_category()

        display.display_categories(records_cat)

        choice = check_input(
            "\nChoose the index of one of the categories:\
 ",
            records_cat,
        )

        os.system("clear")

        records_prod = database.get_infos_product(choice)

        records_prod = display.display_category_product(
            choice, records_cat, records_prod
        )

        choice_prod = check_input(
            "\nChoose the index of one of the products: \
",
            records_prod,
        )

        os.system("clear")

        records_prod = display.display_products(choice_prod, records_prod)

        choice_subs = check_input(
            "\nChoose the index of a product to \
substitute: ",
            records_prod,
        )

        selec = [(1, 1), (2, 2)]
        choice = check_input(
            "\nDo you want to register this substitute in the\
 database?\n\n1:no\n2:yes\n\nYour answer: ",
            selec,
        )

        if choice == 2:
            database.update_data(choice_prod, choice_subs)
        else:
            pass

        choice = check_input(
            "\nDo you want to search other products?\n\n1:no\n2:yes\n\nYour answer: ",
            selec,
        )

        if choice == 1:
            break
        else:
            pass


cli()
