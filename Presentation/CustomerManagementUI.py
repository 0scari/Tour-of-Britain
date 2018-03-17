#!/usr/bin/python
#-*- coding: utf-8 -*-
from Presentation.AbstractUseCaseUI import AbstractUseCaseUI
from tkinter import *
from GUI_NotificationHandler import GUI_NotificationHandler
from Presentation.DataGrid import DataGrid


class CustomerManagementUI(AbstractUseCaseUI):
    def __init__(self, useCaseController, window):
        super().__init__(useCaseController)
        self.__useCaseController = useCaseController
        self._height = window.winfo_height() * 0.95
        self._width  = window.winfo_width() * 0.8
        self._mainFrame = Frame(window, height=self._height, width=self._width)
        self.appear(BOTTOM)
        self.__inputFrame = Frame(self._mainFrame)
        self.__inputFrame.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.__dataGrid = None
        self.__titleLabel = None
        self._setUpCloseBttn()
        self._setUpWidgets()

    def registerCustomer(self, ):
        customerDetails = self._getWidgetData("customerDetails")
        self.__useCaseController.registerCustomer(customerDetails)

    def _setUpWidgets(self):
        self.__titleLabel = Label(self._mainFrame, text="Customer Management")
        self.__titleLabel.pack(side=TOP, pady=(35,0))
        self.__titleLabel.config(font=("Courier", 40))
        refLabel = Label(self.__inputFrame, text="Reference nr.")
        refLabel.grid(row=0, column=0, sticky=W)
        Label(self.__inputFrame, text="First name").grid(row=1, column=0, sticky=W)
        Label(self.__inputFrame, text="Second name").grid(row=2, column=0, sticky=W)
        Label(self.__inputFrame, text="Date of birth (D:M:Y)").grid(row=3, column=0, sticky=W)
        Label(self.__inputFrame, text="Email").grid(row=4, column=0, sticky=W)
        Label(self.__inputFrame, text="Address").grid(row=5, column=0, sticky=W)
        Label(self.__inputFrame, text="Please choose an option:").grid(row=7, column=0, sticky=W)
        Label(self.__inputFrame, text="").grid(row=6, column=0)
        Label(self.__inputFrame, text="").grid(row=7, column=1)

        self._createDataWidgetKey("customerDetails")

        refEntry = Entry(self.__inputFrame)
        refEntry.grid(row=0, column=1, columnspan=3, sticky=E+W)
        self._addDataWidget("ref", "customerDetails", refEntry)

        dataWidget = Entry(self.__inputFrame)
        dataWidget.grid(row=1, column=1,columnspan=3, sticky=E+W)
        self._addDataWidget("name","customerDetails", dataWidget)

        dataWidget = Entry(self.__inputFrame)
        dataWidget.grid(row=2, column=1,columnspan=3, sticky=E+W)
        self._addDataWidget("surname", "customerDetails", dataWidget)

        dataWidget = Entry(self.__inputFrame, width=7)
        dataWidget.grid(row=3, column=1)
        self._addDataWidget("dobDD", "customerDetails", dataWidget)
        dataWidget = Entry(self.__inputFrame, width=7)
        dataWidget.grid(row=3, column=2)
        self._addDataWidget("dobMM", "customerDetails", dataWidget)
        dataWidget = Entry(self.__inputFrame, width=7)
        dataWidget.grid(row=3, column=3)
        self._addDataWidget("dobYYYY", "customerDetails", dataWidget)

        dataWidget = Entry(self.__inputFrame)
        dataWidget.grid(row=4, column=1, columnspan=3, sticky=N+S+E+W)
        self._addDataWidget("email", "customerDetails", dataWidget)

        dataWidget = Entry(self.__inputFrame)
        dataWidget.grid(row=5, column=1, columnspan=3, sticky=E+W)
        self._addDataWidget("address", "customerDetails", dataWidget)

        var = IntVar()
        var.set(0)
        Radiobutton(self.__inputFrame, text="Find customer", variable=var, value=1, \
                    command=lambda: [refLabel.config(state=NORMAL),
                                     refEntry.config(state=NORMAL)]).grid(columnspan=3, row=7, column=1, sticky=W)
        Radiobutton(self.__inputFrame, text="Register customer", variable=var, value=2, \
                    command=lambda: [refLabel.config(state=DISABLED),
                                     refEntry.config(state=DISABLED)]).grid(columnspan=3, row=8, column=1, sticky=W)
        Button(self.__inputFrame, text="Submit",
               command=lambda : self.__submitActionCallback(var.get())).grid(columnspan=3, row=9, column=1)

    def __submitActionCallback(self, opt):
        if opt == 1: # FIND CUSTOMERS
            customers = self.__useCaseController.findCustomers(self._getWidgetData("customerDetails"))
            if customers:
                if self.__dataGrid: # remove previous data grid
                    # self.__dataGrid.destruct()
                    # self.__dataGrid = None
                    return
                self.__titleLabel.pack_forget()
                self.__inputFrame.place(rely=0.48, anchor=S)
                self.__dataGrid = DataGrid(self._mainFrame, self._height * 0.5).setDataSet(customers)
                self.__dataGrid.setUpdateCallback(self.__useCaseController.updateCustomer)
                self.__dataGrid.pack(BOTTOM)
        elif opt == 2: # REGISTER CUSTOMERS
            self.__useCaseController.registerCustomer(self._getWidgetData("customerDetails"))
        else:
            GUI_NotificationHandler.raiseWarningMessg("Warning", "Option not selected")