CREATE DATABASE todo;
SHOW DATABASES;
USE todo;

CREATE TABLE todo_list(
	id INT AUTO_INCREMENT,
	description VARCHAR(512) NOT NULL,
	deadline DATETIME,
	PRIMARY KEY(id)
)DEFAULT CHAR SET utf8mb4;

SHOW TABLES;

DESC todo_list;

INSERT INTO todo_list
(description, deadline)

VALUES
	( "吃早餐","2022-09-23 07:59:59"),
	( "吃午餐","2022-09-23 11:59:59"),
	( "吃晚餐","2022-09-23 17:59:59"),
	( "睡觉喽","2022-09-23 22:59:59");
	
SELECT * FROM todo_list;

SELECT * 
FROM todo_list
WHERE description LIKE "%吃%"
ORDER BY deadline ASC