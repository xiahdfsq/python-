
CREATE DATABASE 'school';

USE 'school'; 
 -- id: 学生的ID 
 -- name: 学生的名称
 -- nickname: 班级
 -- sex: 性别
 -- in_time: 入学时间

CREATE TABLE 'student'(
	'id' INT NOT NULL AUTO_INCREMENT PTIMARY KEY,
	'name' VARCHAR(20) NOT NULL,
	'nickname' VARCHAR(200) NOT NULL,
	'sex' CHAR(1) NULL,
	'in_time' DATETIME NULL
) DEFAULT CHARSET 'UTF-8'

INSERT INTO 'student' ('name','nickname','sex','in_time') VALUES
	('张三','kk','男',now()),
	('李四','jj','男',now()),
	('小五','hh','男',now())
;

--SELECT * FROM 'student';

--SELECT 'name','nickname' FROM 'student';

--LIMIT 从第几条数据开始 查询多少条出来

-- 0, 2
SELECT 'id','name','nickname' FROM 'student' WHERE 'sex'='男' ORDER BY 'id' DESC;



















