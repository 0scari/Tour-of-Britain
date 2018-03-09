#!/usr/bin/python
#-*- coding: utf-8 -*-
from Data.Repositories.ICustomerManagementRepository import ICustomerManagementRepository
from SystemController import SystemController
from GUI_NotificationHandler import GUI_NotificationHandler

class CustomerManagementRepository(ICustomerManagementRepository):
    def __init__(self, connection):
        super().__init__(connection)

    def write(self, customer):
        try:
            self._connection.execute('''
            INSERT INTO Customers(name, surname, dob, email, address, employee_id)
              VALUES (?, ?, ?, ?, ?, ?);
            ''', (customer.getName(),
                  customer.getSurname(),
                  customer.getDob(),
                  customer.getEmail(),
                  customer.getAddress(),
                  customer.getCreatedBy()))

            ref = self.readCustomers({"email": customer.getEmail()})[0]["id"]

            SystemController.conn.commit()  # Save (commit) the changes
            GUI_NotificationHandler.raiseInfoMessg("Registration Success",
                                                   "Customer reference: " + str(ref))    # return the id
        except ValueError as err:
            GUI_NotificationHandler.raiseWarningMessg("DB connection failure", err)

    def readCustomers(self, conditions):
        conds = []
        for cond in conditions:
            conds.append(cond + "=" + "?")

        condition= ' AND '.join(conds)

        print(condition)

        query = "SELECT * FROM Customers WHERE " + condition
        print(query)
        values = list(conditions.values())
        self._connection.execute(query, tuple(values))

        output = []
        columNames = list(map(lambda x: x[0], self._connection.description))
        for row in self._connection:
            output.append(dict(zip(columNames, row)))

        return output

    # def read(self, conditions):
    #     pass