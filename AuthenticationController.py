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
        duty1 = Duty("CustomerManagement", "Customer Management")
        duty2 = Duty("MembershipManagement", "Membership Management")
        duty3 = Duty("BookingsReservations", "Bookings and Reservations")
        role.addDuty(duty1)
        role.addDuty(duty2)
        role.addDuty(duty3)
        user.setRole(role)
        return user
