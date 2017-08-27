from db_functions import *

def list_families():
    sql_str = 'SELECT * FROM families'
    return db.execute_sql(sql_str)

def add_family(family_name):
    sql_str = "INSERT INTO families(name) VALUES(\'{0}\')".format(family_name)
    db.execute_sql(sql_str)
