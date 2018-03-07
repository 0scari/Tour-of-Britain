#!/usr/bin/python
# -*- coding: utf-8 -*-
from BusinessLogic.IDutyController import IDutyController

class CustomerRegistrationController(IDutyController):
    def __init__(self, customerRepo):
        super().__init__()
        self.customerRepo = customerRepo

    def registerCustomerr(self, customerDetails):
        if self.validateInput(customerDetails) == True:
            print("Input valid")
            for i in customerDetails:
                print(i + ": " + customerDetails[i])
        else:
            print("Input invalid")


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