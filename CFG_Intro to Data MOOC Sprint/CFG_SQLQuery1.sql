-- Create our database. 
CREATE DATABASE Cluedo;

-- Use the correct database
USE Cluedo;
-- Create our suspects table
CREATE TABLE Suspects (
	  FullName varchar(50) NOT NULL,
      Salutation varchar(50),
      Gender varchar(1),
      Age int,
      TokenColour varchar(10)
--);

-- Insert our characters into our table
INSERT INTO Suspects
VALUES ('Scarlett', 'Miss', 'F', 42, 'Red'), 
	   ('Green', 'Reverend','M', 50, 'Green'),
       ('Mustard', 'Colonel','M', 65, 'Yellow'),
	   ('Plum', 'Professor','M', 37, 'Purple'),
	   ('Orchid', 'Doctor', 'F', 32, 'Pink'),
	   ('Peacock', 'Mrs', 'F', 35, 'Blue')

-- Display all data
SELECT * FROM Suspects;

-- Display all female characters' names
SELECT FullName
FROM Suspects
WHERE Gender = 'F';

-- Display all characters that are older than 40
SELECT *
FROM Suspects
WHERE Age > 40;