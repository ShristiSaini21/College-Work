-- Database Setup
CREATE DATABASE IF NOT EXISTS Hospital_Cursor_Trigger_Lab;
USE Hospital_Cursor_Trigger_Lab;

-- 1. Create Tables
CREATE TABLE Doctors (
    DoctorID INT PRIMARY KEY,
    DoctorName VARCHAR(50),
    Department VARCHAR(50),
    ConsultationFee DECIMAL(10,2),
    Status VARCHAR(20)
);

CREATE TABLE Doctor_Audit (
    AuditID INT AUTO_INCREMENT PRIMARY KEY,
    DoctorID INT,
    ActionType VARCHAR(30),
    OldFee DECIMAL(10,2),
    NewFee DECIMAL(10,2),
    ActionTime TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Fee_Log (
    LogID INT AUTO_INCREMENT PRIMARY KEY,
    DoctorID INT,
    DoctorName VARCHAR(50),
    OldFee DECIMAL(10,2),
    NewFee DECIMAL(10,2),
    ChangedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Insert Dataset
INSERT INTO Doctors VALUES
(201, 'Dr. Anil', 'Cardiology', 1200, 'Active'),
(202, 'Dr. Beena', 'Pediatrics', 900, 'Active'),
(203, 'Dr. Chirag', 'Neurology', 1500, 'Active'),
(204, 'Dr. Divya', 'Dermatology', 1000, 'Active'),
(205, 'Dr. Eshan', 'Cardiology', 1300, 'Active'),
(206, 'Dr. Farah', 'Pediatrics', 850, 'Active');


--------------------------------------------------------------------------------
-- PART D: CURSORS (Q1 to Q10)
--------------------------------------------------------------------------------

-- Q1: Display DoctorID and DoctorName using Cursor
DELIMITER //
CREATE PROCEDURE Proc_DisplayDoctors()
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE v_id INT;
    DECLARE v_name VARCHAR(50);
    DECLARE cur CURSOR FOR SELECT DoctorID, DoctorName FROM Doctors;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    OPEN cur;
    read_loop: LOOP
        FETCH cur INTO v_id, v_name;
        IF done THEN
            LEAVE read_loop;
        END IF;
        SELECT v_id AS DoctorID, v_name AS DoctorName;
    END LOOP;
    CLOSE cur;
END //
DELIMITER ;
CALL Proc_DisplayDoctors();

-- Q2: Display doctors with ConsultationFee > 1000
DELIMITER //
CREATE PROCEDURE Proc_HighFeeDoctors()
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE v_name VARCHAR(50);
    DECLARE v_fee DECIMAL(10,2);
    DECLARE cur CURSOR FOR SELECT DoctorName, ConsultationFee FROM Doctors WHERE ConsultationFee > 1000;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    OPEN cur;
    read_loop: LOOP
        FETCH cur INTO v_name, v_fee;
        IF done THEN LEAVE read_loop; END IF;
        SELECT v_name AS DoctorName, v_fee AS ConsultationFee;
    END LOOP;
    CLOSE cur;
END //
DELIMITER ;
CALL Proc_HighFeeDoctors();

-- Q3: OUT parameter to calculate total ConsultationFee
DELIMITER //
CREATE PROCEDURE Proc_TotalFee(OUT total_fee DECIMAL(10,2))
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE v_fee DECIMAL(10,2);
    DECLARE sum_fee DECIMAL(10,2) DEFAULT 0;
    DECLARE cur CURSOR FOR SELECT ConsultationFee FROM Doctors;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    OPEN cur;
    read_loop: LOOP
        FETCH cur INTO v_fee;
        IF done THEN LEAVE read_loop; END IF;
        SET sum_fee = sum_fee + v_fee;
    END LOOP;
    CLOSE cur;
    SET total_fee = sum_fee;
END //
DELIMITER ;
CALL Proc_TotalFee(@result_total);
SELECT @result_total AS TotalConsultationFee;

-- Q4: OUT parameter to count Cardiology doctors
DELIMITER //
CREATE PROCEDURE Proc_CountCardiology(OUT cardio_count INT)
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE v_id INT;
    DECLARE cnt INT DEFAULT 0;
    DECLARE cur CURSOR FOR SELECT DoctorID FROM Doctors WHERE Department = 'Cardiology';
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    OPEN cur;
    read_loop: LOOP
        FETCH cur INTO v_id;
        IF done THEN LEAVE read_loop; END IF;
        SET cnt = cnt + 1;
    END LOOP;
    CLOSE cur;
    SET cardio_count = cnt;
END //
DELIMITER ;
CALL Proc_CountCardiology(@cardio_cnt);
SELECT @cardio_cnt AS CardiologyDoctorsCount;

-- Q5: Calculate average ConsultationFee with handling
DELIMITER //
CREATE PROCEDURE Proc_AvgFee(OUT avg_fee DECIMAL(10,2))
BEGIN
    DECLARE row_count INT;
    SELECT COUNT(*), AVG(ConsultationFee) INTO row_count, avg_fee FROM Doctors;
    IF row_count = 0 THEN
        SET avg_fee = 0.00;
    END IF;
END //
DELIMITER ;
CALL Proc_AvgFee(@avg_result);
SELECT @avg_result AS AverageFee;

-- Q6: Increase Pediatrics fees by 10%
DELIMITER //
CREATE PROCEDURE Proc_UpdatePediatricsFee()
BEGIN
    UPDATE Doctors SET ConsultationFee = ConsultationFee * 1.10 WHERE Department = 'Pediatrics';
END //
DELIMITER ;
CALL Proc_UpdatePediatricsFee();

-- Q7: Change Status to 'Review' for fees below 1000
DELIMITER //
CREATE PROCEDURE Proc_MarkForReview()
BEGIN
    UPDATE Doctors SET Status = 'Review' WHERE ConsultationFee < 1000;
END //
DELIMITER ;
CALL Proc_MarkForReview();

-- Q8: Cursor-based report ordered by Department and DoctorName
DELIMITER //
CREATE PROCEDURE Proc_DoctorReport()
BEGIN
    DECLARE done INT DEFAULT FALSE;
    DECLARE v_name VARCHAR(50);
    DECLARE v_dept VARCHAR(50);
    DECLARE v_fee DECIMAL(10,2);
    DECLARE cur CURSOR FOR SELECT DoctorName, Department, ConsultationFee FROM Doctors ORDER BY Department, DoctorName;
    DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

    OPEN cur;
    read_loop: LOOP
        FETCH cur INTO v_name, v_dept, v_fee;
        IF done THEN LEAVE read_loop; END IF;
        SELECT v_name AS DoctorName, v_dept AS Department, v_fee AS ConsultationFee;
    END LOOP;
    CLOSE cur;
END //
DELIMITER ;
CALL Proc_DoctorReport();

-- Q9: OUT parameter to count 'Active' status doctors
DELIMITER //
CREATE PROCEDURE Proc_CountActive(OUT active_count INT)
BEGIN
    SELECT COUNT(*) INTO active_count FROM Doctors WHERE Status = 'Active';
END //
DELIMITER ;
CALL Proc_CountActive(@active_cnt);
SELECT @active_cnt AS ActiveDoctorsCount;

-- Q10: 5% fee increase for doctors with fee >= 1200
DELIMITER //
CREATE PROCEDURE Proc_BonusHighEarners()
BEGIN
    UPDATE Doctors SET ConsultationFee = ConsultationFee * 1.05 WHERE ConsultationFee >= 1200;
END //
DELIMITER ;
CALL Proc_BonusHighEarners();


--------------------------------------------------------------------------------
-- PART E: TRIGGERS (Q1 to Q10)
--------------------------------------------------------------------------------

-- Q1: AFTER INSERT trigger on Doctors
DELIMITER //
CREATE TRIGGER trg_AfterInsertDoctor
AFTER INSERT ON Doctors
FOR EACH ROW
BEGIN
    INSERT INTO Doctor_Audit (DoctorID, ActionType, NewFee) 
    VALUES (NEW.DoctorID, 'INSERT', NEW.ConsultationFee);
END //
DELIMITER ;

-- Q2: AFTER UPDATE trigger recording OLD and NEW fees
DELIMITER //
CREATE TRIGGER trg_AfterUpdateFee
AFTER UPDATE ON Doctors
FOR EACH ROW
BEGIN
    IF OLD.ConsultationFee <> NEW.ConsultationFee THEN
        INSERT INTO Doctor_Audit (DoctorID, ActionType, OldFee, NewFee) 
        VALUES (NEW.DoctorID, 'FEE_UPDATE', OLD.ConsultationFee, NEW.ConsultationFee);
    END IF;
END //
DELIMITER ;

-- Q3: BEFORE INSERT trigger converting DoctorName to uppercase
DELIMITER //
CREATE TRIGGER trg_UpperDoctorName
BEFORE INSERT ON Doctors
FOR EACH ROW
BEGIN
    SET NEW.DoctorName = UPPER(NEW.DoctorName);
END //
DELIMITER ;

-- Q4: BEFORE INSERT trigger preventing negative fee
DELIMITER //
CREATE TRIGGER trg_CheckPositiveFeeInsert
BEFORE INSERT ON Doctors
FOR EACH ROW
BEGIN
    IF NEW.ConsultationFee < 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error: Consultation fee cannot be negative!';
    END IF;
END //
DELIMITER ;

-- Q5: AFTER DELETE trigger recording deleted details
DELIMITER //
CREATE TRIGGER trg_AfterDeleteDoctor
AFTER DELETE ON Doctors
FOR EACH ROW
BEGIN
    INSERT INTO Doctor_Audit (DoctorID, ActionType, OldFee) 
    VALUES (OLD.DoctorID, 'DELETE', OLD.ConsultationFee);
END //
DELIMITER ;

-- Q6: AFTER UPDATE trigger storing changed fee in Fee_Log
DELIMITER //
CREATE TRIGGER trg_FeeLogUpdate
AFTER UPDATE ON Doctors
FOR EACH ROW
BEGIN
    IF OLD.ConsultationFee <> NEW.ConsultationFee THEN
        INSERT INTO Fee_Log (DoctorID, DoctorName, OldFee, NewFee) 
        VALUES (NEW.DoctorID, NEW.DoctorName, OLD.ConsultationFee, NEW.ConsultationFee);
    END IF;
END //
DELIMITER ;

-- Q7: BEFORE UPDATE trigger preventing negative consultation fee
DELIMITER //
CREATE TRIGGER trg_CheckPositiveFeeUpdate
BEFORE UPDATE ON Doctors
FOR EACH ROW
BEGIN
    IF NEW.ConsultationFee < 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error: Updated consultation fee cannot be negative!';
    END IF;
END //
DELIMITER ;

-- Q8: BEFORE UPDATE trigger normalizing Status to 'Active'
DELIMITER //
CREATE TRIGGER trg_NormalizeStatus
BEFORE UPDATE ON Doctors
FOR EACH ROW
BEGIN
    IF LOWER(NEW.Status) = 'active' THEN
        SET NEW.Status = 'Active';
    END IF;
END //
DELIMITER ;

-- Q9: AFTER UPDATE trigger recording audit event when Department changes
DELIMITER //
CREATE TRIGGER trg_DeptChangeAudit
AFTER UPDATE ON Doctors
FOR EACH ROW
BEGIN
    IF OLD.Department <> NEW.Department THEN
        INSERT INTO Doctor_Audit (DoctorID, ActionType, OldFee, NewFee) 
        VALUES (NEW.DoctorID, 'DEPT_CHANGE', NULL, NULL);
    END IF;
END //
DELIMITER ;

-- Q10: Custom Trigger - Prevent zero consultation fee on Insert/Update
DELIMITER //
CREATE TRIGGER trg_ValidateNonZeroFee
BEFORE INSERT ON Doctors
FOR EACH ROW
BEGIN
    IF NEW.ConsultationFee = 0 THEN
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Error: Consultation fee cannot be zero!';
    END IF;
END //
DELIMITER ;