#!/usr/bin/python
# -*- coding: utf-8 -*-
from BusinessLogic.IUseCaseController import IUseCaseController
from GUI_NotificationHandler import GUI_NotificationHandler
from SystemController import SystemController
from Data.Models.Customer import Customer
from Exceptions.DataValidationException import DataValidationException
from Exceptions.InternalErrorException import InternalErrorException
import re as regex


class CustomerManagementController(IUseCaseController):
    def __init__(self, repository):
        super().__init__()
        self.repository = repository

    def registerCustomer(self, customerDetails):
        if not self._validateInput(customerDetails):
            return
        GUI_NotificationHandler.raiseInfoMessg("Success", "Customer registered successfully")
        customer = self._constructDataModel(customerDetails)
        self.repository.write(customer)

    def _constructDataModel(self, data):
        customer = Customer()
        customer.setName(data["name"])
        customer.setSurname(data["surname"])
        customer.setDob(data["dobDD"],
                        data["dobMM"],
                        data["dobYYYY"])
        customer.setEmail(data["email"])
        customer.setAddress(data["address"])
        customer.setCreatedBy(SystemController.getUserId())
        return customer

    def checkIfCustomerExists(self, customerDetails):
        pass

    def storeCustomer(self, customerDetails):
        pass

    def _validateInput(self, customerDetails):
        try:
            self._inputValidation(customerDetails)
            return True
        except DataValidationException as err:
            GUI_NotificationHandler.raiseErrorMessg("Validation Error", err)
        except InternalErrorException as err:
            GUI_NotificationHandler.raiseErrorMessg("Internal Error", err)

        return False

    def _inputValidation(self, input):
        import datetime
        validFieldNames = ["name", "surname", "dobDD", "email", "address", "dobMM", "dobYYYY"]

        if len(input) != len(validFieldNames):
            raise InternalErrorException("Field wrong field amount")

        for fn in input:
            if fn not in validFieldNames:
                raise InternalErrorException("Field not recognised")

        if len(input["name"]) not in range(2, 255):
            raise DataValidationException("First Name too short")
        if regex.search(r'\d', input["name"]):
            raise DataValidationException("First Name must be alphabetic")

        if len(input["surname"]) not in range(2, 255):
            raise DataValidationException("Last Name too short")
        if regex.search(r'\d', input["surname"]):
            raise DataValidationException("First Name must be alphabetic")

        if self.__is_int(input["dobDD"]) \
         and self.__is_int(input["dobMM"]) \
         and self.__is_int(input["dobYYYY"]):
            if int(input["dobYYYY"]) not in range(1900, 2018):
                raise DataValidationException("Invalid year")
            try:
                datetime.date(int(input["dobYYYY"]), int(input["dobMM"]), int(input["dobDD"]))

            except ValueError:
                raise DataValidationException("Non-existent date")
        else:
            raise DataValidationException("Inappropriate date format")

        validEmail = \
            regex.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$',
                        input["email"])
        if not validEmail:
            raise DataValidationException("Bad email format")

        if len(input["address"]) not in range(10, 255):
            raise DataValidationException("Address too short")

        return True

    def __is_int(self, input):
        try:
            num = int(input)
        except ValueError:
            return False
        return True
