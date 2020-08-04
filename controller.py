#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from models import Db, ProductsCleaned
from view import Display


class Control:
    """To control user's inputs and display recorded substitutes"""

    def __init__(self):

        self.selection = [(1, 1), (2, 2)]

    def substitution(self, substitutes):

        if len(substitutes[0]) == 0:
            print("There is no substitutes recorded")
        elif len(substitutes[0]) > 0:
            answer = self.check_input(
                "\nSome substitutes are available. Do you \
want to visit them?\n\n1:no\n2:yes\n\nYour answer: ",
                self.selection,
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

    def check_input(self, question, records):

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


class Command:
    """Allows to follow user's path"""

    def __init__(self):

        self.database = Db()
        self.control = Control()

    def cli(self):

        Display.greeting()

        continu = True

        while continu:

            substitutes = self.database.get_substitute()

            self.control.substitution(substitutes)

            records_cat = self.database.get_infos_category()

            Display.display_categories(records_cat)

            choice = self.control.check_input(
                "\nChoose the index of one of the categories:", records_cat,
            )

            records_prod = self.database.get_infos_product(choice)

            records_prod_cleaned = ProductsCleaned().clean(records_prod)

            sampling = Display.display_category_product(
                choice, records_cat, records_prod_cleaned
            )

            choice_prod = self.control.check_input(
                "\nChoose the index of one of the products:", sampling,
            )

            records_prod = Display.display_products(choice_prod, records_prod_cleaned)

            choice_subs = self.control.check_input(
                "\nChoose the index of a product to \
substitute: ",
                records_prod,
            )

            selec = [(1, 1), (2, 2)]
            choice = self.control.check_input(
                "\nDo you want to register this substitute in the\
 database?\n\n1:no\n2:yes\n\nYour answer: ",
                selec,
            )

            if choice == 2:
                self.database.update_data(choice_prod, choice_subs)
            else:
                pass

            choice = self.control.check_input(
                "\nDo you want to search other products?\n\n1:no\n2:yes\n\n\
Your answer: ",
                selec,
            )

            if choice == 1:
                break


command = Command()

if __name__ == "__main__":
    command.cli()
