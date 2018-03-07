#!/usr/bin/python
#-*- coding: utf-8 -*-
from Presentation.IDutyUI import IDutyUI
from tkinter import *


class CustomerRegistrationUI(IDutyUI):
    def __init__(self, dutyController, window):
        super().__init__(dutyController)
        self.dutyController = dutyController

        self.height = window.winfo_height() * 0.95
        self.width  = window.winfo_width() * 0.8

        self.frame = Frame(window, bg="yellow", height=self.height , width=self.width)
        self.appear()
        self.setUpWidgets()

    def registerCustomer(self, ):
        customerDetails = self.getWidgetData("customerDetails")
        self.dutyController.registerCustomerr( customerDetails)

    def setUpWidgets(self):
        inputFrame = Frame(self.frame)

        Label(inputFrame, text="Name").grid(row=0, column=0)
        Label(inputFrame, text="Surname").grid(row=1, column=0)
        Label(inputFrame, text="Date of birth").grid(row=2, column=0)
        Label(inputFrame, text="Email").grid(row=3, column=0)
        Label(inputFrame, text="Address").grid(row=4, column=0)

        self._createDataWidgetKey("customerDetails")
        dataWidget = Entry(inputFrame)
        dataWidget.grid(row=0, column=1)
        self._addDataWidget("name","customerDetails", dataWidget)
        dataWidget = Entry(inputFrame)
        dataWidget.grid(row=1, column=1)
        self._addDataWidget("surname", "customerDetails", dataWidget)

        dobFrame = Frame(inputFrame, bg="blue")
        dobFrame.grid(row=2, column=1, columnspan=1, sticky=N+S+E+W)
        dobFrame.grid_propagate(False)

        dataWidget = Entry(dobFrame)
        dataWidget.grid(row=0, column=0, pady=(1,0))
        self._addDataWidget("dobDD", "customerDetails", dataWidget)
        dataWidget = Entry(dobFrame)
        dataWidget.grid(row=0, column=1, pady=(0,0))
        self._addDataWidget("dobMM", "customerDetails", dataWidget)
        dataWidget = Entry(dobFrame)
        dataWidget.grid(row=0, column=2, pady=(0,0))
        self._addDataWidget("dobYYYY", "customerDetails", dataWidget)

        dobFrame.grid_columnconfigure(0, weight=1)
        dobFrame.grid_columnconfigure(1, weight=1)
        dobFrame.grid_columnconfigure(2, weight=1)


        dataWidget = Entry(inputFrame)
        dataWidget.grid(row=3, column=1)
        self._addDataWidget("email", "customerDetails", dataWidget)
        dataWidget = Entry(inputFrame)
        dataWidget.grid(row=4, column=1)
        self._addDataWidget("address", "customerDetails", dataWidget)
        Button(inputFrame, text="Register",
               command=lambda: self.registerCustomer()).grid(row=5, column=1)

        inputFrame.pack(side=LEFT, padx=(self.width *0.35, 5))