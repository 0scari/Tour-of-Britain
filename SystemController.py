#!/usr/bin/python
#-*- coding: utf-8 -*-
from BritaniaTourGUI import BritaniaTourGUI
import importlib # module for importing other modules using string type __name
from GUI_NotificationHandler import GUI_NotificationHandler
import sqlite3 as sqlite

class SystemController:
    __user = None

    def __init__(self, user):
        SystemController.__user = user
        self.gui = self.__setGui()
        self.gui.startGui()

    def __setGui(self, ):
        return BritaniaTourGUI(self, SystemController.__user.getRoleDuties())

    @staticmethod
    def getUserId():
        if SystemController.__user:
            return SystemController.__user.getId()
        else:
            GUI_NotificationHandler.raiseErrorMessg("Error", "User data corrupt")

    def initDutyController(self, dutyName):
        try:
            # Repository
            dbConn = sqlite.connect("database")
            dbCursor = dbConn.cursor()
            repoModule = importlib.import_module('Data.RepositoryImplementations.' + dutyName + "Repository")
            repoClass = getattr(repoModule, dutyName + "Repository")
            repo = repoClass(dbConn, dbCursor)
            # Controller
            dutyControllerName = dutyName + "Controller"
            cntrlrModule = importlib.import_module('BusinessLogic.'+dutyControllerName)
            cntrlrClass  = getattr(cntrlrModule, dutyControllerName)
            return cntrlrClass(repo)
        except ModuleNotFoundError as err:
            self.gui.raiseWarningMessg("Please note!", "Work on this functionality is in prgress...")
            return False

