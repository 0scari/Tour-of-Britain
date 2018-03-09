#!/usr/bin/python
#-*- coding: utf-8 -*-
from Presentation.IDutyUI import IDutyUI
from tkinter import *
from GUI_NotificationHandler import GUI_NotificationHandler
from Presentation.DataGrid import DataGrid


class CustomerManagementUI(IDutyUI):
    def __init__(self, UseCaseController, window):
        super().__init__(UseCaseController)
        self.__useCaseController = UseCaseController

        self.height = window.winfo_height() * 0.95
        self.width  = window.winfo_width() * 0.8

        self.frame = Frame(window, bg="yellow", height=self.height , width=self.width)
        self.appear(BOTTOM)
        self.__inputFrame = Frame(self.frame)
        self.setUpWidgets()

    def registerCustomer(self, ):
        customerDetails = self.getWidgetData("customerDetails")
        self.__useCaseController.registerCustomer(customerDetails)

    def setUpWidgets(self):
        refLabel = Label(self.__inputFrame, text="Reference nr.")
        refLabel.grid(row=0, column=0)
        Label(self.__inputFrame, text="First name").grid(row=1, column=0)
        Label(self.__inputFrame, text="Second name").grid(row=2, column=0)
        Label(self.__inputFrame, text="Date of birth").grid(row=3, column=0)
        Label(self.__inputFrame, text="Email").grid(row=4, column=0)
        Label(self.__inputFrame, text="Address").grid(row=5, column=0)
        Label(self.__inputFrame, text="Please choose an option:").grid(row=7, column=0)
        Label(self.__inputFrame, text="").grid(row=6, column=0)
        Label(self.__inputFrame, text="").grid(row=7, column=1)

        self._createDataWidgetKey("customerDetails")

        refEntry = Entry(self.__inputFrame)
        refEntry.grid(row=0, column=1)
        self._addDataWidget("ref", "customerDetails", refEntry)

        dataWidget = Entry(self.__inputFrame)
        dataWidget.grid(row=1, column=1)
        self._addDataWidget("name","customerDetails", dataWidget)

        dataWidget = Entry(self.__inputFrame)
        dataWidget.grid(row=2, column=1)
        self._addDataWidget("surname", "customerDetails", dataWidget)

        dobFrame = Frame(self.__inputFrame, bg="blue")
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

        dataWidget = Entry(self.__inputFrame)
        dataWidget.grid(row=4, column=1)
        self._addDataWidget("email", "customerDetails", dataWidget)

        dataWidget = Entry(self.__inputFrame)
        dataWidget.grid(row=5, column=1)
        self._addDataWidget("address", "customerDetails", dataWidget)

        var = IntVar()
        var.set(0)
        Radiobutton(self.__inputFrame, text="Find customer", variable=var, value=1, \
                    command=lambda: [refLabel.config(state=NORMAL),
                                     refEntry.config(state=NORMAL)]).grid(row=7, column=1, sticky=W)
        Radiobutton(self.__inputFrame, text="Register customer", variable=var, value=2, \
                    command=lambda: [refLabel.config(state=DISABLED),
                                     refEntry.config(state=DISABLED)]).grid(row=8, column=1, sticky=W)

        Button(self.__inputFrame, text="Submit",
               command=lambda : self.__submitActionCallback(var.get())).grid(row=9, column=1)

        print(str(var))

        self.__inputFrame.place(relx=0.5, rely=0.5, anchor=CENTER)

    def __submitActionCallback(self, opt, ):
        if opt == 1: # FIND CUSTOMERS
            customers = self.__useCaseController.findCustomers(self.getWidgetData("customerDetails"))
            # self.__inputFrame.place(rely=0.45, anchor=S)
            # data = [{"Reference nr." : "Hue",
            #     "First name": "Bob",
            #     "Second name": "Bob",
            #     "Date of birth": "Bob",
            #     "Email": "Bob",
            #     "Address": "Bob",
            #     "Created by:": "Bob"}, {"Reference nr." : "Susan",
            #     "First name": "Susan",
            #     "Second name": "Susan",
            #     "Date of birth": "Susan",
            #     "Email": "Susan",
            #     "Address": "Susan",
            #     "Created by:": "Susan"}]
            dataGrid = DataGrid(self.frame, self.height * 0.5).setData(customers)
            dataGrid.pack(side=BOTTOM)
        elif opt == 2: # REGISTER CUSTOMERS
            self.__useCaseController.registerCustomer(self.getWidgetData("customerDetails"))
        else:
            GUI_NotificationHandler.raiseWarningMessg("Warning", "Option not selected")
