#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Setup the database """

import config
import models

db = models.Db()

# drop tables if exists:
db.drop_table("product")
db.drop_table("category")

# create tables:
db.create_tables()

db.input_data(db)
