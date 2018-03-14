#!/usr/bin/python
#-*- coding: utf-8 -*-
from abc import ABC, abstractmethod
from tkinter import *


class AbstractUseCaseUI(ABC):
    @abstractmethod
    def __init__(self, useCaseController, window = None):
        self._dataWidgets = {}
        self._mainFrame = None
        self._useCaseController = useCaseController

    @abstractmethod
    def _setUpWidgets(self, ):
        pass

    # TODO candidate for unittests
    def _addDataWidget(self, name, key, widget):
        """Polymorphic method"""
        if key not in self._dataWidgets:
            raise ValueError
        else:
            self._dataWidgets[key][name] = widget

    def getDutyName(self):
        return self.__class__.__name__[:-2]

    def hide(self):
        self._mainFrame.pack_forget()

    def _createDataWidgetKey(self, key):
        if key in self._dataWidgets:
            raise ValueError
        else:
            self._dataWidgets[key] = {}

    def appear(self, pos):
        self._mainFrame.pack_propagate(False)
        self._mainFrame.pack(side=pos)

    def close(self, ):
        self.hide()

    def replicate(self, window):
        return self._useCaseController.initDutyUI(window)

    def _getWidgetData(self, key):
        if key not in self._dataWidgets:
            raise ValueError
        outputData = {}
        print(len(self._dataWidgets))
        print(len(self._dataWidgets[key]))
        for fieldName, dataWidget in self._dataWidgets[key].items():
            outputData[fieldName] = dataWidget.get()
        return outputData

    def _setUpCloseBttn(self):
        # set up label with picture
        photo = PhotoImage(file=r"closeBttn.gif")
        label = Label(self._mainFrame, image=photo, width=15, height=15, )
        label.pack(side=TOP, anchor=W, padx=7, pady=7)
        label.config(bg='systemTransparent')
        label.image = photo  # keep a reference!
        #  set up on-click event
        # label.bind("<Button-1>", lambda event: self.__addDutyUI_Tab())

