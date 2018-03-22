#!/usr/bin/python
#-*- coding: utf-8 -*-
import importlib
from abc import ABC, abstractmethod
from Presentation.AbstractUseCaseUI import AbstractUseCaseUI


class AbstractUseCaseController(ABC):
    @abstractmethod
    def _validateInput(self, input):
        pass

    @abstractmethod
    def _inputValidation(self, input):
        pass

    @abstractmethod
    def _constructDataModel(self, data):
        pass

    def initUseCaseUI(self, window):
        # get class __name substring without final "Controller" part"
        # e.g. authController => auth
        useCaseName = self.__class__.__name__[:-10]
        dutyUi = AbstractUseCaseUI.factory(useCaseName)
        return dutyUi(self, window)