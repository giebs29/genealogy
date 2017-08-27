from db_functions import *

def list_locations():
    sql_str = 'SELECT * FROM locations'
    return db.execute_sql(sql_str)


def add_location(ltype=None,name=None,addr1=None,addr2=None,addr3=None,addr4=None,city=None,state=None,zip_code=None,country=None,notes=None,x=None,y=None,datum=None):
    args = [ltype,name,addr1,addr2,addr3,addr4,city,state,zip_code,country,notes,x,y,datum]
    for arg in args:
        if not arg:
            arg = ''
    sql_str = 'INSERT INTO locations(type,name,addr1,addr2,addr3,addr4,city,state,zip,country,notes,x,y,datum) VALUES(\'{0}\',\'{1}\',\'{2}\',\'{3}\',\'{4}\',\'{5}\',\'{6}\',\'{7}\',\'{8}\',\'{9}\',\'{10}\',\'{11}\',\'{12}\',\'{13}\')'.format(ltype,name,addr1,addr2,addr3,addr4,city,state,zip_code,country,notes,x,y,datum)
    db.execute_sql(sql_str)

def find_location(location_id):
    sql_str = 'SELECT * FROM locations WHERE id = {0}'.format(location_id)
    return db.execute_sql(sql_str)[0]
