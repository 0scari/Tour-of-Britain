import unittest
from unittest.mock import Mock
from BusinessLogic.CustomerManagementController import CustomerManagementController
from Data.RepositoryImplementations.CustomerManagementRepository import CustomerManagementRepository
from GUI_NotificationHandler import GUI_NotificationHandler

class CustomerManagementTestSuite(unittest.TestCase):

    def setUp(self):
        # controller with dummy repository
        self.CMC = CustomerManagementController(CustomerManagementRepository(None, None))

    def testCustomerRegistrationNameTooShort(self):
        input = {
            'name': "J",
        }
        GUI_NotificationHandler.raiseErrorMessg = Mock()
        result = self.CMC.registerCustomer(input)
        self.assertFalse(result)
        GUI_NotificationHandler.raiseErrorMessg.assert_called_once_with(
            "Validation Error", "First Name invalid")

if __name__ == '__main__':
    unittest.main()
