#!/usr/bin/python
#-*- coding: utf-8 -*-
from abc import ABC, abstractmethod
from tkinter import *


class IDutyUI(ABC):
    @abstractmethod
    def __init__(self, dutyController, window = None):
        self.dataWidgets = {}
        self.frame = None
        self.__useCaseController = dutyController

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

    def getDutyName(self):
        return self.__class__.__name__[:-2]

    def hide(self, ):
        self.frame.pack_forget()

    def _createDataWidgetKey(self, key):
        """Polymorphic method"""
        if key in self.dataWidgets:
            raise ValueError
        else:
            self.dataWidgets[key] = {}

    def appear(self, pos):
        self.frame.pack_propagate(False)
        self.frame.pack(side=pos)

    def close(self, ):
        pass

    def replicate(self, window):
        return self.__useCaseController.initDutyUI(window)

    def getWidgetData(self, key):
        if key not in self.dataWidgets:
            raise ValueError
        outputData = {}
        print(len(self.dataWidgets))
        print(len(self.dataWidgets[key]))
        for fieldName, dataWidget in self.dataWidgets[key].items():
            outputData[fieldName] = dataWidget.get()
        return outputData

