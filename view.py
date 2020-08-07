"""view file"""

import random

from colorama import Fore, Style


class Display:
    "To display informations on the terminal"

    @staticmethod
    def greeting():
        """ function to greet app's users"""
        message = "This app help users to look for healthier products."
        print("Welcome in this app:\n\n" + message)

    @staticmethod
    def display_categories(records):
        """display available categories"""

        for row in records:
            print(row[0], ":", row[1])

    @staticmethod
    def display_category_product(pick, records_cat, records_prod):
        """display products of the category chosen"""

        print("\nYou chose the category", records_cat[pick - 1][1], ":\n")

        sampling = random.choices(records_prod, k=30)

        for row in sampling:
            print(row[0], ":", row[1], "(", row[2], ")")

        return sampling

    @staticmethod
    def display_products(pick, records_prod):
        """Display available substitutes of a product"""
        selected = []

        for idx, val in enumerate(records_prod):
            if val[0] == pick:
                index = idx

        for row in records_prod:
            if row[2] < records_prod[index][2]:
                selected.append(row)

        if len(selected) == 0:
            for row in records_prod:
                if row[2] == records_prod[index][2] and row[0] != pick:
                    selected.append(row)

            print(
                "\nNo healthier product available. However, you can choose "
                "a product with more or less energy. The list is sorted by "
                "energy values in kj per 100g or 100mL. The red values are "
                "greater than the energy of the product picked or green if "
                "equal or less:\n"
            )
        else:
            print(
                "\nHere is a list of healthier products (sorted by their"
                " energy values in kj per 100g or 100mL). The red values"
                " are greater than the energy of the product picked or "
                "green if equal or less:\n"
            )

        selected_energy = records_prod[index][3]

        "Add product's id picked in the selected products' list"
        selected.append(records_prod[index])

        """Sort products by their energy"""
        sorted_by_energy = sorted(selected, key=lambda tup: tup[3])

        """Select 10 products with similar energy and same nutrisocre"""
        for idx, val in enumerate(sorted_by_energy):
            if val[3] == selected_energy:
                mini = idx - 5
                if mini < 0:
                    mini = 0
                sorted_by_energy = sorted_by_energy[mini : idx + 5]
                break

        if records_prod[index] in sorted_by_energy:
            sorted_by_energy.remove(records_prod[index])

        """Display substitutes with the color of their energy according 
        to their value"""
        for idx, val in enumerate(sorted_by_energy):
            for i in range(6):
                if i != 3:
                    print(val[i], " ", end="")
                else:
                    if val[3] > selected_energy:
                        print(Fore.RED + str(val[3]), " ", end="")
                        print(Style.RESET_ALL)
                    else:
                        print(Fore.GREEN + str(val[3]), " ", end="")
                        print(Style.RESET_ALL)
            print("\n")

        return sorted_by_energy
