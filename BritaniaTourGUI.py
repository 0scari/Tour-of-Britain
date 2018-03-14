#!/usr/bin/python
#-*- coding: utf-8 -*-
from tkinter import *
from tkinter import messagebox
from GUI_NotificationHandler import GUI_NotificationHandler
from tkinter import ttk


class BritaniaTourGUI(Frame):
    def __init__(self, sysController, duties):

        self.window = Tk()
        self.window.update()
        Frame.__init__(self, self.window)
        self.style =ttk.Style()
        self.style.theme_use("default")

        self.tabFrame = None
        self.menuFrame = None
        self.activeDutyUI = None
        self.__height = 610
        self.__width  = 1000
        self.__newTabButton = None
        self.sysController = sysController
        self.__useCaseUIs = {}

        self.__setUpWindow()
        self.__setUpMenuFrame()
        self.__setUpTabFrame()
        self.__displayMenuOptions(duties)
        self.__setDutyUIs(duties)

    def __del__(self):
        GUI_NotificationHandler.unsetGUI()

    def __setDutyUIs(self, duties):
        for i in range(len(duties["cntrlr"])):
            self.__useCaseUIs[duties["cntrlr"][i]] = []

    def __setUpWindow(self):
        self.window.geometry("%sx%s" % (self.__width, self.__height))
        self.window.configure(bg='white')
        self.window.title('Tour of Britain')
        self.window.resizable(width=FALSE, height=FALSE)

    def __setUpMenuFrame(self):
        self.menuFrame = Frame(self.window, bg="#F0F0F0", height=self.__height, width=self.__width * 0.2)
        self.menuFrame.pack_propagate(False)
        self.menuFrame.pack(side=LEFT)
        # set up label with picture
        photo = PhotoImage(file=r"menuText200x55.gif")
        label = Label(self.menuFrame, image=photo, width=200, height=38)
        label.pack(side=TOP, fill=X, pady=0)
        label.config(bg='systemTransparent')
        label.image = photo  # keep a reference!

    def __setUpTabFrame(self):
        self.tabFrame = Frame(self.window, bg="#DEDEDE", height=self.__height * 0.05, width=self.__width * 0.8)
        self.tabFrame.pack_propagate(False)
        self.tabFrame.pack(side=TOP)
        # set up label with picture
        photo = PhotoImage(file=r"newTabx29.gif")
        label = Label(self.tabFrame, image=photo, width=29, height=29,)
        label.pack(side=RIGHT)
        label.config(bg='systemTransparent')
        label.image = photo  # keep a reference!
        # set up on-click event
        label.bind("<Button-1>", lambda event: self.__addDutyUI_Tab())

    def __displayMenuOptions(self, duties):

        for i in range(len(duties["cntrlr"])):
            ttk.Button(self.menuFrame, text = duties["labels"][i], \
                   command=lambda cntrlr = duties["cntrlr"][i]: \
                       self.__displayUseCaseUIs(cntrlr)).pack(fill=X, side=TOP, padx=5, pady=3)

    def __displayUseCaseUIs(self, useCaseControllerName):
        # if an entry in the list of the Use Case UIs with the given controller name exists
        if len(self.__useCaseUIs[useCaseControllerName]) == 0:
            dutyContrlr = self.sysController.initDutyController(useCaseControllerName)
            if dutyContrlr:
                self.activeDutyUI = dutyContrlr.initDutyUI(self.window)
                self.__useCaseUIs[useCaseControllerName].append(self.activeDutyUI)
                self.__refreshTabPanel(useCaseControllerName)
        else: # Else, pick the first one
            self.__setActiveUseCaseUI(self.__useCaseUIs[useCaseControllerName][0])

    def __refreshTabPanel(self, dutyControllerName):
        self.tabFrame.destroy()
        self.__setUpTabFrame()
        for i in range(len(self.__useCaseUIs[dutyControllerName])):
            ttk.Button(self.tabFrame, command=lambda uiIndx=i:
                    self.__setActiveUseCaseUI(self.__useCaseUIs[dutyControllerName][uiIndx])).\
                pack(side=LEFT)

    def __setActiveUseCaseUI(self, dutyUI):
        self.activeDutyUI.hide()
        self.activeDutyUI = dutyUI
        self.activeDutyUI.appear(BOTTOM)

    def startGui(self):
        self.window.mainloop()

    def raiseErrorMessg(self, header, body):
        messagebox.showerror(header, body)

    def raiseWarningMessg(self, header, body):
        messagebox.showwarning(header, body)

    def raiseInfoMessg(self, header, body):
        messagebox.showinfo(header, body)


    def __addDutyUI_Tab(self):
        dutyName = self.activeDutyUI.getDutyName()
        newDutyUI = self.activeDutyUI.replicate(self.window)
        self.__useCaseUIs[dutyName].append(newDutyUI)
        b = ttk.Button(self.tabFrame, \
               command=lambda dutyUI = newDutyUI:
                self.__setActiveUseCaseUI(dutyUI)). \
            pack(side=LEFT)
