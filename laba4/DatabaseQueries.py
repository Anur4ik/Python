import sqlite3


class DatabaseQueries:
    def __init__(self, db_name="house_prices.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def find_indices_by_period(self, period):
        self.cursor.execute('SELECT * FROM indices WHERE period=?', (period,))
        return self.cursor.fetchall()

    def get_average_index_by_period(self):
        self.cursor.execute("""
        SELECT period, AVG(index1) AS avg_index1, AVG(index2) AS avg_index2, 
               AVG(index3) AS avg_index3, AVG(index4) AS avg_index4
        FROM indices
        GROUP BY period
        """)
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()


