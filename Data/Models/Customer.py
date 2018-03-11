#!/usr/bin/python
#-*- coding: utf-8 -*-

class Customer():

    def __init__(self):
        self.id = None
        self.name = None
        self.surname = None
        self.dob = None
        self.email = None
        self.address = None
        self.createdBy = None

    def getId(self, ):
        return self.id

    def setId(self, id):
        self.id = id

    def setName(self, name):
        self.name = name

    def getName(self, ):
        return self.name

    def setSurname(self, surname):
        self.surname = surname

    def getSurname(self, ):
        return self.surname

    def setDob(self, dd, mm = False, yyyy = False):
        if mm and yyyy:
            self.dob = dd + '/' + mm + '/' + yyyy
        else:
            self.dob = dd

    def getDob(self, ):
        return  self.dob

    def setEmail(self, email):
        self.email = email

    def getEmail(self, ):
        return self.email

    def setAddress(self, address):
        self.address = address

    def getAddress(self, ):
        return self.address

    def setCreatedBy(self, userId):
        self.createdBy = userId

    def getCreatedBy(self, ):
        return self.createdBy

    def getData(self):
        output = {}
        if self.id:
            output["id"] = self.id
        if self.name:
            output["name"] = self.name
        if self.surname:
            output["surname"] = self.surname
        if self.dob:
            output["dob"] = self.dob
        if self.email:
            output["email"] = self.email
        if self.address:
            output["address"] = self.address
        if self.createdBy:
            output["createdBy"] = self.createdBy
        return output

    def dataToDict(self):
        return {"Reference nr." : self.id,
                "First name": self.name,
                "Second name": self.surname,
                "Date of birth": self.dob,
                "Email": self.email,
                "Address": self.email,
                "Created by:": self.createdBy}

