#!/usr/bin/python
#-*- coding: utf-8 -*-
from tkinter import *

class BritaniaTourGUI:
    def __init__(self, sysController, duties):
        self.dutyUIs = None
        self.window = Tk()
        self.tabFrame = None
        self.menuFrame = None
        self.activeDutyUI = None
        self.height = 610
        self.width  = 1000
        self.sysController = sysController

        self.menuFrame = Frame(self.window, bg="red", height=self.height, width=self.width * 0.2)
        self.menuFrame.pack_propagate(False)
        self.menuFrame.pack(side=LEFT)

        self.__setUpWindow()
        self.displayMenuOptions(duties)

        self.window.mainloop()

    def __setUpWindow(self):
        self.window.geometry("%sx%s"%(self.width, self.height))
        self.window.configure(bg='white')
        self.window.title('Tour of Britain')
        self.window.resizable(width=FALSE, height=FALSE)

    def displayMenuOptions(self, duties):

        for i in range(len(duties["cntrlr"])):
            Button(self.menuFrame, background='green', text = duties["labels"][i], \
                   command=lambda cntrlr = duties["cntrlr"][i]: \
                       self.displayDutyUI(cntrlr)).pack(fill=X, side=TOP, padx=5, pady=3)


    def displayDutyUI(self, dutyControllerName):
        print(dutyControllerName)

    def refreshTabPanel(self, dutyControllerName):
        pass

    def setActiveDutyUI(self, IDutyUI):
        pass

