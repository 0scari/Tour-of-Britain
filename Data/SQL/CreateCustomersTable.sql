CREATE TABLE Customers
(
  id      INTEGER
    PRIMARY KEY,
  name    TEXT NOT NULL,
  surname TEXT NOT NULL,
  dob     TEXT NOT NULL,
  email   TEXT NOT NULL UNIQUE,
  address TEXT NOT NULL,
  employee_id INT NOT NULL,
  CONSTRAINT unq UNIQUE (name, surname, dob)
);