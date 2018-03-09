from abc import ABC, abstractmethod

class AbstractBaseDataModel(ABC):
    @abstractmethod
    def dataToDict(self):
        pass

    @abstractmethod
    def getData(self):
        pass
