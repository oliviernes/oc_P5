"""view file"""

from models import Db
from colorama import Fore, Style


def greeting():
    """ function to greet app's users"""
    print(
        "Welcome in this app:\n\nThis app help users to look for \
healthier products."
    )


def display_categories(records):
    """display available categories"""

    for row in records:
        print(row[0], ":", row[1])


def display_category_product(pick, records_cat, records_prod):
    """display products of the category chosen"""

    print("\nYou chose the category", records_cat[pick - 1][1], ":\n")

    """Cleaning of the product's list:"""
    records_prod_dirty = []
    for row in records_prod:
        records_prod_dirty.append(row[:4])

    records_prod = [prod for prod in records_prod_dirty if all(prod)]

    for row in records_prod:
        print(row[0], ":", row[1], "(", row[2], ")")

    return records_prod


def display_products(pick, records_prod):

    selected = []

    for idx, val in enumerate(records_prod):
        if val[0] == pick:
            index = idx

    for row in records_prod:
        if row[2] < records_prod[index][2]:
            selected.append(row[0])

    if len(selected) == 0:
        for row in records_prod:
            if row[2] == records_prod[index][2] and row[0] != pick:
                selected.append(row[0])
        print(
            "\nNo healthier product available. However, you can \
choose a product with more or less energy. The list is sorted by \
 energy values in kj per 100g or 100mL. The red values are greater\
 than the energy of the product picked or green if equal\
 or less:\n"
        )
    else:
        print(
            "\nHere is a list of healthier products (sorted by their\
 energy values in kj per 100g or 100mL). The red values are greater\
 than the energy of the product picked or green if equal\
 or less:\n"
        )

    selected_energy = records_prod[index][3]

    """Sort products by their energy"""
    sorted_by_energy = sorted(records_prod, key=lambda tup: tup[3])

    for idx, val in enumerate(sorted_by_energy):
        if val[0] in selected:
            for i in range(4):
                if i < 3:
                    print(val[i], " ", end="")
                else:
                    if val[3] > selected_energy:
                        print(Fore.RED + str(val[3]), " ", end="")
                        print(Style.RESET_ALL)
                    else:
                        print(Fore.GREEN + str(val[3]), " ", end="")
                        print(Style.RESET_ALL)
            print("\n")

    """Remove products not selected:"""
    records_prod = [prod for prod in records_prod if prod[0] in selected]

    return records_prod
