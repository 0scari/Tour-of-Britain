#!/usr/bin/python
#-*- coding: utf-8 -*-

class Customer:

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

    def setName(self, name):
        self.name = name

    def getName(self, ):
        return self.name

    def setSurname(self, surname):
        self.surname = surname

    def getSurname(self, ):
        return self.surname

    def setDob(self, dd, mm, yyyy):
        self.dob = dd + '/' + mm + '/' + yyyy

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

    def dataToDict(self):
        return {"Reference nr." : self.id,
                "First name": self.name,
                "Second name": self.surname,
                "Date of birth": self.dob,
                "Email": self.email,
                "Address": self.email,
                "Created by:": self.createdBy}

