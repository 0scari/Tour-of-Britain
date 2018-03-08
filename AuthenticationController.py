from Data.Models.Employee import Employee
from Data.Models.Role import Role
from Data.Models.Duty import Duty

class AuthenticationController:
    def __init__(self):
        pass

    @staticmethod
    def login():
        user = Employee()
        role = Role()
        role.setName("Operator")
        duty1 = Duty("CustomerManagement", "Membership Management")
        duty2 = Duty("CustomerLookup", "Find a customer")
        duty3 = Duty("TripLookup", "Find a trip")
        duty4 = Duty("TripBooking", "Book a trip")
        role.addDuty(duty1)
        role.addDuty(duty2)
        role.addDuty(duty3)
        role.addDuty(duty4)
        user.setRole(role)
        return user