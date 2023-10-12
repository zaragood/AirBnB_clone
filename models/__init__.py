#!/usr/bin/python3
"""python package model"""

"""importing file_storage from models.engine"""
from models.engine.file_storage import FileStorage

"""creating an instance of file_storage"""
storage = FileStorage()

"""calling the reloade method on the instance 'sorage'"""
storage.reload()
