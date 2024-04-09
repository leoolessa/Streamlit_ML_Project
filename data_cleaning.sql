/*

Cleaning Data in SQL Queries

*/


BEGIN TRANSACTION;

-- Select data from the table
USE PortfolioProject;
SELECT * FROM breast_cancer;

-- Drop the 'id' column from the table
ALTER TABLE breast_cancer DROP COLUMN id;

-- Update the 'diagnosis' column
UPDATE breast_cancer
SET diagnosis =
    CASE WHEN diagnosis = 'M' THEN '1'
         WHEN diagnosis = 'B' THEN '0'
    END
FROM breast_cancer;


-- Commit the changes
COMMIT TRANSACTION;
