from db_functions import *

def list_persons():
    sql_str = 'SELECT * FROM persons'
    persons = db.execute_sql(sql_str)
    return persons

def add_person(first,middle,last,gender,family):
    # Cheack to ensure that person doesn't already exist in layer
    if person_exists(first,middle,last,gender,family):
        return False
    else:
        sql_str = 'INSERT INTO persons(first,middle,last,gender,family) VALUES(\'{0}\',\'{1}\',\'{2}\',\'{3}\',{4})'.format(first,last,middle,gender,family)
        db.execute_sql(sql_str)
        return True

def person_exists(first,middle,last,gender,family):
    sql_str = 'SELECT * FROM persons WHERE first = \'{0}\'AND middle = \'{1}\'AND last = \'{2}\'AND gender = \'{3}\'AND family = \'{4}\''.format(first,last,middle,gender,family)
    exists = db.execute_sql(sql_str)
    if exists:
        return True
    else:
        return False

def person_search(first=None,middle=None,last=None,gender=None,family=None):
    sql_str = 'SELECT * FROM persons WHERE first = \'{0}\'OR middle = \'{1}\'OR last = \'{2}\'OR gender = \'{3}\'OR family = \'{4}\''.format(first,last,middle,gender,family)
    results = db.execute_sql(sql_str)
    return results

def list_full_name(person_id):
    sql_str = 'SELECT * FROM persons WHERE id = {0}'.format(person_id)
    results = db.execute_sql(sql_str)[0]
    if results['middle']:
        name = '{0} {1} {2}'.format(results['first'],results['middle'],results['last'])
    else:
        name = '{0} {1}'.format(results['first'],results['last'])
    return name
