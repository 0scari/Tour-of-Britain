#!/usr/bin/python
#-*- coding: utf-8 -*-
import sqlite3 as sql
from AuthenticationController import AuthenticationController
from BritaniaTourController import BritaniaTourController

class BritaniaTour:
    def __init__(self):
        user = AuthenticationController.login()
        BritaniaTourController(user)

if __name__ == "__main__":
    bt = BritaniaTour()

