CREATE TABLE parents AS
  SELECT "abraham" AS parent, "barack" AS child UNION
  SELECT "abraham"          , "clinton"         UNION
  SELECT "delano"           , "herbert"         UNION
  SELECT "fillmore"         , "abraham"         UNION
  SELECT "fillmore"         , "delano"          UNION
  SELECT "fillmore"         , "grover"          UNION
  SELECT "eisenhower"       , "fillmore";

CREATE TABLE dogs AS
  SELECT "abraham" AS name, "long" AS fur, 26 AS height UNION
  SELECT "barack"         , "short"      , 52           UNION
  SELECT "clinton"        , "long"       , 47           UNION
  SELECT "delano"         , "long"       , 46           UNION
  SELECT "eisenhower"     , "short"      , 35           UNION
  SELECT "fillmore"       , "curly"      , 32           UNION
  SELECT "grover"         , "short"      , 28           UNION
  SELECT "herbert"        , "curly"      , 31;

CREATE TABLE sizes AS
  SELECT "toy" AS size, 24 AS min, 28 AS max UNION
  SELECT "mini"       , 28       , 35        UNION
  SELECT "medium"     , 35       , 45        UNION
  SELECT "standard"   , 45       , 60;

-------------------------------------------------------------
-- PLEASE DO NOT CHANGE ANY SQL STATEMENTS ABOVE THIS LINE --
-------------------------------------------------------------

-- The size of each dog
CREATE TABLE size_of_dogs AS
  SELECT name, size FROM dogs, sizes
  WHERE dogs.height > sizes.min AND dogs.height <= sizes.max;

-- All dogs with parents ordered by decreasing height of their parent
DROP TABLE IF EXISTS by_height;
CREATE TABLE by_height AS
  SELECT d1.name FROM dogs AS d1, dogs AS d2, parents
  WHERE d1.name = parents.child AND
        d2.name = parents.parent
  ORDER BY d2.height DESC;

-- SELECT dogs.height FROM dogs, parents WHERE dogs.name = parents.parent

-- Filling out this helper table is optional

DROP TABLE IF EXISTS siblings;
CREATE TABLE siblings AS
  SELECT d1.name AS siblings_name1, d2.name AS siblings_name2
  FROM dogs AS d1, dogs AS d2, parents AS p1, parents AS p2
  WHERE siblings_name1 <> siblings_name2 AND p1.child = d1.name AND p2.child = d2.name AND p1.parent = p2.parent;
--SELECT * FROM siblings;


-- Sentences about siblings that are the same size
DROP TABLE IF EXISTS sentences;
CREATE TABLE sentences AS
SELECT siblings_name1 || " and " || siblings_name2 || " are " || dz1.size || " siblings"
FROM siblings, size_of_dogs as dz1, size_of_dogs as dz2
WHERE dz1.name = siblings_name1 AND dz2.name = siblings_name2 AND dz1.size = dz2.size AND dz1.name < dz2.name order by dz2.name;
--SELECT * FROM sentences;

-- Ways to stack 4 dogs to a height of at least 170, ordered by total height
DROP TABLE IF EXISTS stacks_helper;
CREATE TABLE stacks_helper(dogs, stack_height, last_height);

INSERT INTO stacks_helper(dogs, stack_height, last_height) SELECT a.name || ", " ||  b.name || ", " || c.name || ", " ||d.name,
a.height+b.height+c.height+d.height, d.height
FROM dogs as a, dogs as b, dogs as c, dogs as d
WHERE a.name!=b.name!=c.name!=d.name AND a.height < b.height AND b.height < c.height AND c.height < d.height;

--SELECT * FROM stacks_helper;

DROP TABLE IF EXISTS stacks;
CREATE TABLE stacks AS
  SELECT dogs, stack_height FROM stacks_helper WHERE stack_height > 170
  ORDER BY stack_height;
-- SELECT * FROM stacks;
