#!/usr/bin/python
#-*- coding: utf-8 -*-
from Presentation.IDutyUI import IDutyUI
from tkinter import *
from GUI_NotificationHandler import GUI_NotificationHandler


class CustomerManagementUI(IDutyUI):
    def __init__(self, UseCaseController, window):
        super().__init__(UseCaseController)
        self.__useCaseController = UseCaseController

        self.height = window.winfo_height() * 0.95
        self.width  = window.winfo_width() * 0.8

        self.frame = Frame(window, bg="yellow", height=self.height , width=self.width)
        self.appear()
        self.setUpWidgets()

    def registerCustomer(self, ):
        customerDetails = self.getWidgetData("customerDetails")
        self.__useCaseController.registerCustomer(customerDetails)

    def setUpWidgets(self):
        inputFrame = Frame(self.frame)

        refLabel = Label(inputFrame, text="Reference nr.")
        refLabel.grid(row=0, column=0)
        Label(inputFrame, text="First name").grid(row=1, column=0)
        Label(inputFrame, text="Second name").grid(row=2, column=0)
        Label(inputFrame, text="Date of birth").grid(row=3, column=0)
        Label(inputFrame, text="Email").grid(row=4, column=0)
        Label(inputFrame, text="Address").grid(row=5, column=0)
        Label(inputFrame, text="Please choose an option:").grid(row=7, column=0)
        Label(inputFrame, text="").grid(row=6, column=0)
        Label(inputFrame, text="").grid(row=7, column=1)



        self._createDataWidgetKey("customerDetails")

        refEntry = Entry(inputFrame)
        refEntry.grid(row=0, column=1)
        self._addDataWidget("ref", "customerDetails", refEntry)

        dataWidget = Entry(inputFrame)
        dataWidget.grid(row=1, column=1)
        self._addDataWidget("name","customerDetails", dataWidget)

        dataWidget = Entry(inputFrame)
        dataWidget.grid(row=2, column=1)
        self._addDataWidget("surname", "customerDetails", dataWidget)

        dobFrame = Frame(inputFrame, bg="blue")
        dobFrame.grid(row=3, column=1, columnspan=1, sticky=N+S+E+W)
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
        dataWidget.grid(row=4, column=1)
        self._addDataWidget("email", "customerDetails", dataWidget)

        dataWidget = Entry(inputFrame)
        dataWidget.grid(row=5, column=1)
        self._addDataWidget("address", "customerDetails", dataWidget)

        var = IntVar()
        var.set(None)
        Radiobutton(inputFrame, text="Find customer", variable=var, value=1, \
                    command=lambda: [refLabel.config(state=DISABLED),
                                     refEntry.config(state=DISABLED)]).grid(row=7, column=1, sticky=W)
        Radiobutton(inputFrame, text="Register customer", variable=var, value=2, \
                    command=lambda: [refLabel.config(state=NORMAL),
                                     refEntry.config(state=NORMAL)]).grid(row=8, column=1, sticky=W)

        Button(inputFrame, text="Submit",
               command=lambda opt = var: self.__submitActionCallback(opt)).grid(row=9, column=1)

        inputFrame.pack(side=LEFT, padx=(self.width *0.35, 5))

    def __submitActionCallback(self, opt, ):
        if opt == 1:
            pass
        elif opt == 2:
            self.__useCaseController.registerCustomer(self.getWidgetData("customerDetails"))
        else:
            GUI_NotificationHandler.raiseWarningMessg("Warning", "Option not selected")

