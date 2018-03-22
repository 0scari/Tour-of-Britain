#!/usr/bin/python
#-*- coding: utf-8 -*-
from Data.Models.AbstractBaseDataModel import AbsttractBaseDataModel

class Customer(AbsttractBaseDataModel):

    def __init__(self):
        self.__id = None
        self.__name = None
        self.__surname = None
        self.__dob = None
        self.__email = None
        self.__address = None
        self.__createdBy = None

    def getId(self, ):
        return self.__id

    def setId(self, id):
        self.__id = id

    def setName(self, name):
        self.__name = name

    def getName(self, ):
        return self.__name

    def setSurname(self, surname):
        self.__surname = surname

    def getSurname(self, ):
        return self.__surname

    def setDob(self, dd, mm = False, yyyy = False):
        if mm and yyyy:
            self.__dob = str(dd) + '/' + str(mm) + '/' + str(yyyy)
        else:
            self.__dob = str(dd)

    def getDob(self, ):
        return  self.__dob

    def setEmail(self, email):
        self.__email = email

    def getEmail(self, ):
        return self.__email

    def setAddress(self, address):
        self.__address = address

    def getAddress(self, ):
        return self.__address

    def setCreatedBy(self, userId):
        self.__createdBy = userId

    def getCreatedBy(self, ):
        return self.__createdBy

    def getData(self):
        output = {}
        if self.__id:
            output["id"] = self.__id
        if self.__name:
            output["name"] = self.__name
        if self.__surname:
            output["surname"] = self.__surname
        if self.__dob:
            output["dob"] = self.__dob
        if self.__email:
            output["email"] = self.__email
        if self.__address:
            output["address"] = self.__address
        if self.__createdBy:
            output["createdBy"] = self.__createdBy
        return output

    def dataToDict(self):
        return {"Ref." : self.__id,
                "First name": self.__name,
                "Second name": self.__surname,
                "Date of birth": self.__dob,
                "Email": self.__email,
                "Address": self.__email,
                "Creator": self.__createdBy}

