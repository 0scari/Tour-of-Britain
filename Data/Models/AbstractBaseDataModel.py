from abc import ABC, abstractmethod

class AbsttractBaseDataModel(ABC):
    @abstractmethod
    def getData(self):
        pass

    @abstractmethod
    def dataToDict(self):
        pass