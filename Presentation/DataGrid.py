from tkinter import *
from Presentation.VerticalScrollableFrame import VerticalScrolledFrame


class DataGrid:
    def __init__(self, parent, height = None, width = None):
        self.__frame  = VerticalScrolledFrame(parent, height)
        self.__data   = []
        self.__labels = None

    def setData(self, data):
        self.__labels = list(data[0])
        for record in data:
            self.__data.append(list(record.values()))
        self.__prepGrid()
        return self.__frame

    def __prepGrid(self):
        if self.__labels == None or self.__data == None:
            # error to programmer:
            raise Exception("Data Grid: labels or data unset")
        for i in range(len(self.__labels)):
            Label(self.__frame.interior, text=self.__labels[i]).grid(row=0, column=i)
        for i in range(len(self.__data)):
            print(self.__data[i])
            entries = []
            for j in range(len(self.__data[i])):
                entries.append(Entry(self.__frame.interior))
                entries[-1].insert(END, self.__data[i][j])
                entries[-1].config(state=DISABLED)
                entries[-1].grid(row=i+1, column=j)
                self.__frame.interior.grid_columnconfigure(j, weight=1)
            bttn = Button(self.__frame.interior, text="edit")
            bttn.bind('<Button-1>', (lambda event, entries = entries, buttn = bttn: \
                                         self.__editRecordCallback(event, buttn, entries)))
            bttn.grid(row=i+1, column=len(self.__data[i]) +1)

    def __editRecordCallback(self, event,  button, entries):
        print(button["text"])
        if button["text"] == "edit":
            button.config(text="done")
            for entry in entries:
                entry.config(state=NORMAL)
        else:
            button.config(text="edit")
            for entry in entries:
                entry.config(state=DISABLED)
