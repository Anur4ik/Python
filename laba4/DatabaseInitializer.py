import sqlite3
class DatabaseInitializer:
    def __init__(self, db_name="house_prices.db"):
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
    def create_tables(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS indices (
            id INTEGER PRIMARY KEY,
            period TEXT NOT NULL,
            index1 REAL,
            index2 REAL,
            index3 REAL,
            index4 REAL
        )
        """)
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS periods (
            id INTEGER PRIMARY KEY,
            period TEXT NOT NULL
        )
        """)
        self.conn.commit()
    def close(self):

        self.conn.close()
if __name__ == "__main__":
    db_initializer = DatabaseInitializer()
    db_initializer.create_tables()
    db_initializer.close()

    print("База даних і таблиці успішно створені.")
