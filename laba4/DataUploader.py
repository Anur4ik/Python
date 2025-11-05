import sqlite3


class DataUploader:
    def __init__(self, db_name="house_prices.db"):
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def upload_indices(self, indices):

        self.cursor.executemany('INSERT INTO indices (id, period, index1, index2, index3, index4) VALUES (?, ?, ?, ?, ?, ?)',
            [(entry['ID'], entry['period'], entry['index1'], entry['index2'], entry['index3'], entry['index4']) for entry in indices]
        )
        self.conn.commit()

    def upload_periods(self, periods):

        self.cursor.executemany('INSERT INTO periods (id, period) VALUES (?, ?)',
            [(period['id'], period['period']) for period in periods]
        )
        self.conn.commit()

    def close(self):

        self.conn.close()
