.read fa17data.sql
.read sp18data.sql

-- Q2
DROP TABLE IF EXISTS obedience;
CREATE TABLE obedience AS
  SELECT seven, denero from students;

-- Q3
DROP TABLE IF EXISTS smallest_int;
CREATE TABLE smallest_int AS
  SELECT time, smallest FROM students WHERE smallest > 15 ORDER BY smallest LIMIT 20 ;

-- Q4
DROP TABLE IF EXISTS matchmaker;
CREATE TABLE matchmaker AS
  SELECT stu_a.pet, stu_a.song, stu_a.color, stu_b.color FROM students AS stu_a, students AS stu_b
  WHERE stu_a.pet = stu_b.pet AND stu_a.song = stu_b.song AND stu_a.time < stu_b.time;

-- SELECT * FROM matchmaker LIMIT 10;