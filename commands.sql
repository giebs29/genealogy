CREATE TABLE terminus_type(
  terminus_type_id TEXT PRIMARY KEY NOT NULL,
  terminus_type INTEGER);

INSERT INTO terminus_type VALUES('B',1);
INSERT INTO terminus_type VALUES('D',2);

CREATE TABLE terminus(
  terminus_id INTEGER PRIMARY KEY NOT NULL,
  person INTEGER,
  terminus_type TEXT,
  terminus_date TEXT,
  terminus_city TEXT,
  terminus_state TEXT,
  terminus_country TEXT,
  terminus_notes TEXT,
  FOREIGN KEY(terminus_type) REFERENCES terminus_type(terminus_type_id),
  FOREIGN KEY(person) REFERENCES persons(id));

CREATE TABLE gender_type(
  gender_id TEXT PRIMARY KEY NOT NULL,
  gender_type INTEGER);

INSERT INTO gender_type VALUES('M',1);
INSERT INTO gender_type VALUES('F',2);

CREATE TABLE families(
  family_id INTEGER PRIMARY KEY NOT NULL,
  family_name TEXT NOT NULL);

CREATE TABLE persons(
  id INTEGER PRIMARY KEY NOT NULL,
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  middle_name TEXT NOT NULL,
  gender TEXT NOT NULL,
  family INTEGER,
  FOREIGN KEY(family) REFERENCES families(family_id));

--Add family members
INSERT INTO persons VALUES(NULL,'Anders','Giebner','Henry',1,NULL);
INSERT INTO persons VALUES(NULL,'Samuel','Giebner','Henry',1,NULL);
INSERT INTO persons VALUES(NULL,'Larissa','Giebner','Brooke',2,NULL);

--Add births
INSERT INTO terminus VALUES(NULL,3,1,date('1991-03-07'),'St. Paul', 'Minnesota','USA','Needs Confirmation');
INSERT INTO terminus VALUES(NULL,2,1,date('1990-11-29'),'St. Paul', 'Minnesota','USA',NULL);
INSERT INTO terminus VALUES(NULL,1,1,date('2016-07-16'),'Duluth', 'Minnesota','USA','Premature birth. Due date was 2016-08-10.');

CREATE TABLE relationship_type(
  relationship_type_id TEXT PRIMARY KEY NOT NULL,
  relationship_type INTEGER);

INSERT INTO relationship_type VALUES('Parent/Child',1);
INSERT INTO relationship_type VALUES('Adoptive Parent/Child',2);
INSERT INTO relationship_type VALUES('Marriage',3);

CREATE TABLE relationship_roles(
  relationship_role_id TEXT PRIMARY KEY NOT NULL,
  relationship_role INTEGER);

INSERT INTO relationship_roles VALUES('Parent',1);
INSERT INTO relationship_roles VALUES('Child',2);
INSERT INTO relationship_roles VALUES('Husband',3);
INSERT INTO relationship_roles VALUES('Wife',4);

CREATE TABLE relations(
  relation_id INTEGER PRIMARY KEY NOT NULL,
  relation TEXT NOT NULL,
  person_1 INTEGER NOT NULL,
  person_2 INTEGER NOT NULL,
  person_1_role TEXT NOT NULL,
  person_2_role TEXT NOT NULL,
  relation_start TEXT,
  relation_end TEXT,
  relation_location TEXT,
  FOREIGN KEY(relation) REFERENCES relationship_type(relationship_type_id)
  FOREIGN KEY(person_1) REFERENCES persons(id),
  FOREIGN KEY(person_2) REFERENCES persons(id),
  FOREIGN KEY(person_1_role) REFERENCES relationship_roles(relationship_role_id),
  FOREIGN KEY(person_2_role) REFERENCES relationship_roles(relationship_role_id));

INSERT INTO relations VALUES(NULL,1,1,2,1,2,date('2016-07-16'),NULL,NULL);
INSERT INTO relations VALUES(NULL,1,1,3,1,2,date('2016-07-16'),NULL,NULL);
INSERT INTO relations VALUES(NULL,3,2,3,3,4,date('2013-06-08'),NULL,'Brighton Beach, Duluth, MN');

UPDATE relationship_roles
SET  relationship_role= 4
WHERE relationship_role_id = 'Wife';

--Show relations
SELECT first_name,relationship_type_id, relation_start
FROM persons, relations, relationship_type
WHERE persons.id = relations.person_2
AND relations.relation = relationship_type.relationship_type;
