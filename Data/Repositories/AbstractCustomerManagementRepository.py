#!/usr/bin/python
#-*- coding: utf-8 -*-
from abc import ABC, abstractmethod

class AbstractCustomerManagementRepository(ABC):
    @abstractmethod
    def __init__(self, connection, cursor):
        self._cursor = cursor
        self._connection = connection
    @abstractmethod
    def write(self, customer):
        pass

    @abstractmethod
    def read(self, conditions):
        pass

    @abstractmethod
    def update(self, customer):
        pass

    @abstractmethod
    def delete(self, id):
        pass
