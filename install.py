#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Setup the database """

import config
import models

db = models.Db()

db.create_tables()

db.input_data(db)
