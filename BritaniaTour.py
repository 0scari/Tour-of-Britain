#!/usr/bin/python
#-*- coding: utf-8 -*-
import sqlite3 as sql
from AuthenticationController import AuthenticationController
from SystemController import SystemController

# TODO - PSC: ajust theme, data input fields alignment, DataGrid conflicts
# TODO - add The title to the Customer Management frame (mind replacment when searching for customer)
# TODO - search by id
# TODO - implement tab closing

class BritaniaTour:
    def __init__(self):
        user = AuthenticationController.login()
        SystemController(user)


if __name__ == "__main__":
    BritaniaTour()

