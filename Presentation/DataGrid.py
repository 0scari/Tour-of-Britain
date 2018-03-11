from tkinter import *
from Presentation.VerticalScrollableFrame import VerticalScrolledFrame


class DataGrid:
    def __init__(self, parent, height = None, width = None):
        self.__frame  = VerticalScrolledFrame(parent, height)
        self.__dataSet   = []
        self.__labels = None
        self.__updateRecordCallback = None

    def setDataSet(self, dataSet):
        for object in dataSet:
            self.__dataSet.append(object)
        self.__labels = list(dataSet[0].dataToDict()) # get dict keys representing field labels
        self.__prepGrid()
        return self

    def setUpdateCallback(self, callback):
        if callable(callback):
            self.__updateRecordCallback = callback
        else:
            # Exception to programmer
            raise Exception("DataGrid: update callback not callable")

    def pack(self, side):
        return self.__frame.pack(side=side)

    def __prepGrid(self):
        if self.__labels == None or self.__dataSet == None:
            # error to programmer:
            raise Exception("Data Grid: labels or data unset")
        for i in range(len(self.__labels)):
            Label(self.__frame.interior, text=self.__labels[i]).grid(row=0, column=i)
        for i in range(len(self.__dataSet)):
            entries = {}
            data = self.__dataSet[i].getData()
            columnNr = 0
            # print(data)
            for field in data:
                entries[field] = Entry(self.__frame.interior)
                entries[field].insert(END, data[field])
                entries[field].config(state=DISABLED)
                entries[field].grid(row=i+1, column=columnNr)
                self.__frame.interior.grid_columnconfigure(columnNr, weight=1)
                columnNr += 1
            bttn = Button(self.__frame.interior, text="edit")
            bttn.bind('<Button-1>', (lambda event, entries = entries, buttn = bttn: \
                                         self.__editRecordCallback(event, buttn, entries)))
            bttn.grid(row=i+1, column=len(data) + 1)

    def __editRecordCallback(self, event,  button, entries):
        if button["text"] == "edit":
            button.config(text="done")
            for key in entries:
                if key != "id" and key != "createdBy":
                    entries[key].config(state=NORMAL)
        else:
            button.config(text="edit")
            data = {}
            for key in entries:
                data[key] = entries[key].get()
                entries[key].config(state=DISABLED)
            self.__updateRecordCallback(data)

    def destruct(self):
        self.__frame.destruct()