#!/usr/bin/python
#-*- coding: utf-8 -*-

class Employee:
    def __init__(self):
        self.role = None
        self.id = "12345"
        self.name = "John Snow"

    def setRole(self, role):
        self.role = role

    def getRoleDuties(self, ):
        return {"cntrlr": ["CustomerManagement", "MembershipManagement", "BookingReservation"],
                "labels": ["Customer Management", "Membership Management", "Bookings and Reservations"]}

    def getId(self):
        return self.id

