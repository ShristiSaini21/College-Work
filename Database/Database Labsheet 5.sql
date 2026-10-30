-- Database Setup
CREATE DATABASE IF NOT EXISTS CollegeJoinDB;
USE CollegeJoinDB;

-- Setup: Create Tables
CREATE TABLE Departments (
    DeptID INT PRIMARY KEY,
    DeptName VARCHAR(50),
    Location VARCHAR(50)
);

CREATE TABLE Employees (
    EmpID INT PRIMARY KEY,
    EmpName VARCHAR(50),
    DeptID INT,
    Salary DECIMAL(10,2),
    City VARCHAR(50)
);

CREATE TABLE SalaryGrades (
    Grade CHAR(2) PRIMARY KEY,
    MinSalary DECIMAL(10,2),
    MaxSalary DECIMAL(10,2)
);

-- Setup: Insert Data
INSERT INTO Departments VALUES
(10, 'Computer Science', 'Block A'),
(20, 'Pharmacy', 'Block B'),
(30, 'Management', 'Block C'),
(40, 'Civil Engineering', 'Block D');

INSERT INTO Employees VALUES
(101, 'Aarav', 10, 65000, 'Delhi'),
(102, 'Priya', 20, 72000, 'Mumbai'),
(103, 'Rahul', 10, 48000, 'Delhi'),
(104, 'Sneha', 30, 91000, 'Pune'),
(105, 'Vikram', 20, 55000, 'Jaipur'),
(106, 'Neha', 50, 80000, 'Bengaluru'),
(107, 'Kabir', 30, 43000, 'Pune');

INSERT INTO SalaryGrades VALUES
('G1', 0, 49999),
('G2', 50000, 69999),
('G3', 70000, 89999),
('G4', 90000, 120000);

-- Q1: Basic Inner Join
SELECT e.EmpName, d.DeptName, d.Location
FROM Employees e
INNER JOIN Departments d ON e.DeptID = d.DeptID;

-- Q2: Employee and Department IDs
SELECT e.EmpID, e.EmpName, e.DeptID, d.DeptName
FROM Employees e
INNER JOIN Departments d ON e.DeptID = d.DeptID;

-- Q3: Join with Condition
SELECT e.EmpName, d.DeptName, e.Salary
FROM Employees e
INNER JOIN Departments d ON e.DeptID = d.DeptID
WHERE e.Salary > 60000;

-- Q4: Multiple Table Join / Selection
SELECT e.EmpName, e.Salary, d.DeptName
FROM Employees e
INNER JOIN Departments d ON e.DeptID = d.DeptID;

-- Q5: Column Aliasing in Join
SELECT e.EmpName AS Employee_Name, d.DeptName AS Department_Name
FROM Employees e
INNER JOIN Departments d ON e.DeptID = d.DeptID;

-- Q6: Equi Join with Multiple Columns
SELECT e.EmpName, e.City, d.DeptName, d.Location
FROM Employees e, Departments d
WHERE e.DeptID = d.DeptID;

-- Q7: Computer Science Filter
SELECT e.EmpName, d.DeptName
FROM Employees e
INNER JOIN Departments d ON e.DeptID = d.DeptID
WHERE d.DeptName = 'Computer Science';

-- Q8: Theta Join Greater Than
SELECT e.EmpName, e.Salary, sg.Grade, sg.MinSalary
FROM Employees e
JOIN SalaryGrades sg ON e.Salary > sg.MinSalary;

-- Q9: Theta Join Salary Range
SELECT e.EmpName, e.Salary, sg.Grade
FROM Employees e
JOIN SalaryGrades sg ON e.Salary >= sg.MinSalary AND e.Salary <= sg.MaxSalary;

-- Q10: Theta Join Less Than
SELECT e.EmpName, e.Salary, sg.Grade, sg.MaxSalary
FROM Employees e
JOIN SalaryGrades sg ON e.Salary < sg.MaxSalary;

-- Q11: Theta Join Greater Than or Equal
SELECT e.EmpName, e.Salary, sg.Grade
FROM Employees e
JOIN SalaryGrades sg ON e.Salary >= sg.MinSalary;

-- Q12: Natural Join
SELECT EmpName, DeptID, DeptName
FROM Employees
NATURAL JOIN Departments;

-- Q13: Natural Join with Filter
SELECT EmpName, DeptName, Location
FROM Employees
NATURAL JOIN Departments
WHERE Location = 'Block B';

-- Q14: Natural Join with Salary Filter
SELECT EmpName, DeptName, Salary
FROM Employees
NATURAL JOIN Departments
WHERE Salary >= 70000;

-- Q15: Inner Join ORDER BY
SELECT e.EmpName, d.DeptName, e.Salary
FROM Employees e
INNER JOIN Departments d ON e.DeptID = d.DeptID
ORDER BY e.Salary DESC;

-- Q16: DISTINCT Departments
SELECT DISTINCT d.DeptName
FROM Departments d
INNER JOIN Employees e ON d.DeptID = e.DeptID;

-- Q17: Employee Count
SELECT d.DeptName, COUNT(e.EmpID) AS EmployeeCount
FROM Departments d
INNER JOIN Employees e ON d.DeptID = e.DeptID
GROUP BY d.DeptName;

-- Q18: Average Salary
SELECT d.DeptName, AVG(e.Salary) AS AvgSalary
FROM Departments d
INNER JOIN Employees e ON d.DeptID = e.DeptID
GROUP BY d.DeptName;

-- Q19: HAVING Clause
SELECT d.DeptName, AVG(e.Salary) AS AvgSalary
FROM Departments d
INNER JOIN Employees e ON d.DeptID = e.DeptID
GROUP BY d.DeptName
HAVING AVG(e.Salary) > 60000;

-- Q20: Highest Paid Employee
SELECT e.EmpName, d.DeptName, e.Salary
FROM Employees e
INNER JOIN Departments d ON e.DeptID = d.DeptID
ORDER BY e.Salary DESC
LIMIT 1;

-- Q21: IN Condition
SELECT e.EmpName, d.DeptName
FROM Employees e
INNER JOIN Departments d ON e.DeptID = d.DeptID
WHERE d.DeptName IN ('Computer Science', 'Pharmacy');

-- Q22: City and Salary Filter
SELECT e.EmpName, e.City, e.Salary, d.DeptName
FROM Employees e
INNER JOIN Departments d ON e.DeptID = d.DeptID
WHERE e.City IN ('Delhi', 'Pune') AND e.Salary > 50000;

-- Q23: Matched Rows Observation
SELECT e.EmpID, e.EmpName, e.DeptID, d.DeptName
FROM Employees e
INNER JOIN Departments d ON e.DeptID = d.DeptID;

-- Q24: Natural Join & GROUP BY
SELECT DeptName, COUNT(EmpID) AS TotalEmployees
FROM Employees
NATURAL JOIN Departments
GROUP BY DeptName;

-- Q25: Final Challenge (Departments with Total Employee Salary > 100000)
SELECT d.DeptName, SUM(e.Salary) AS TotalSalary
FROM Departments d
INNER JOIN Employees e ON d.DeptID = e.DeptID
GROUP BY d.DeptName
HAVING SUM(e.Salary) > 100000;