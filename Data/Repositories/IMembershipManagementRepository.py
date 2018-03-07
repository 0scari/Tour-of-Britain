#!/usr/bin/python
#-*- coding: utf-8 -*-
from abc import ABC, abstractmethod

class IMembershipManagementRepository:
    @abstractmethod
    def __init__(self, connection):
        self._connection = connection

    @abstractmethod
    def write(self, customer):
        pass

    @abstractmethod
    def read(self, criteria):
        pass

