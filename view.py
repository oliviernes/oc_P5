"""view file"""

from models import Db

def greeting():
    """ function to greet app's users"""
    print("Welcome in this app:\n\nThis app help users to look for \
healthier products.")
    print("\nHere are the categories available for screening:\n")

def display_categories(records):
    """display available categories"""
    
    for row in records:
        print( row[0], ":", row[1])

def display_category_product(pick, records_cat, records_prod):
    """display products of the category chosen"""
    
    print("\nYou chose the category", \
	records_cat[int(pick)-1][1], ":\n")

    for idx, val in enumerate(records_prod):
        """if sentences to display only products with full data"""
        if "" in val:
            del records_prod[idx]

    for row in records_prod:
        print( row[0], ":", row[1], "(",row[2],")")

def display_products(pick, records_prod):
   	
    selected=[]
	
    for idx, val in enumerate(records_prod):
        if val[0]==int(pick):
            index=idx
		
    for row in records_prod:
        if row[2]<records_prod[index][2]:
            selected.append(row[0])
	
    if len(selected)==0:
        for row in records_prod:
            if row[2]==records_prod[index][2]:
                selected.append(row[0])
        print("\nNo healthier product available. However, you can \
choose a product with more or less energy:\n")
    else:
        print("\nHere is a list of healthier products (sorted by their\
 energy value in kj per 100g or 100mL:\n")

    sorted_by_nrj=sorted(records_prod, key=lambda tup: tup[3])

    for idx, val in enumerate(sorted_by_nrj):
        if val[0] in selected:
            for i in range(4):
                print(val[i], " ", end="")
            print("\n")

