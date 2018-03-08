#!/usr/bin/python
#-*- coding: utf-8 -*-
from Presentation.IDutyUI import IDutyUI
from tkinter import *
from GUI_NotificationHandler import GUI_NotificationHandler
from Presentation.VerticalScrollableFrame import VerticalScrolledFrame


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
        var.set(None)
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
        if opt == 1:
            self.__inputFrame.place(rely=0.45, anchor=S)
            outputFrame = VerticalScrolledFrame(self.frame, self.height * 0.5)

            refLabel = Label(outputFrame.interior, text="Reference nr.")
            refLabel.grid(row=0, column=0)
            Label(outputFrame.interior, text="First name").grid(row=0, column=1)
            Label(outputFrame.interior, text="Second name").grid(row=0, column=2)
            Label(outputFrame.interior, text="Date of birth").grid(row=0, column=3)
            Label(outputFrame.interior, text="Email").grid(row=0, column=4)
            Label(outputFrame.interior, text="Address").grid(row=0, column=5)

            for i in range(1,50):

                dataWidget = Entry(outputFrame.interior)
                dataWidget.grid(row=i, column=0)
                dataWidget = Entry(outputFrame.interior)
                dataWidget.grid(row=i, column=1)
                dataWidget = Entry(outputFrame.interior)
                dataWidget.grid(row=i, column=2)
                dataWidget = Entry(outputFrame.interior)
                dataWidget.grid(row=i, column=3)
                dataWidget = Entry(outputFrame.interior)
                dataWidget.grid(row=i, column=4)
                dataWidget = Entry(outputFrame.interior)
                dataWidget.grid(row=i, column=5)
                Button(outputFrame.interior, text="edit").grid(row=i, column=6)

            outputFrame.interior.grid_columnconfigure(0, weight=1)
            outputFrame.interior.grid_columnconfigure(1, weight=1)
            outputFrame.interior.grid_columnconfigure(2, weight=1)
            outputFrame.interior.grid_columnconfigure(3, weight=1)
            outputFrame.interior.grid_columnconfigure(4, weight=1)
            outputFrame.interior.grid_columnconfigure(5, weight=1)
            # outputFrame.interior.grid_columnconfigure(6, weight=1)


            #Frame(self.frame, bg="green", height=self.height * 0.5, width=self.width)

            outputFrame.pack(side=BOTTOM)

                #place(relx=0.5, rely=0.5, anchor=N)
        elif opt == 2:
            self.__useCaseController.registerCustomer(self.getWidgetData("customerDetails"))
        else:
            GUI_NotificationHandler.raiseWarningMessg("Warning", "Option not selected")

