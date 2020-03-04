#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from models import Db

database = Db()

def cli():

	print("categories available for screening:\n")

	database.get_infos_category()

	for row in database.records:
		print( row[0], ":", row[1])
	
	choice=input("\nChoose the index of one of the categories: ")

	print("\nYou chose the category", \
	database.records[int(choice)-1][1], ":\n")

	database.get_infos_product(choice)

	for idx, val in enumerate(database.records):
		"""if sentences to display only products with full data"""
		if "" in val:
			del database.records[idx]

	for row in database.records:
		print( row[0], ":", row[1], "(",row[2],")")
			
	choice=input("\nChoose the index of one of the products: \n")
	
	selected=[]
	
	for idx, val in enumerate(database.records):
		if val[0]==int(choice):
			index=idx
		
	for row in database.records:
		if row[2]<database.records[index][2]:
			selected.append(row[0])
	
	if len(selected)==0:
		for row in database.records:
			if row[2]==database.records[index][2]:
				selected.append(row[0])
		print("\nNo healthier product available. However, you can \
choose a product with more or less energy:\n")
	else:
		print("\nHere is the list of healthier products:\n")

	#~ breakpoint()

	for idx, val in enumerate(database.records):
		if val[0] in selected:
			for i in range(4):
				print(val[i], " ", end="")
			print("\n")
	
cli()
