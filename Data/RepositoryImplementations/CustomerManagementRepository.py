#!/usr/bin/python
#-*- coding: utf-8 -*-
from Data.Repositories.AbstractCustomerManagementRepository import AbstractCustomerManagementRepository
from SystemController import SystemController
from GUI_NotificationHandler import GUI_NotificationHandler
import sqlite3

class CustomerManagementRepository(AbstractCustomerManagementRepository):
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

            ref = self.read({"email": customer.getEmail()})[0]["id"]

            SystemController.conn.commit()  # Save (commit) the changes
            GUI_NotificationHandler.raiseInfoMessg(
                "Registration Success", "Customer reference: " + str(ref))    # return the __id
            return True
        except ValueError as err:
            GUI_NotificationHandler.raiseWarningMessg("DB connection failure", err)
            return False
        except sqlite3.IntegrityError:
            GUI_NotificationHandler.raiseWarningMessg(
                "Operation Failed", "Customer with the specified details already exists")
            return False

    def read(self, conditions):
        conds = []
        for cond in conditions:
            conds.append(cond + "=" + "?")

        condition= ' AND '.join(conds)

        print(condition)

        query = "SELECT * FROM Customers WHERE " + condition
        print(query)
        values = list(conditions.values())
        print(conditions, values)
        self._connection.execute(query, tuple(values))

        output = []
        columNames = list(map(lambda x: x[0], self._connection.description))
        for row in self._connection:
            output.append(dict(zip(columNames, row)))

        return output

    def update(self, customer):
        try:
            self._connection.execute('''
            UPDATE Customers SET name=?, surname=?, dob=?, email=?, address=?
            WHERE id=?;''',
                (customer.getName(),
                 customer.getSurname(),
                 customer.getDob(),
                 customer.getEmail(),
                 customer.getAddress(),
                 customer.getId()))
            SystemController.conn.commit()  # Save (commit) the changes
            return True
        except ValueError as err:
            print("DB error while updating:\n", err) # error to programmer
            return False
        except sqlite3.IntegrityError:
            GUI_NotificationHandler.raiseWarningMessg("Operation Failed",
                                                      "Customer with the specified details already exists")


    def delete(self, id):
        print(type(id))
        try:
            self._connection.execute('''
            DELETE FROM Customers WHERE id=?;''', (id,))
            SystemController.conn.commit()  # Save (commit) the changes
            return True
        except ValueError as err:
            print("DB error while deleting:\n", err) # error to programmer
            return False