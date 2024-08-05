CREATE DATABASE Finance;

USE Finance;
CREATE TABLE Customers (
			 FullName varchar(50),
			 Address varchar(100),
		     Balance int,
			 Credit int,
			 Debit int
);

INSERT INTO Customers
VALUES	('Polly Moore', '123 Fake Street, Bristol, BS15BB', 10, NULL, 15),
		('Jonathan Lindfield', '1 Made up St, London, LN1 5TB', 15, NULL, 11),
		('Lewis Hendry', '1 Fictitious Avenue, Glasgow, GL1 6HH', 20, 20 , 20);

SELECT * FROM Customers;

-- SET SQL_SAFE_UPDATES = 0

UPDATE Customers
SET Balance = 20
WHERE FullName = 'Polly Moore';

SELECT * FROM Customers;

UPDATE Customers
SET Address = '22 Not Real Lane, Glasgow, GL7 5BW'
WHERE FullName = 'Lewis Hendry';

SELECT * FROM Customers;

DELETE FROM Customers
WHERE Balance = 20;

SELECT * FROM Customers;
