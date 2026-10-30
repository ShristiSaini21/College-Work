-- Database Setup
CREATE DATABASE IF NOT EXISTS CollegeDB;
USE CollegeDB;

CREATE TABLE IF NOT EXISTS Department (
    DeptID INT PRIMARY KEY,
    DeptName VARCHAR(50) NOT NULL,
    Location VARCHAR(50)
);

CREATE TABLE IF NOT EXISTS Student (
    StudentID INT PRIMARY KEY,
    StudentName VARCHAR(50) NOT NULL,
    Age INT,
    Gender VARCHAR(10),
    Marks DECIMAL(5,2),
    DeptID INT,
    Email VARCHAR(100),
    FOREIGN KEY (DeptID) REFERENCES Department (DeptID)
);

CREATE TABLE IF NOT EXISTS Course (
    CourseID INT PRIMARY KEY,
    CourseName VARCHAR(50) NOT NULL,
    Credits INT
);

INSERT INTO Department VALUES
(101, 'Computer Science', 'Block A'),
(102, 'Pharmacy', 'Block B'),
(103, 'Commerce', 'Block C'),
(104, 'Mathematics', 'Block D');

INSERT INTO Student VALUES
(1, 'Amit', 20, 'Male', 85.50, 101, 'amit@gmail.com'),
(2, 'Priya', 21, 'Female', 92.00, 102, 'priya@gmail.com'),
(3, 'Rahul', 19, 'Male', 76.50, 101, 'rahul@gmail.com'),
(4, 'Neha', 22, 'Female', 88.00, 103, 'neha@gmail.com'),
(5, 'Arjun', 20, 'Male', 69.50, 104, 'arjun@gmail.com'),
(6, 'Sneha', 21, 'Female', 95.00, 102, 'sneha@gmail.com'),
(7, 'Rohit', 23, 'Male', 72.00, 103, 'rohit@gmail.com'),
(8, 'Pooja', 20, 'Female', 81.00, 104, 'pooja@gmail.com');

INSERT INTO Course VALUES
(201, 'Database Management System', 4),
(202, 'Python Programming', 4),
(203, 'Mathematics', 3),
(204, 'Computer Networks', 3),
(205, 'Data Structures', 4);

-- PART 1: STORED PROCEDURES

-- Q1: Display All Students
DELIMITER //
CREATE PROCEDURE GetAllStudents ()
BEGIN
    SELECT * FROM Student;
END //
DELIMITER ;
CALL GetAllStudents();

-- Q4: Display Student by ID
DELIMITER //
CREATE PROCEDURE GetStudent (IN p_StudentID INT)
BEGIN
    SELECT * FROM Student WHERE StudentID = p_StudentID;
END //
DELIMITER ;
CALL GetStudent(3);

-- Q5: Display Students from a Department
DELIMITER //
CREATE PROCEDURE GetStudentsByDept (IN p_DeptID INT)
BEGIN
    SELECT * FROM Student WHERE DeptID = p_DeptID;
END //
DELIMITER ;
CALL GetStudentsByDept(102);

-- Q6: Display Students Above Given Marks
DELIMITER //
CREATE PROCEDURE StudentsAboveMarks (IN p_Marks DECIMAL(5,2))
BEGIN
    SELECT * FROM Student WHERE Marks > p_Marks;
END //
DELIMITER ;
CALL StudentsAboveMarks(80);

-- Q7: Display Total Number of Students
DELIMITER //
CREATE PROCEDURE TotalStudents()
BEGIN
    SELECT COUNT(*) AS TotalStudents FROM Student;
END //
DELIMITER ;
CALL TotalStudents();

-- Q8: Check Student Result
DELIMITER //
CREATE PROCEDURE CheckResult (IN p_StudentID INT)
BEGIN
    DECLARE v_Marks DECIMAL(5,2);
    SELECT Marks INTO v_Marks FROM Student WHERE StudentID = p_StudentID;
    IF v_Marks >= 50 THEN
        SELECT 'Pass' AS Result;
    ELSE
        SELECT 'Fail' AS Result;
    END IF;
END //
DELIMITER ;
CALL CheckResult(1);

-- Q9: Display Students of a Particular Gender
DELIMITER //
CREATE PROCEDURE GetStudentsByGender (IN p_Gender VARCHAR(10))
BEGIN
    SELECT * FROM Student WHERE Gender = p_Gender;
END //
DELIMITER ;
CALL GetStudentsByGender('Female');


-- PART 2: FUNCTIONS

-- Q11: Add Two Numbers
DELIMITER //
CREATE FUNCTION AddTwoNumbers (a INT, b INT) RETURNS INT
DETERMINISTIC
BEGIN
    RETURN a + b;
END //
DELIMITER ;
SELECT AddTwoNumbers(10, 20) AS SumResult;

-- Q12: Find Square
DELIMITER //
CREATE FUNCTION FindSquare (num INT) RETURNS INT
DETERMINISTIC
BEGIN
    RETURN num * num;
END //
DELIMITER ;
SELECT FindSquare(5) AS SquareResult;

-- Q13: Check Pass or Fail
DELIMITER //
CREATE FUNCTION ResultStatus (marks DECIMAL(5,2)) RETURNS VARCHAR(10)
DETERMINISTIC
BEGIN
    IF marks >= 50 THEN
        RETURN 'Pass';
    ELSE
        RETURN 'Fail';
    END IF;
END //
DELIMITER ;
SELECT ResultStatus(85.5) AS Status;

-- Q14: Find Student Grade
DELIMITER //
CREATE FUNCTION StudentGrade (marks DECIMAL(5,2)) RETURNS CHAR(1)
DETERMINISTIC
BEGIN
    IF marks >= 90 THEN RETURN 'A';
    ELSEIF marks >= 75 THEN RETURN 'B';
    ELSEIF marks >= 60 THEN RETURN 'C';
    ELSE RETURN 'D';
    END IF;
END //
DELIMITER ;
SELECT StudentGrade(85.5) AS Grade;

-- Q15: Find Age Category
DELIMITER //
CREATE FUNCTION AgeCategory (age INT) RETURNS VARCHAR(10)
DETERMINISTIC
BEGIN
    IF age < 21 THEN
        RETURN 'Young';
    ELSE
        RETURN 'Adult';
    END IF;
END //
DELIMITER ;
SELECT AgeCategory(20) AS Category;

-- Q18: Calculate Double Marks
DELIMITER //
CREATE FUNCTION DoubleMarks (marks DECIMAL(5,2)) RETURNS DECIMAL(5,2)
DETERMINISTIC
BEGIN
    RETURN marks * 2;
END //
DELIMITER ;
SELECT DoubleMarks(85.50) AS DoubledMarks;

-- Q19: Calculate Age After Five Years
DELIMITER //
CREATE FUNCTION AgeAfterFiveYears (current_age INT) RETURNS INT
DETERMINISTIC
BEGIN
    RETURN current_age + 5;
END //
DELIMITER ;
SELECT AgeAfterFiveYears(20) AS FutureAge;

-- Q20: Display Student Name, Marks and Grade
SELECT StudentName, Marks, StudentGrade(Marks) AS Grade
FROM Student;