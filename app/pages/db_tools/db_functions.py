import sqlite3 as lite

class Database():
    def __init__(self,db_path):
        self.db = db_path

    def dict_factory(self, cursor, row):
        d = {}
        for idx, col in enumerate(cursor.description):
            d[col[0]] = row[idx]
        return d

    def execute_sql(self, sql_str):
        con = lite.connect(self.db)
        con.row_factory = self.dict_factory
        with con:
            cur = con.cursor()
            cur.execute(sql_str)
            return cur.fetchall()

db_path = r"C:\Users\giebners\Documents\MyRepos\genealogy\genealogy.sqlite"
db = Database(db_path)
