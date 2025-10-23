import sqlite3

class Database:
    def __init__(self, db_name="students.db"):
        self.db_name = db_name
        self.create_table()

    def connect(self):
        return sqlite3.connect(self.db_name)

    def create_table(self):
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    pib TEXT,
                    group_number TEXT,
                    birth_date TEXT,
                    avg_real REAL,
                    avg_desired REAL
                )
            """)
            conn.commit()

    def insert_student(self, pib, group_number, birth_date, avg_real, avg_desired):
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO students (pib, group_number, birth_date, avg_real, avg_desired)
                VALUES (?, ?, ?, ?, ?)
            """, (pib, group_number, birth_date, avg_real, avg_desired))
            conn.commit()

    def update_student(self, student_id, avg_real, avg_desired):
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE students
                SET avg_real = ?, avg_desired = ?
                WHERE id = ?
            """, (avg_real, avg_desired, student_id))
            conn.commit()

    def delete_student(self, student_id):
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM students WHERE id = ?", (student_id,))
            conn.commit()

    def get_all_students(self):
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM students")
            return cursor.fetchall()