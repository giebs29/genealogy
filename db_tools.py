import sqlite3 as lite

def execute_sql(db,sql_str):
    con = lite.connect(db)
    with con:
        cur = con.cursor()
        cur.execute(sql_str)

def add_individual(first,last,middle=None,bday=None,bplace=None,dday=None,dplace=None,cemetary_id=None,url=None):
    sql_str = "INSERT INTO Individuals VALUES(NULL,{0},{1},{2},{3},{4},{5},{6},{7},{8})".format(
        first,last,middle,bday,bplace,dday,dplace,cemetary_id,url)
    execute_sql(db_path,sql_str)

if __name__ == '__main__':
    db_path = '/home/sam/ancestors.sqlite'

    add_individual('Bob','Barker')
