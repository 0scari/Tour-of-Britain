#!/usr/bin/python
# -*- coding: utf-8 -*-
from BusinessLogic.IDutyController import IDutyController
from GUI_NotificationHandler import GUI_NotificationHandler
from BritaniaTourController import BritaniaTourController
from Data.Models.Customer import Customer

class MembershipManagementController(IDutyController):
    def __init__(self, customerRepo):
        super().__init__()
        self.customerRepo = customerRepo

    def registerCustomer(self, customerDetails):
        if self.validateInput(customerDetails) == True:
            GUI_NotificationHandler.raiseInfoMessg("Success", "Customer registered successfully")
            customer = self.constructDataModel(customerDetails)
            print(customer.getDob())
        else:
            GUI_NotificationHandler.raiseErrorMessg("Error", "Customer details invalid")

    def constructDataModel(self, data):
        customer = Customer()
        customer.setName(data["name"])
        customer.setSurname(data["surname"])
        customer.setDob(data["dobDD"],
                        data["dobMM"],
                        data["dobYYYY"])
        customer.setEmail(data["email"])
        customer.setAddress(data["address"])
        customer.setCreatedBy(BritaniaTourController.getUserId())
        return customer

    def checkIfCustomerExists(self, customerDetails):
        pass

    def storeCustomer(self, customerDetails):
        pass

    def validateInput(self, input):
        validFieldNames = ["name", "surname", "dobDD", "email", "address", "dobMM", "dobYYYY"]

        if len(input) != len(validFieldNames):
            return False

        for fn in input:
            if fn not in validFieldNames:
                return False

        if isinstance(input["name"], str):
            if len(input["name"]) not in range(2,255):
                return False
        else:
            return False

        print("DBG")

        if isinstance(input["surname"], str):
            if len(input["surname"]) not in range(2,255):
                return False
        else:
            return False

        if isinstance(input["email"], str):
            if len(input["email"]) not in range(5,255):
                return False
        else:
            return False

        if isinstance(input["address"], str):
            if len(input["address"]) not in range(10,255):
                return False
        else:
            return False
        print("DBG1")


        if self.__is_int(input["dobDD"]):
            if int(input["dobDD"]) not in range(0, 31):
                return False
        else:
            return False

        if self.__is_int(input["dobMM"]):
            if int(input["dobMM"]) not in range(1, 12):
                return False
        else:
            return False
        print("DBG2")

        if self.__is_int(input["dobYYYY"]):
            if int(input["dobYYYY"]) not in range(1900, 2018):
                return False
        else:
            return False

        return True

    def __is_int(self, input):
      try:
        num = int(input)
      except ValueError:
        return False
      return True
