-- create schema
DROP SCHEMA if EXISTS stored_proc_tutorial;
CREATE SCHEMA if not exists stored_proc_tutorial;

USE stored_proc_tutorial;

-- table creation
CREATE TABLE if not exists studentMarks (stud_id SMALLINT(5) NOT NULL AUTO_INCREMENT PRIMARY KEY, total_marks INT, grade VARCHAR(5));
 
 
-- insert sample data
INSERT INTO studentMarks(total_marks, grade) 
VALUES (450, 'A'), (480, 'A+'), (490, 'A++'), 
       (440, 'B+'), (400, 'C+'), (380,'C'),
		 (250, 'D'), (200,'E'), (100,'F'),
		 (150,'F'), (220, 'E');

		
USE stored_proc_tutorial;

drop procedure if exists GetStudentData;

DELIMITER $$
CREATE PROCEDURE GetStudentData()
BEGIN
    SELECT * FROM studentMarks;
END$$
DELIMITER ;

CALL GetStudentData()