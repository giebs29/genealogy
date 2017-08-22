import sqlite3 as lite

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

def execute_sql(db,sql_str):
    con = lite.connect(db)
    con.row_factory = dict_factory
    with con:
        cur = con.cursor()
        cur.execute(sql_str)
        print sql_str
        return cur.fetchall()

def add_child(child_id,mother_id,father_id):
    sql_strs = ["INSERT INTO relations(type,person_1,person_2,person_1_role,person_2_role) VALUES('PC',{0},{1},'C','P')".format(child_id,mother_id),
        "INSERT INTO relations(type,person_1,person_2,person_1_role,person_2_role) VALUES('PC',{0},{1},'C',P)".format(child_id,father_id)]

    for sql_str in sql_strs:
        execute_sql(db_path,sql_str)

def add_marriage(husband_id,wife_id,date,loc_id):
    sql_str = "INSERT INTO relations(type,person_1,person_2,person_1_role,person_2_role,start,location) VALUES(M,{0},{1},3,4,{2},{3})".format(husband_id,wife_id,date,loc_id)
    execute_sql(db_path,sql_str)

def add_person(first,middle,last,gender,family,bdate,loc_id):
    sql_str = "INSERT INTO persons(first,middle,last,gender,family) VALUES(\'{0}\',\'{1}\',\'{2}\',{3},{4})".format(first,last,middle,gender,family)
    execute_sql(db_path,sql_str)

    sql_str = 'SELECT MAX(id) AS max FROM persons'

    person_id = execute_sql(db_path,sql_str)[0]['max']

    sql_str= '''INSERT INTO terminus
        VALUES(NULL,{0},1,\"{1}\",{2},NULL)'''.format(person_id,bdate,loc_id)
    execute_sql(db_path,sql_str)

def list_married():
    sql_str = """SELECT first, middle, last
        FROM persons, relations
        WHERE relations.type = 'M'
        AND persons.id IN (relations.person_1, relations.person_2)"""
    married_list = execute_sql(db_path,sql_str)
    for person in married_list:
        print person['first'],person['middle'],person['last']

def list_unmarried():
    sql_str = """SELECT DISTINCT first, middle, last
        FROM persons, relations
        WHERE persons.id NOT IN(
        SELECT persons.id
        FROM persons, relations
        WHERE relations.type = 'M'
        AND persons.id IN (relations.person_1, relations.person_2))"""
    unmarried_list = execute_sql(db_path,sql_str)
    for person in unmarried_list:
        print person['first'],person['middle'],person['last']


def list_orphans():
    sql_str = """SELECT first,middle,last
        FROM persons
        WHERE persons.id NOT IN (
        SELECT DISTINCT persons.id
        FROM persons, relations
        WHERE relations.type = 'PC'
        AND ((persons.id = relations.person_1
        AND relations.person_1_role !='P') OR (persons.id = relations.person_2
        AND relations.person_2_role !='P')))"""
    orphans = execute_sql(db_path,sql_str)
    for orphan in orphans:
        print orphan['first'],orphan['middle'],orphan['last']

def parents_of_children():
    sql_str = """SELECT first,middle,last
        FROM persons
        WHERE persons.id IN (
        SELECT DISTINCT persons.id
        FROM persons, relations
        WHERE relations.type = 'PC'
        AND ((persons.id = relations.person_1
        AND relations.person_1_role ='P') OR (persons.id = relations.person_2
        AND relations.person_2_role ='P')))"""
    parents = execute_sql(db_path,sql_str)
    for parent in parents:
        print parent['first'],parent['middle'],parent['last']

if __name__ == '__main__':
    db_path = '/home/sam/Documents/MyRepos/genealogy/genealogy.sqlite'

    add_child(39,5,6)
    list_orphans()
    # add_marriage(15,40,'2016-05-27',33)
    # list_married()
    # list_unmarried()
    # parents_of_children()


    # add_person(
    #     first = 'Kelly',
    #     middle = '',
    #     last = 'Johnson',
    #     gender = 2,
    #     family = 2,
    #     bdate = '1993-07-12',
    #     loc_id = 16)
