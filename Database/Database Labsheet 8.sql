-- Database Setup
CREATE DATABASE IF NOT EXISTS Hospital_Functions_Lab;
USE Hospital_Functions_Lab;

-- Create Tables
CREATE TABLE Patients (
    PatientID INT PRIMARY KEY,
    PatientName VARCHAR(50),
    Age INT,
    Gender VARCHAR(10),
    WeightKg DECIMAL(5,2),
    ConsultationFee DECIMAL(10,2)
);

CREATE TABLE Medicines (
    MedicineID INT PRIMARY KEY,
    MedicineName VARCHAR(50),
    UnitPrice DECIMAL(10,2),
    Stock INT
);

-- Insert Dataset into Patients
INSERT INTO Patients VALUES
(201, 'Asha', 24, 'F', 55.5, 600),
(202, 'Rohan', 35, 'M', 72.0, 800),
(203, 'Meera', 29, 'F', 61.5, 700),
(204, 'Vivek', 46, 'M', 85.0, 1000),
(205, 'Nitin', 17, 'M', 58.0, 500),
(206, 'Kavya', 52, 'F', 68.0, 900);

-- Insert Dataset into Medicines
INSERT INTO Medicines VALUES
(301, 'Paracetamol', 25, 100),
(302, 'Amoxicillin', 80, 50),
(303, 'Cetirizine', 35, 75),
(304, 'Omeprazole', 60, 40),
(305, 'Azithromycin', 120, 25);


--------------------------------------------------------------------------------
-- PART A & B: FUNCTIONS (Q1 to Q4)
--------------------------------------------------------------------------------

-- Q1: Function to calculate BMI (Assuming a standard reference height of 1.75m)
DELIMITER //
CREATE FUNCTION calculate_bmi (weight_kg DECIMAL(5,2), height_m DECIMAL(4,2)) 
RETURNS DECIMAL(5,2)
DETERMINISTIC
BEGIN
    RETURN weight_kg / (height_m * height_m);
END //
DELIMITER ;

-- Q2: Function to return age category
DELIMITER //
CREATE FUNCTION age_category (age INT) 
RETURNS VARCHAR(10)
DETERMINISTIC
BEGIN
    IF age < 18 THEN
        RETURN 'Child';
    ELSEIF age BETWEEN 18 AND 50 THEN
        RETURN 'Adult';
    ELSE
        RETURN 'Senior';
    END IF;
END //
DELIMITER ;

-- Q3: Function to calculate consultation fee with tax
DELIMITER //
CREATE FUNCTION consultation_with_tax (fee DECIMAL(10,2), tax_percent DECIMAL(5,2)) 
RETURNS DECIMAL(10,2)
DETERMINISTIC
BEGIN
    RETURN fee + (fee * tax_percent / 100);
END //
DELIMITER ;

-- Q4: Function to calculate total medicine stock value
DELIMITER //
CREATE FUNCTION medicine_stock_value (unit_price DECIMAL(10,2), stock INT) 
RETURNS DECIMAL(10,2)
DETERMINISTIC
BEGIN
    RETURN unit_price * stock;
END //
DELIMITER ;


--------------------------------------------------------------------------------
-- STORED PROCEDURES (Q5 to Q10)
--------------------------------------------------------------------------------

-- Q5: Stored procedure to filter patients by gender
DELIMITER //
CREATE PROCEDURE patient_by_gender (IN p_gender VARCHAR(10))
BEGIN
    SELECT * FROM Patients WHERE Gender = p_gender;
END //
DELIMITER ;

-- Q6: Stored procedure to find patients above a given age
DELIMITER //
CREATE PROCEDURE patients_above_age (IN p_age INT)
BEGIN
    SELECT * FROM Patients WHERE Age > p_age;
END //
DELIMITER ;

-- Q7: Stored procedure to update medicine stock
DELIMITER //
CREATE PROCEDURE update_medicine_stock (IN p_id INT, IN p_quantity INT)
BEGIN
    UPDATE Medicines 
    SET Stock = Stock + p_quantity 
    WHERE MedicineID = p_id;
END //
DELIMITER ;

-- Q8: Stored procedure to get total medicine count via OUT parameter
DELIMITER //
CREATE PROCEDURE medicine_count (OUT p_count INT)
BEGIN
    SELECT COUNT(*) INTO p_count FROM Medicines;
END //
DELIMITER ;

-- Q9: Stored procedure for comprehensive patient report
DELIMITER //
CREATE PROCEDURE patient_report ()
BEGIN
    SELECT PatientID, PatientName, Age, Gender, WeightKg,
           calculate_bmi(WeightKg, 1.75) AS BMI, 
           age_category(Age) AS AgeCategory 
    FROM Patients;
END //
DELIMITER ;

-- Q10: Stored procedure for comprehensive medicine report with stock status
DELIMITER //
CREATE PROCEDURE medicine_report ()
BEGIN
    SELECT MedicineID, MedicineName, UnitPrice, Stock, 
           medicine_stock_value(UnitPrice, Stock) AS StockValue,
           CASE 
               WHEN Stock > 50 THEN 'Sufficient Stock'
               ELSE 'Low Stock'
           END AS StockStatus
    FROM Medicines;
END //
DELIMITER ;


--------------------------------------------------------------------------------
-- VERIFICATION & EXECUTION EXAMPLES
--------------------------------------------------------------------------------
-- Test functions:
SELECT calculate_bmi(60.0, 1.70) AS TestBMI;
SELECT age_category(30) AS TestCategory;
SELECT consultation_with_tax(800, 18) AS FeeWithTax;
SELECT medicine_stock_value(25, 100) AS StockVal;

-- Test procedures:
CALL patient_by_gender('F');
CALL patients_above_age(30);
CALL update_medicine_stock(301, 20);
CALL medicine_count(@total_meds);
SELECT @total_meds AS TotalMedicines;
CALL patient_report();
CALL medicine_report();