--Show relations
SELECT first_name,relationship_type_id, relation_start
FROM persons, relations, relationship_type
WHERE persons.id = relations.person_2
AND relations.relation = relationship_type.relationship_type;
