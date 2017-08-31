from db_functions import *

def list_terminus():
    sql_str = 'SELECT * FROM terminus'
    results = db.execute_sql(sql_str)
    return results

def add_birth(person_id,tdate,loc_id):
    sql_str= 'INSERT INTO terminus VALUES(NULL,{0},\'B\',\"{1}\",{2},NULL)'.format(person_id,tdate,loc_id)
    db.execute_sql(sql_str)

def add_death(person_id,tdate,loc_id):
    sql_str= 'INSERT INTO terminus VALUES(NULL,{0},\'D\',\"{1}\",{2},NULL)'.format(person_id,tdate,loc_id)
    db.execute_sql(sql_str)

def get_birth(person_id):
    sql_str= 'SELECT * FROM terminus WHERE type =\'B\' AND person ={0}'.format(person_id)
    return db.execute_sql(sql_str)

def get_death(person_id):
    sql_str= 'SELECT * FROM terminus WHERE type =\'D\' AND person ={0}'.format(person_id)
    return db.execute_sql(sql_str)
