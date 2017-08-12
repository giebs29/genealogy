--terminus_type
INSERT INTO terminus_type VALUES('B',1);
INSERT INTO terminus_type VALUES('D',2);

--gender_type
INSERT INTO gender_type VALUES('M',1);
INSERT INTO gender_type VALUES('F',2);

--families
INSERT INTO families VALUES(NULL,'Giebner');
INSERT INTO families VALUES(NULL,'Carlson');
INSERT INTO families VALUES(NULL,'Johnson');
INSERT INTO families VALUES(NULL,'Rott');
INSERT INTO families VALUES(NULL,'Anderson');
INSERT INTO families VALUES(NULL,'Almile');
INSERT INTO families VALUES(NULL,'Deming');

--persons
INSERT INTO persons VALUES(NULL,'Anders','Giebner','Henry',1,1);
INSERT INTO persons VALUES(NULL,'Samuel','Giebner','Henry',1,1);
INSERT INTO persons VALUES(NULL,'Tiffany','Giebner','Autumn',2,1);
INSERT INTO persons VALUES(NULL,'Norman','Giebner','Paul',1,1);
INSERT INTO persons VALUES(NULL,'Richard','Giebner','Henry',1,1);
INSERT INTO persons VALUES(NULL,'Sandra','Giebner','J',2,NULL);
INSERT INTO persons VALUES(NULL,'Phyllis','Giebner','Louise',2,2);
INSERT INTO persons VALUES(NULL,'Joan','Carlson','Yvonne',2,2);
INSERT INTO persons VALUES(NULL,'George','Carlson','Henry',1,2);
INSERT INTO persons VALUES(NULL,'Herman','Carlson','Edwin',1,2);
INSERT INTO persons VALUES(NULL,'Herman','Carlson','Amandus',1,2);
INSERT INTO persons VALUES(NULL,'Nora','Carlson','Deming',2,7);
INSERT INTO persons VALUES(NULL,'Lois','Carlson','A',1,5);
INSERT INTO persons VALUES(NULL,'Larissa','Giebner','Brooke',2,3);
INSERT INTO persons VALUES(NULL,'Alexander','Johnson','Benjamin',1,3);
INSERT INTO persons VALUES(NULL,'Randall','Johnson','Bruce',1,3);
INSERT INTO persons VALUES(NULL,'Gary','Johnson','',1,3);
INSERT INTO persons VALUES(NULL,'Judeth','Johnson','',1,6);
INSERT INTO persons VALUES(NULL,'Mary Beth','Johnson','',2,4);
INSERT INTO persons VALUES(NULL,'Donald','Rott','Randolf',1,4);
INSERT INTO persons VALUES(NULL,'Sue','Rott','',2,NULL);

--terminus
INSERT INTO terminus VALUES(NULL,3,1,date('1991-03-07'),'St. Paul', 'Minnesota','USA','Needs Confirmation');
INSERT INTO terminus VALUES(NULL,2,1,date('1990-11-29'),'St. Paul', 'Minnesota','USA',NULL);
INSERT INTO terminus VALUES(NULL,1,1,date('2016-07-16'),'Duluth', 'Minnesota','USA','Premature birth. Due date was 2016-08-10.');

--relationship_type
INSERT INTO relationship_type VALUES('Parent/Child',1);
INSERT INTO relationship_type VALUES('Adoptive Parent/Child',2);
INSERT INTO relationship_type VALUES('Marriage',3);

--relationship_roles
INSERT INTO relationship_roles VALUES('Parent',1);
INSERT INTO relationship_roles VALUES('Child',2);
INSERT INTO relationship_roles VALUES('Husband',3);
INSERT INTO relationship_roles VALUES('Wife',4);

--relations
INSERT INTO relations VALUES(NULL,1,1,2,1,2,date('2016-07-16'),NULL,NULL);
INSERT INTO relations VALUES(NULL,1,1,3,1,2,date('2016-07-16'),NULL,NULL);
INSERT INTO relations VALUES(NULL,3,2,3,3,4,date('2013-06-08'),NULL,'Brighton Beach, Duluth, MN');
