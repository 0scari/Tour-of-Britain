import unittest
from unittest.mock import Mock
from BusinessLogic.CustomerManagementController import CustomerManagementController
from Data.RepositoryImplementations.CustomerManagementRepository import CustomerManagementRepository
from GUI_NotificationHandler import GUI_NotificationHandler

class CustomerManagementTestSuite(unittest.TestCase):

    def setUp(self):
        # controller with dummy repository
        self.CMC = CustomerManagementController(CustomerManagementRepository(None, None))

    def testCustomerRegistrationFailureWrongField(self):
        wrongFieldName = 'wrongFieldName'
        input = {}
        input[wrongFieldName] = "xXx"
        GUI_NotificationHandler.raiseErrorMessg = Mock()
        result = self.CMC.registerCustomer(input)
        self.assertFalse(result)
        GUI_NotificationHandler.raiseErrorMessg.assert_called_once_with(
            "Internal Error", "Field "+wrongFieldName+"not recognised")

    def testCustomerRegistrationFailureNameTooShort(self):
        input = {'name': "J"}
        GUI_NotificationHandler.raiseErrorMessg = Mock()
        result = self.CMC.registerCustomer(input)
        self.assertFalse(result)
        GUI_NotificationHandler.raiseErrorMessg.assert_called_once_with(
            "Validation Error", "First Name invalid")

    def testCustomerRegistrationFailureSurnameTooShort(self):
        input = {'name': "John",
                 'surname': "Smith222"}
        GUI_NotificationHandler.raiseErrorMessg = Mock()
        result = self.CMC.registerCustomer(input)
        self.assertFalse(result)
        GUI_NotificationHandler.raiseErrorMessg.assert_called_once_with(
            "Validation Error", "Last Name must be alphabetic")

    def testCustomerRegistrationFailureDobIncomplete(self):
        """
        Testing whether the registration will fail due to
        wrong number of values for date of birth
        """
        input = {'name': "John",
                 'surname': "Smith",
                 'dobDD': "19", 'dobMM': "10"}
        # Mocking the behaviour of GUI_NotificationHandler
        GUI_NotificationHandler.raiseErrorMessg = Mock()
        result = self.CMC.registerCustomer(input)
        self.assertFalse(result)
        # Assert behaviour for the mocked method
        GUI_NotificationHandler.raiseErrorMessg.assert_called_once_with(
            "Validation Error", "Some part of date of birth is missing")

    def testCustomerRegistrationFailureDobNonExistent(self):
        """
        Testing whether the registration will fail due to
        specified date of birth that does not exist
        """
        input = {'name': "John",
                 'surname': "Smith",
                 'dobDD': 29, 'dobMM': 2, "dobYYYY": 1999}
        # Mocking the behaviour of GUI_NotificationHandler
        GUI_NotificationHandler.raiseErrorMessg = Mock()
        result = self.CMC.registerCustomer(input)
        self.assertFalse(result)
        # Assert behaviour for the mocked method
        GUI_NotificationHandler.raiseErrorMessg.assert_called_once_with(
            "Validation Error", "Non-existent date")

        
if __name__ == '__main__':
    unittest.main()
