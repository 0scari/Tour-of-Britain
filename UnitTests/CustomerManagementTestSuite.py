import unittest
from unittest.mock import Mock
from BusinessLogic.CustomerManagementController import CustomerManagementController
from Data.RepositoryImplementations.CustomerManagementRepository import CustomerManagementRepository
from GUI_NotificationHandler import GUI_NotificationHandler
from Data.Models.Employee import Employee
from Data.Models.Duty import Duty
from Data.Models.Role import Role
from SystemController import SystemController

class CustomerManagementTestSuite(unittest.TestCase):

    def setUp(self):
        # controller with dummy repository
        self.repo = CustomerManagementRepository(None, None)
        self.CMC = CustomerManagementController(self.repo)

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

    def testCustomerRegistrationFailureEmailIncorrect(self):
        """
        Testing whether the registration will fail due to
        email not corresponding to proper format
        """
        input = {'name': "John",
                 'surname': "Smith",
                 'dobDD': 28, 'dobMM': 2, "dobYYYY": 1999,
                 'email': "smith@internet."}
        # Mocking the behaviour of GUI_NotificationHandler
        GUI_NotificationHandler.raiseErrorMessg = Mock()
        result = self.CMC.registerCustomer(input)
        self.assertFalse(result)
        # Assert behaviour for the mocked method
        GUI_NotificationHandler.raiseErrorMessg.assert_called_once_with(
            "Validation Error", "Email invalid")

    def testCustomerRegistrationFailureAddressTooShort(self):
        """
        Testing whether the registration will fail due to
        specified date of birth that does not exist
        """
        input = {'name': "John",
                 'surname': "Smith",
                 'dobDD': 28, 'dobMM': 2, "dobYYYY": 1999,
                 'email': "smith@internet.",
                 'address': "London"}
        # Mocking the behaviour of GUI_NotificationHandler
        GUI_NotificationHandler.raiseErrorMessg = Mock()
        result = self.CMC.registerCustomer(input)
        self.assertFalse(result)
        # Assert behaviour for the mocked method
        GUI_NotificationHandler.raiseErrorMessg.assert_called_once_with(
            "Validation Error", "Email invalid")

    def testCustomerRegistrationFailureDuplicateEmail(self):
        pass

    def testCustomerRegistrationFailureDuplicateUser(self):
        pass

    def testCustomerRegistrationSuccess(self):
        """
        Testing whether the registration will succeed
        with perfectly valid data
        """
        input = {'name': "John",
                 'surname': "Smith",
                 'dobDD': 28, 'dobMM': 2, "dobYYYY": 1999,
                 'email': "smith@internet.com",
                 'address': "55 London Street, Coventry, CV6 7SS"}
        # Mocking the behaviour of GUI_NotificationHandler
        GUI_NotificationHandler.raiseInfoMessg = Mock()
        # Mocking the repository
        self.repo.write = Mock()
        result = self.CMC.registerCustomer(input)
        self.assertTrue(result)
        # Assert behaviour for the mocked methods
        GUI_NotificationHandler.raiseInfoMessg.assert_called_once()
        self.repo.write.assert_called_once()

    def testCustomerRegistrationSuccessSettingEmployeeID(self):
        """
        Testing whether the registration will succeed
        with perfectly valid data and the created record
        will be associated with the currently logged in user.
        """
        input = {'name': "John",
                 'surname': "Smith",
                 'dobDD': 28, 'dobMM': 2, "dobYYYY": 1999,
                 'email': "smith@internet.com",
                 'address': "55 London Street, Coventry, CV6 7SS"}
        employee = self.createEmployee()
        SystemController._SystemController__user = employee
        # Mocking the behaviour of GUI_NotificationHandler
        GUI_NotificationHandler.raiseInfoMessg = Mock()
        self.repo.write = Mock() # Mocking the repository
        employee.getId = Mock()  # Mocking Employee id getter
        # registration call
        result = self.CMC.registerCustomer(input)
        self.assertTrue(result)
        # Assert behaviour for the mocked methods
        GUI_NotificationHandler.raiseInfoMessg.assert_called_once()
        self.repo.write.assert_called_once()
        employee.getId.assert_called_once()

    def testCustomerUpdatingSuccess(self):
        pass

    def testCustomerSearchSuccess(self):
        pass

    def testCustomerDeletionSuccess(self):
        pass

    def createEmployee(self):
        user = Employee()
        role = Role()
        role.setName("Operator")
        duty1 = Duty("CustomerManagement", "Customer Management")
        duty2 = Duty("MembershipManagement", "Membership Management")
        duty3 = Duty("BookingsReservations", "Bookings and Reservations")
        role.addDuty(duty1)
        role.addDuty(duty2)
        role.addDuty(duty3)
        user.setRole(role)
        user.setId("123")
        return user

if __name__ == '__main__':
    unittest.main()
