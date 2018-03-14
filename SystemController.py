#!/usr/bin/python
#-*- coding: utf-8 -*-
from BritaniaTourGUI import BritaniaTourGUI
import importlib # module for importing other modules using string type name
from GUI_NotificationHandler import GUI_NotificationHandler
import sqlite3 as sqlite

class SystemController:
    __user = None
    conn = None # Temporary hack

    def __init__(self, user):
        SystemController.__user = user
        self.gui = self.setGui()
        GUI_NotificationHandler.setGui(self.gui)
        self.gui.startGui()

    def setGui(self, ):
        employeeDuties = {"cntrlr": ["CustomerManagement", "MembershipManagement", "BookingReservation"],
                          "labels": ["Customer Management", "Membership Management", "Bookings and Reservations"]}
        return BritaniaTourGUI(self, employeeDuties)

    def getEmployeeDuties(self, ):
        pass

    @staticmethod
    def getUserId():
        if SystemController.__user:
            return SystemController.__user.getId()
        else:
            GUI_NotificationHandler.raiseErrorMessg("Error", "User data corrupt")


    def initDutyController(self, dutyName):
        '''
        Factory method
        @type  
        @param dutyName:
        @return:
        '''
        dutyControllerName = dutyName + "Controller"
        try:
            # Controller
            cntrlrModule = importlib.import_module('BusinessLogic.'+dutyControllerName)
            cntrlrClass  = getattr(cntrlrModule, dutyControllerName)
            # Repository
            SystemController.conn = sqlite.connect("database")
            dbCursor   = SystemController.conn.cursor()
            repoModule = importlib.import_module('Data.RepositoryImplementations.' + dutyName + "Repository")
            repoClass  = getattr(repoModule, dutyName + "Repository")
            repo = repoClass(dbCursor)
            return cntrlrClass(repo)
        except ModuleNotFoundError as err:
            self.gui.raiseWarningMessg("Please note!", "Work on this functionality is in prgress...")
            return False

    # def dynamicLoading():