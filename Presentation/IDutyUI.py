#!/usr/bin/python
#-*- coding: utf-8 -*-
from abc import ABC, abstractmethod

class IDutyUI(ABC):
    @abstractmethod
    def __init__(self, dutyController, window):
        self.dutyController = dutyController
        self.frame = None
        self.dataWidgets = {}

    @abstractmethod
    def setUpWidgets(self, ):
        pass

    @abstractmethod
    def hide(self, ):
        pass

    @abstractmethod
    def appear(self, ):
        pass

    @abstractmethod
    def close(self, ):
        pass

    @abstractmethod
    def replicate(self, window):
        pass

    @abstractmethod
    def getWidgetData(self, key):
        pass

