#!/usr/bin/python
#-*- coding: utf-8 -*-
from BritaniaTourGUI import BritaniaTourGUI
import importlib # module for importing other modules using string type name
from GUI_NotificationHandler import GUI_NotificationHandler
import sqlite3 as sqlite

class BritaniaTourController:
    # TODO is it ok to do it static???
    __user = None
    conn = None # Temporary hack

    def __init__(self, user):
        BritaniaTourController.__user = user
        self.gui = self.setGui()
        GUI_NotificationHandler.setGui(self.gui)
        self.gui.startGui()

    def setGui(self, ):
        employeeDuties = {"cntrlr": ["MembershipManagement", "CustomerLookup", "TripLookup"],
                          "labels": ["Membership Management", "Find a customer", "Find a trip"]}
        return BritaniaTourGUI(self, employeeDuties)

    def getEmployeeDuties(self, ):
        pass

    @staticmethod
    def getUserId():
        if BritaniaTourController.__user:
            return BritaniaTourController.__user.getId()
        else:
            GUI_NotificationHandler.raiseErrorMessg("Error", "User data corrupt")


    def initDutyController(self, dutyName):
        dutyControllerName = dutyName + "Controller"
        try:
            # Controller
            cntrlrModule = importlib.import_module('BusinessLogic.'+dutyControllerName)
            cntrlrClass  = getattr(cntrlrModule, dutyControllerName)
            # Repository
            BritaniaTourController.conn = sqlite.connect("database")
            dbCursor = BritaniaTourController.conn.cursor()
            repoModule = importlib.import_module('Data.RepositoryImplementations.' + dutyName + "Repository")
            repoClass = getattr(repoModule, dutyName + "Repository")
            repo = repoClass(dbCursor)
            return cntrlrClass(repo)
        except Exception as e:
             self.gui.raiseErrorMessg("Error", str(e))
             # close

    # def dynamicLoading():