from db_functions import *
from person_tools import *

def list_relationships():
    sql_str = 'SELECT * FROM relations'
    return db.execute_sql(sql_str)

def add_child(child_id,mother_id=None,father_id=None):
    if mother_id:
        sql_str = "INSERT INTO relations(type,person_1,person_2,person_1_role,person_2_role) VALUES('PC',{0},{1},'C','P')".format(child_id,mother_id)
        db.execute_sql(sql_str)
    if father_id:
        sql_str = "INSERT INTO relations(type,person_1,person_2,person_1_role,person_2_role) VALUES('PC',{0},{1},'C','P')".format(child_id,father_id)
        db.execute_sql(sql_str)

def add_marriage(husband_id,wife_id,start_date,end_date=None,loc_id=None):
    sql_str = "INSERT INTO relations(type,person_1,person_2,person_1_role,person_2_role,start,end,location) VALUES('M',{0},{1},'H','W',\'{2}\',\'{3}\',\'{4}\')".format(husband_id,wife_id,start_date,end_date,loc_id)
    db.execute_sql(sql_str)

def list_spouses(person_id):
    sql_str = 'SELECT person_1,person_2 FROM relations WHERE type = "M" AND {0} IN (person_1,person_2)'.format(person_id)
    marriages = db.execute_sql(sql_str)
    spouses = []
    for marriage in marriages:
        if marriage['person_1'] != person_id:
            spouses.append(marriage['person_1'])
        else:
            spouses.append(marriage['person_2'])
    return spouses

def list_parents(person_id):
    parents = []
    sql_str = 'SELECT * FROM relations WHERE type = "PC" AND {0} IN (person_1,person_2)'.format(person_id)
    relations = db.execute_sql(sql_str)
    for relation in relations:
        if relation['person_1'] == person_id:
            if relation['person_1_role'] == 'C':
                parents.append(relation['person_2'])
        if relation['person_2'] == person_id:
            if relation['person_2_role'] == 'C':
                parents.append(relation['person_1'])
    return parents

def list_children(person_id):
    children = []
    sql_str = 'SELECT * FROM relations WHERE type = "PC" AND {0} IN (person_1,person_2)'.format(person_id)
    relations = db.execute_sql(sql_str)
    for relation in relations:
        if relation['person_1'] == person_id:
            if relation['person_1_role'] == 'P':
                children.append(relation['person_2'])
        if relation['person_2'] == person_id:
            if relation['person_2_role'] == 'P':
                children.append(relation['person_1'])
    return children

def list_ancestors(person_id):
    ancestors = list_parents(person_id)
    checked = []
    for ancestor in ancestors:
        if ancestor not in checked:
            for each in list_parents(ancestor):
                ancestors.append(each)
            checked.append(ancestor)
    return list(set(ancestors))

def list_decendants(person_id):
    decendants = list_children(person_id)
    checked = []
    for decendant in decendants:
        if decendant not in checked:
            for each in list_children(decendant):
                decendants.append(each)
            checked.append(decendant)
    return list(set(decendants))

def list_orphans():
    orphans = []
    for person in list_persons():
        if not list_parents(person['id']):
            orphans.append(person)
    return orphans

def list_unmarried():
    unmarried = []
    for person in list_persons():
        if not list_spouses(person['id']):
            unmarried.append(person)
    return unmarried
