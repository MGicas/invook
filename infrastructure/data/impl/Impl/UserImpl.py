import sqlite3
from typing import List, Optional
from co.edu.uco.invook.applicationcore.domain.user.User import User
from UserRepository import UserRepository


class UserImpl(UserRepository):
    def __init__(self, db_path: str = "database.db"):
        self.db_path = db_path
        self._create_table()

    def _get_connection(self):
        return sqlite3.connect(self.db_path)

    def _create_table(self):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id TEXT PRIMARY KEY,
                    rfid TEXT,
                    names TEXT,
                    surnames TEXT,
                    email TEXT,
                    phone TEXT
                )
            """)
            conn.commit()

    def save(self, user: User) -> None:
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT OR REPLACE INTO users (id, rfid, names, surnames, email, phone)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (user._id, user._rfid, user._names, user._surnames, user._email, user._phone))
            conn.commit()

    def find_by_id(self, user_id: str) -> Optional[User]:
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, rfid, names, surnames, email, phone FROM users WHERE id = ?", (user_id,))
            row = cursor.fetchone()
            if row:
                return User(*row)
            return None

    def find_all(self) -> List[User]:
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, rfid, names, surnames, email, phone FROM users")
            rows = cursor.fetchall()
            return [User(*row) for row in rows]

    def delete(self, user_id: str) -> None:
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
            conn.commit()
