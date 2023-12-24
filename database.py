import pymysql as db

class Database:
    def __init__(self, username, password, host, database):
        self.connection = db.connect(user=username, password=password, host=host, database=database)
        self.cursor = self.connection.cursor()

    def execute_query(self, query, params=None):
        if params:
            self.cursor.execute(query, params)
            self.commit()
        else:
            self.cursor.execute(query)
            self.commit()

    def fetchall(self):
        return self.cursor.fetchall()
    

    def commit(self):
        self.connection.commit()

    def close_cursor(self):
        self.commit()
        self.cursor.close()
 
    def close(self):
        self.cursor.close()
        self.connection.close()