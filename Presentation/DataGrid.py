from tkinter import *
from Presentation.VerticalScrollableFrame import VerticalScrolledFrame


class DataGrid:
    def __init__(self, parent, height = None, width = None):
        self.__frame  = VerticalScrolledFrame(parent, height)
        self.__data   = None
        self.__labels = None

    def setData(self, data):
        self.__data = data
        return self

    def setLabels(self, labels):
        self.__labels = labels
        return self

    def getGrid(self):
        return self.__frame

    def __prepGrid(self):
        if self.__labels == None or self.__data == None:
            # error to programmer:
            raise Exception("Data Grid: labels or data unset")
        for i in range(len(self.__labels)):
            Label(self.__frame.interior, text=self.__labels[i]).grid(row=0, column=i)
        for i in range(len(self.__data)):
            entries = []
            for j in range(len(self.__data[i])):
                entries.append(Entry(self.__frame))
                entries[-1].insert(END, self.__data[i][j])
                entries[-1].grid(row=i+1, column=j)
                self.__frame.interior.grid_columnconfigure(j, weight=1)
            bttn = Button(self.__frame, text="edit")
            bttn.bind('<Return>', (lambda _: self.__editRecordCallback(bttn, entries)))
            bttn.grid(row=i+1, column=len(self.__data[i]) +1)

    def __prepLabels(self):
        for label in self.__labels:
            Label(self.__frame.interior, text=label).grid(row=0, column=1)

    def __editRecordCallback(self, button, entries):
        pass

import tkinter as tk


# class GetWidgetAttributes:
#     @staticmethod
#     def get_attributes(widget):
#         widg = widget
#         keys = widg.keys()
#         for key in keys:
#             print("Attribute: {:<20}".format(key), end=' ')
#             value = widg[key]
#             vtype = type(value)
#             print('Type: {:<30} Value: {}'.format(str(vtype), value))
#
#
# if __name__ == '__main__':
#     gw = GetWidgetAttributes()
#     # For Example, find all attributes of Tkinter Frame
#     gw.get_attributes(tk.Button(text="lol"))