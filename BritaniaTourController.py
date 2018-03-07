#!/usr/bin/python
#-*- coding: utf-8 -*-
from BritaniaTourGUI import BritaniaTourGUI
import importlib # module for importing other modules using string type name
from GUI_NotificationHandler import GUI_NotificationHandler

class BritaniaTourController:
    # TODO is it ok to do it static???
    __user = None

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


    def initDutyController(self, dutyControllerName):
        dutyControllerName += "Controller"
        try:
            cntrlrModule = importlib.import_module('BusinessLogic.'+dutyControllerName)
            cntrlrClass = getattr(cntrlrModule, dutyControllerName)
            dutyContrlr = cntrlrClass("Repository")
            return dutyContrlr
        except ModuleNotFoundError:
            self.gui.raiseErrorMessg("Module not found", "Module '" + dutyControllerName[:-10] + "' was not identified")