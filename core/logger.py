import sqlite3

class DeadlockLogger:
    def __init__(self, db_name="database/deadlock_logs.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS deadlocks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                processes TEXT
            )
        ''')
        self.conn.commit()

    def log_deadlock(self, processes):
        """Logs a detected deadlock into the database."""
        self.cursor.execute("INSERT INTO deadlocks (processes) VALUES (?)", (str(processes),))
        self.conn.commit()

    def fetch_logs(self):
        """Retrieves all logged deadlocks."""
        self.cursor.execute("SELECT * FROM deadlocks")
        return self.cursor.fetchall()
