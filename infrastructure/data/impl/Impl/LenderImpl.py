import sqlite3
from typing import List, Optional
from co.edu.uco.invook.applicationcore.domain.user.Lender import Lender
from LenderRepository import LenderRepository

class LenderImpl(LenderRepository):

    def __init__(self, db_path: str = "app_database.db"):
        self.db_path = db_path
        self._create_table()

    def _create_table(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS lenders (
                id TEXT PRIMARY KEY,
                rfid TEXT NOT NULL,
                names TEXT NOT NULL,
                surnames TEXT NOT NULL,
                email TEXT NOT NULL,
                phone TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()

    def find_all(self) -> List[Lender]:
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT id, rfid, names, surnames, email, phone FROM lenders")
        rows = cursor.fetchall()
        conn.close()

        return [Lender(id=row[0], rfid=row[1], names=row[2], surnames=row[3], email=row[4], phone=row[5]) for row in rows]

    def save(self, lender: Lender) -> None:
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT OR REPLACE INTO lenders (id, rfid, names, surnames, email, phone)
            VALUES (?, ?, ?, ?, ?)
        ''', (lender._id, lender._rfid, lender._names, lender._surnames, lender._email, lender._phone))
        conn.commit()
        conn.close()

    def find_by_id(self, id: str) -> Optional[Lender]:
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT id, rfid, names, surnames, email, phone FROM lenders WHERE id = ?", (id,))
        row = cursor.fetchone()
        conn.close()

        if row:
            return Lender(id=row[0], name=row[1], email=row[2], phone=row[3], address=row[4])
        return None

    def delete(self, id: str) -> None:
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM lenders WHERE id = ?", (id,))
        conn.commit()
        conn.close()
