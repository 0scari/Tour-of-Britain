#!/usr/bin/python
#-*- coding: utf-8 -*-
from abc import ABC, abstractmethod

class AbstractCustomerManagementRepository(ABC):
    @abstractmethod
    def __init__(self, connection):
        self._connection = connection

    @abstractmethod
    def write(self, customer):
        pass

    @abstractmethod
    def read(self, conditions):
        pass
