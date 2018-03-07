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
        pass

    def create(self, ):
        pass

    def setName(self, name):
        self.name = name

    def getName(self, ):
        pass

    def setSurname(self, surname):
        self.surname = surname

    def getSurname(self, ):
        pass

    def setDob(self, dd, mm, yyyy):
        self.dob = dd + '/' + mm + '/' + yyyy

    def getDob(self, ):
        return  self.dob

    def setEmail(self, email):
        self.email = email

    def getEmail(self, ):
        pass

    def setAddress(self, address):
        self.address = address

    def getAddress(self, ):
        pass

    def setCreatedBy(self, userId):
        self.createdBy = userId

    def getCreatedBy(self, ):
        pass

