#!/usr/bin/python
#-*- coding: utf-8 -*-
from tkinter import *

class BritaniaTourGUI:
    def __init__(self, sysController, duties):
        self.dutyUIs = {}
        self.window = Tk()
        self.tabFrame = None
        self.menuFrame = None
        self.activeDutyUI = None
        self.__height = 610
        self.__width  = 1000
        self.__newTabButton = None
        self.sysController = sysController

        self.__setUpWindow()

        self.__setUpMenuFrame()
        self.__setUpTabFrame()
        self.displayMenuOptions(duties)

        self.__setDutyUIs(duties)

        self.window.mainloop()

    def __setDutyUIs(self, duties):
        for i in range(len(duties["cntrlr"])):
            self.dutyUIs[duties["cntrlr"][i]] = []

    def __setUpWindow(self):
        self.window.geometry("%sx%s" % (self.__width, self.__height))
        self.window.configure(bg='white')
        self.window.title('Tour of Britain')
        self.window.resizable(width=FALSE, height=FALSE)

    def __setUpMenuFrame(self):
        self.menuFrame = Frame(self.window, bg="red", height=self.__height, width=self.__width * 0.2)
        self.menuFrame.pack_propagate(False)
        self.menuFrame.pack(side=LEFT)

    def __setUpTabFrame(self):
        self.tabFrame = Frame(self.window, bg="#7fc7ff", height=self.__height * 0.05, width=self.__width * 0.8)
        self.tabFrame.pack_propagate(False)
        self.tabFrame.pack(side=TOP)

        self.__newTabButton = Button(self.tabFrame, text="+",  \
                                     command=lambda: print(self.activeDutyUI)).pack(side=RIGHT)

    def displayMenuOptions(self, duties):

        for i in range(len(duties["cntrlr"])):
            Button(self.menuFrame, background='green', text = duties["labels"][i], \
                   command=lambda cntrlr = duties["cntrlr"][i]: \
                       self.displayDutyUI(cntrlr)).pack(fill=X, side=TOP, padx=5, pady=3)


    def displayDutyUI(self, dutyControllerName):
        print(dutyControllerName)

        if not len(self.dutyUIs[dutyControllerName]):
            dutyContrlr = self.sysController.initDutyController(dutyControllerName)
            self.dutyUIs[dutyControllerName] = dutyContrlr.initDutyUI(self.window)


        self.activeDutyUI = dutyControllerName

    def refreshTabPanel(self, dutyControllerName):
        pass

    def setActiveDutyUI(self, IDutyUI):
        pass

