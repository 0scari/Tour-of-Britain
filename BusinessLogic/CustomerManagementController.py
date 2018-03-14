#!/usr/bin/python
# -*- coding: utf-8 -*-
from BusinessLogic.AbstractUseCaseController import AbstractUseCaseController
from GUI_NotificationHandler import GUI_NotificationHandler
from SystemController import SystemController
from Data.Models.Customer import Customer
from Exceptions.DataValidationException import DataValidationException
from Exceptions.InternalErrorException import InternalErrorException
import re as regex

class CustomerManagementController(AbstractUseCaseController):
    def __init__(self, repository):
        super().__init__()
        self._repository = repository

    def registerCustomer(self, customerDetails):
        if not self._validateInput(customerDetails):
            return
        customer = self._constructDataModel(customerDetails)
        customer.setCreatedBy(SystemController.getUserId())
        self._repository.write(customer)

    def updateCustomer(self, customerDetails):
        splitDob = dict(zip(["dobDD", "dobMM", "dobYYYY"], customerDetails["dob"].split("/")))
        del customerDetails["dob"] # delete atomic __dob element
        customerDetails = {**splitDob, **customerDetails} # merge dictionaries
        print(customerDetails)
        if not self._validateInput(customerDetails, False):
            return
        customer = self._constructDataModel(customerDetails)
        if self._repository.update(customer):
            GUI_NotificationHandler.raiseInfoMessg("Success", "Customer was updated successfully")

    def _constructDataModel(self, data):
        customer = Customer()
        if "id" in data:
            customer.setId(data["id"])
        if "name" in data:
            customer.setName(data["name"])
        if "surname" in data:
            customer.setSurname(data["surname"])
        if "dobDD" in data and "dobMM" in data and "dobYYYY" in data:
            customer.setDob(data["dobDD"],
                            data["dobMM"],
                            data["dobYYYY"])
        if "dob" in data:
            customer.setDob(data["dob"])
        if "email" in data:
            customer.setEmail(data["email"])
        if "address" in data:
            customer.setAddress(data["address"])
        if "ref" in data:
            customer.setId(data["ref"])
        if "employee_id" in data:
            customer.setCreatedBy(data["employee_id"])
        if "createdBy" in data:
            customer.setCreatedBy(data["createdBy"])
        return customer

    def findCustomers(self, customerDetails):
        customerDetails = {k: v for k, v in customerDetails.items() if len(v) > 0}
        if not len(customerDetails):
            GUI_NotificationHandler.raiseWarningMessg("Warning", "No search criteria was given")
            return None
        if not self._validateInput(customerDetails, False):
            return None
        customerModel = self._constructDataModel(customerDetails)
        customers = self._repository.readCustomers(customerModel.getData())
        customerModels = []
        for customer in customers:
            customerModels.append(self._constructDataModel(customer))
        if len(customers) > 0:
            return customerModels
        else:
            GUI_NotificationHandler.raiseWarningMessg("Warning", "No customer matches the search criteria")
            return None

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
        validFieldNames = ["ref", "name", "surname", "dobDD", "createdBy",
                           "email", "address", "dobMM", "dobYYYY", "id"]

        for fn in input:
            if fn not in validFieldNames:
                raise InternalErrorException("Field "+fn+"not recognised")

        if "name" in input:
            if len(input["name"]) not in range(2, 255):
                raise DataValidationException("First Name invalid")
            if regex.search(r'\d', input["name"]):
                raise DataValidationException("First Name must be alphabetic")

        if "surname" in input:
            if len(input["surname"]) not in range(2, 255):
                raise DataValidationException("Last Name invalid")
            if regex.search(r'\d', input["surname"]):
                raise DataValidationException("Last Name must be alphabetic")

        if "dobDD" in input or "dobMM" in input or "dobYYYY" in input:
            try:
                if self.__isInt(input["dobDD"]) \
                 and self.__isInt(input["dobMM"]) \
                 and self.__isInt(input["dobYYYY"]):
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

    def __isInt(self, input):
        try:
            num = int(input)
        except ValueError:
            return False
        return True

