#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Setup the database """

from config import CATEGORIES
import models

db = models.Db()

# drop tables if exists:
db.drop_table("product")
db.drop_table("category")

# create tables:
db.create_tables()

for cat in CATEGORIES:
    categorie = models.Category(cat)
    categorie.input_data(db)
