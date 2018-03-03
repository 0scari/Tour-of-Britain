#!/usr/bin/python
#-*- coding: utf-8 -*-
from Presentation.IDutyUI import IDutyUI
from tkinter import *


class CustomerRegistrationUI(IDutyUI):
    def __init__(self, dutyController, window):
        super().__init__(dutyController)

        self.dataWidgets = {}
        self.dutyController = dutyController

        self.height = window.winfo_height() * 0.95
        self.width  = window.winfo_width() * 0.8

        self.frame = Frame(window, bg="yellow", height=self.height , width=self.width)
        self.frame.pack_propagate(False)
        self.frame.pack(side=TOP)

        self.setUpWidgets()

    def registerCustomer(self, ):
        pass

    def setUpWidgets(self):
        labelContainer = Frame(self.frame, bg="brown")

            #Frame(self.frame, bg="green").pack(side=TOP, fill=X, pady=(self.height * 0.1, 0))
        Label(labelContainer, text="Name").pack(side=TOP)
        Label(labelContainer, text="Surname").pack(side=TOP)
        Label(labelContainer, text="Date of birth").pack(side=TOP)

        labelContainer.pack(side=LEFT, padx=(self.width *0.2, 0))
        #
        # Entry(self.frame).pack(side=RIGHT)
        # Entry(self.frame).pack(side=RIGHT)
        # Entry(self.frame).pack(side=RIGHT)

    def hide(self, ):
        pass

    def appear(self, ):
        pass

    def close(self, ):
        pass

    def replicate(self, window):
        pass

    def getWidgetData(self, key):
        pass