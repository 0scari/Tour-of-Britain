#!/usr/bin/python
# -*- coding: utf-8 -*-
from BusinessLogic.IDutyController import IDutyController

class CustomerRegistrationController(IDutyController):
    def __init__(self, customerRepo):
        super().__init__()
        self.customerRepo = customerRepo

    def registerCustomerr(self, customerDetails):
        for i in customerDetails:
            print(i + ": " + customerDetails[i])

    def checkIfCustomerExists(self, customerDetails):
        pass

    def storeCustomer(self, customerDetails):
        pass

    def validateInput(self, input):
        pass
