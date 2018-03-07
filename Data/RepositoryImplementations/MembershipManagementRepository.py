#!/usr/bin/python
#-*- coding: utf-8 -*-
from Data.Repositories.IMembershipManagementRepository import IMembershipManagementRepository
from BritaniaTourController import BritaniaTourController

class MembershipManagementRepository(IMembershipManagementRepository):
    def __init__(self, connection):
        super().__init__(connection)

    def write(self, customer):
        self._connection.execute('''
        INSERT INTO Customers(name, surname, dob, email, address)
          VALUES (?, ?, ?, ?, ?);
        ''', (customer.getName(),
              customer.getSurname(),
              customer.getDob(),
              customer.getEmail(),
              customer.getAddress()))

        self._connection.execute('''
        SELECT * FROM Customers;''')

        for row in self._connection:
            print(row)

        # Save (commit) the changes
            BritaniaTourController.conn.commit()

    def read(self, criteria):
        pass

