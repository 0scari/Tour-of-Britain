#!/usr/bin/python
#-*- coding: utf-8 -*-

class Role:
    def __init__(self):
        self.duties = []

    def setName(self, name):
        self.name = name

    def addDuty(self, duty):
        self.duties.append(duty)

    def getDuties(self):
        return self.duties

