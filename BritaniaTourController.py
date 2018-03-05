#!/usr/bin/python
#-*- coding: utf-8 -*-
from BritaniaTourGUI import BritaniaTourGUI
import importlib # module for importing other modules using string type name

class BritaniaTourController:
    def __init__(self, user):
        self.user = user
        self.gui = self.setGui()
        self.gui.startGui()

    def setGui(self, ):
        employeeDuties = {"cntrlr": ["CustomerRegistration", "CustomerLookup", "TripLookup"],
                          "labels": ["Register a new customer", "Find a customer", "Find a trip"]}
        return BritaniaTourGUI(self, employeeDuties)

    def getEmployeeDuties(self, ):
        pass

    def initDutyController(self, dutyControllerName):
        dutyControllerName += "Controller"
        try:
            cntrlrModule = importlib.import_module('BusinessLogic.'+dutyControllerName)
            cntrlrClass = getattr(cntrlrModule, dutyControllerName)
            dutyContrlr = cntrlrClass("Repository")
            return dutyContrlr
        except ModuleNotFoundError:
            self.gui.raiseErrorMessg("Module not found", "Module '" + dutyControllerName[:-10] + "' was not identified")