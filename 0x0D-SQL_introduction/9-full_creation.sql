-- Creates a table second_table in teh database hbtn_0c_0 
-- and add multiple rows
CREATE TABLE IF NOT EXISTS second_table (
	id INT,
	name VARCHAR(256),
	score INT
);
INSERT INTO second_table
VALUES
	(1, 'Jhon', 10),
	(2, 'Alex', 3),
	(3, 'Bob', 14),
	(4, 'George', 8);