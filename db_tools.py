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
        return cur.fetchall()

def add_child(child_id,mother_id,father_id):
    sql_strs = ["INSERT INTO relations(relation,person_1,person_2,person_1_role,person_2_role) VALUES(1,{0},{1},2,1)".format(child_id,mother_id),
        "INSERT INTO relations(relation,person_1,person_2,person_1_role,person_2_role) VALUES(1,{0},{1},2,1)".format(child_id,father_id)]

    for sql_str in sql_strs:
        execute_sql(db_path,sql_str)

def add_marriage(husband_id,wife_id,date,loc_id):
    sql_str = "INSERT INTO relations(relation,person_1,person_2,person_1_role,person_2_role,relation_start,location) VALUES(3,{0},{1},3,4,{2},{3})".format(husband_id,wife_id,date,loc_id)
    execute_sql(db_path,sql_str)

def add_person(first,middle,last,gender,family,bdate,loc_id):
    sql_str = "INSERT INTO persons(first_name,middle_name,last_name,gender,family) VALUES({0},{1},{2},{3},{4})".format(first,last,middle,gender,family)
    execute_sql(db_path,sql_str)

    # sql_str = """SELECT * FROM persons
    #     WHERE persons.first_name={0}
    #     AND persons.middle_name={1}
    #     AND persons.last_name={2}""".format(first,middle,last)
    #
    # person_id = execute_sql(db_path,sql_str)[0]['id']
    #
    # sql_str= """INSERT INTO terminus
    #     VALUES(NULL,{0},1,{1},{2},NULL)""".format(person_id,bdate,loc_id)
    # execute_sql(db_path,sql_str)

def list_married():
    sql_str = """SELECT id, first_name, middle_name, last_name
        FROM persons
        WHERE persons.id IN (
        SELECT DISTINCT id
        FROM relations, persons
        WHERE relation = 3
        AND persons.id = relations.person_1
        OR persons.id = relations.person_2)"""
    married_list = execute_sql(db_path,sql_str)
    for person in married_list:
        print person['first_name'],person['middle_name'],person['last_name']

def list_unmarried():
    sql_str = """SELECT id, first_name, middle_name, last_name
        FROM persons
        WHERE persons.id NOT IN (
        SELECT DISTINCT id
        FROM relations, persons
        WHERE relation = 3
        AND persons.id = relations.person_1
        OR persons.id = relations.person_2)"""
    unmarried_list = execute_sql(db_path,sql_str)
    for person in unmarried_list:
        print person['first_name'],person['middle_name'],person['last_name']


def list_orphans():
    sql_str = """SELECT id,first_name,middle_name,last_name FROM persons
        WHERE persons.id NOT IN (
        SELECT DISTINCT id
        FROM persons, relations
        WHERE relations.relation = 1
        AND ((persons.id = relations.person_1
        AND relations.person_1_role !=1) OR (persons.id = relations.person_2
        AND relations.person_2_role !=1)))"""
    orphans = execute_sql(db_path,sql_str)
    for orphan in orphans:
        print orphan['first_name'],orphan['middle_name'],orphan['last_name']

def parents_of_children():
    sql_str = """SELECT id,first_name,middle_name,last_name FROM persons
        WHERE persons.id IN (
        SELECT DISTINCT id
        FROM persons, relations
        WHERE relations.relation = 1
        AND ((persons.id = relations.person_1
        AND relations.person_1_role =1) OR (persons.id = relations.person_2
        AND relations.person_2_role =1)))"""
    parents = execute_sql(db_path,sql_str)
    for parent in parents:
        print parent['first_name'],parent['middle_name'],parent['last_name']

if __name__ == '__main__':
    db_path = '/home/sam/Documents/MyRepos/genealogy/genealogy.sqlite'

    # add_child(39,5,6)
    # list_orphans()
    # add_marriage(28,29,'1950',12)
    # list_married()
    list_unmarried()
    # parents_of_children()


    # add_person(
    #     first = 'Ernest',
    #     middle = 'Wilhelm',
    #     last = 'Carlson',
    #     gender = 1,
    #     family = 2,
    #     bdate = '1893-07-24',
    #     loc_id = 16)
