#!/usr/bin/python
#-*- coding: utf-8 -*-
from abc import ABC, abstractmethod

class IDutyUI(ABC):
    @abstractmethod
    def __init__(self, dutyController, window = None):
        self.dataWidgets = {}

    @abstractmethod
    def setUpWidgets(self, ):
        pass

    # TODO candidate for unittests
    def _addDataWidget(self, name, key, widget):
        """Polymorphic method"""
        if key not in self.dataWidgets:
            raise ValueError
        else:
            self.dataWidgets[key][name] = widget

    @abstractmethod
    def hide(self, ):
        pass

    def _createDataWidgetKey(self, key):
        """Polymorphic method"""
        if key in self.dataWidgets:
            raise ValueError
        else:
            self.dataWidgets[key] = {}

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

