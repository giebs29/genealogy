CREATE TABLE terminus_type(
  terminus_type_id TEXT PRIMARY KEY NOT NULL,
  terminus_type INTEGER);

CREATE TABLE terminus(
  terminus_id INTEGER PRIMARY KEY NOT NULL,
  person INTEGER,
  terminus_type TEXT,
  terminus_date TEXT,
  terminus_location INTEGER,
  terminus_notes TEXT,
  FOREIGN KEY(terminus_type) REFERENCES terminus_type(terminus_type_id),
  FOREIGN KEY(person) REFERENCES persons(id),
  FOREIGN KEY(terminus_location) REFERENCES locations(location_id));

CREATE TABLE gender_type(
  gender_id TEXT PRIMARY KEY NOT NULL,
  gender_type INTEGER);

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

CREATE TABLE relationship_type(
  relationship_type_id TEXT PRIMARY KEY NOT NULL,
  relationship_type INTEGER);

CREATE TABLE relationship_roles(
  relationship_role_id TEXT PRIMARY KEY NOT NULL,
  relationship_role INTEGER);

CREATE TABLE relations(
  relation_id INTEGER PRIMARY KEY NOT NULL,
  relation TEXT NOT NULL,
  person_1 INTEGER NOT NULL,
  person_2 INTEGER NOT NULL,
  person_1_role TEXT NOT NULL,
  person_2_role TEXT NOT NULL,
  relation_start TEXT,
  relation_end TEXT,
  location TEXT,
  FOREIGN KEY(relation) REFERENCES relationship_type(relationship_type_id)
  FOREIGN KEY(person_1) REFERENCES persons(id),
  FOREIGN KEY(person_2) REFERENCES persons(id),
  FOREIGN KEY(person_1_role) REFERENCES relationship_roles(relationship_role_id),
  FOREIGN KEY(person_2_role) REFERENCES relationship_roles(relationship_role_id),
  FOREIGN KEY(location) REFERENCES locations(location_id));

CREATE TABLE location_types(
  location_type_id TEXT PRIMARY KEY NOT NULL,
  location_type INTEGER);

CREATE TABLE locations(
  location_id INTEGER PRIMARY KEY NOT NULL,
  location_type INTEGER,
  name TEXT,
  addr1 TEXT,
  addr2 TEXT,
  addr3 TEXT,
  addr4 TEXT,
  city TEXT,
  state TEXT,
  zip TEXT,
  country TEXT,
  notes TEXT,
  x TEXT,
  y TEXT,
  datum TEXT,
  FOREIGN KEY(location_type) REFERENCES location_types(location_type_id));
