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
        customer.setCreatedBy(SystemController.getUserId())
        self.repository.write(customer)

    def _constructDataModel(self, data):
        customer = Customer()
        if "name" in data:
            customer.setName(data["name"])
        if "surname" in data:
            customer.setSurname(data["surname"])
        if "dobDD" in data and "dobMM" in data and "dobYYYY" in data:
            customer.setDob(data["dobDD"],
                            data["dobMM"],
                            data["dobYYYY"])
        if "email" in data:
            customer.setEmail(data["email"])
        if "address" in data:
            customer.setAddress(data["address"])
        return customer

    def findCustomers(self, customerDetails):
        customerDetails = {k: v for k, v in customerDetails.items() if len(v) > 0}
        if not len(customerDetails):
            GUI_NotificationHandler.raiseWarningMessg("Warning", "No search criteria was given")
            return None
        if not self._validateInput(customerDetails, False):
            return None
        customerModel = self._constructDataModel(customerDetails)
        customers = self.repository.readCustomers(customerModel.getData())
        if len(customers) > 0:
            return customers
        else:
            GUI_NotificationHandler.raiseWarningMessg("Warning", "No customer matches the search criteria")
            return None

    def storeCustomer(self, customerDetails):
        pass

    def _validateInput(self, customerDetails, fullValidation = True):
        try:
            self._inputValidation(customerDetails, fullValidation)
            return True
        except DataValidationException as err:
            GUI_NotificationHandler.raiseErrorMessg("Validation Error", err)
        except InternalErrorException as err:
            GUI_NotificationHandler.raiseErrorMessg("Internal Error", err)

        return False

    def _inputValidation(self, input, fullValidation):
        import datetime
        validFieldNames = ["ref", "name", "surname", "dobDD",
                           "email", "address", "dobMM", "dobYYYY"]

        if len(input) != len(validFieldNames) and fullValidation:
            raise InternalErrorException("Wrong field amount")

        for fn in input:
            if fn not in validFieldNames:
                raise InternalErrorException("Field not recognised")

        if "name" in input:
            if len(input["name"]) not in range(2, 255):
                raise DataValidationException("First Name invalid")
            if regex.search(r'\d', input["name"]):
                raise DataValidationException("First Name must be alphabetic")

        if "surname" in input:
            if len(input["surname"]) not in range(2, 255):
                raise DataValidationException("Last Name invalid")
            if regex.search(r'\d', input["surname"]):
                raise DataValidationException("First Name must be alphabetic")

        if "dobDD" in input or "dobMM" in input or "dobYYYY" in input:
            try:
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
            except KeyError:
                raise DataValidationException("Some part of date of birth is missing")

        if "email" in input:
            validEmail = \
                regex.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$',
                            input["email"])
            if not validEmail:
                raise DataValidationException("Email invalid")

        if "address" in input:
            if len(input["address"]) not in range(10, 255):
                raise DataValidationException("Address invalid")

        return True

    def __is_int(self, input):
        try:
            num = int(input)
        except ValueError:
            return False
        return True
