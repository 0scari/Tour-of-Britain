#!/usr/bin/python
#-*- coding: utf-8 -*-
from Data.Repositories.ICustomerManagementRepository import ICustomerManagementRepository
from SystemController import SystemController

class CustomerManagementRepository(ICustomerManagementRepository):
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
        SELECT id FROM Customers;''')
        SystemController.conn.commit()  # Save (commit) the changes
        return(self._connection[0])     # return the id


    def read(self, conditions):

        conds = []
        for cond in conditions:
            conds.append(cond + "=" + "?")

        condition= ' AND '.join(conds)

        print(condition)

        query = "SELECT * FROM Customers WHERE " + condition
        print(query)
        values = list(conditions.values())
        self._connection.execute(query, tuple(values))

        for row in self._connection:  # return the id
            print(row)


