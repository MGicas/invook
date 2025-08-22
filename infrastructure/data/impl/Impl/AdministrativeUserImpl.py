import sqlite3
from typing import List, Optional
from co.edu.uco.invook.applicationcore.domain.user.AdministrativeUser import AdministrativeUser
from AdministrativeUserRepository import AdministrativeUserRepository
from co.edu.uco.invook.applicationcore.domain.user.AdministrativeUserState import AdministrativeUserState
from co.edu.uco.invook.applicationcore.domain.user.AdministrativeUserRole import AdministrativeUserRole

class AdministrativeUserImpl(AdministrativeUserRepository):

    def __init__(self, db_path: str = "app_database.db"):
        self.db_path = db_path
        self._create_table()

    def _create_table(self):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS administrative_users (
                username TEXT PRIMARY KEY,
                password TEXT NOT NULL,
                state TEXT NOT NULL,
                role TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()

    def find_all(self) -> List[AdministrativeUser]:
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT username, password, state, role FROM administrative_users")
        rows = cursor.fetchall()
        conn.close()

        return [
            AdministrativeUser(username=row[0], password=row[1],
                               state=AdministrativeUserState[row[2]],
                               role=AdministrativeUserRole[row[3]])
            for row in rows
        ]

    def save(self, user: AdministrativeUser) -> None:
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT OR REPLACE INTO administrative_users (username, password, state, role)
            VALUES (?, ?, ?, ?)
        ''', (user.get_username(), user._password, user.get_state().name, user.get_role().name))
        conn.commit()
        conn.close()

    def find_by_username(self, username: str) -> Optional[AdministrativeUser]:
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT username, password, state, role FROM administrative_users WHERE username = ?", (username,))
        row = cursor.fetchone()
        conn.close()

        if row:
            return AdministrativeUser(username=row[0], password=row[1],
                                      state=AdministrativeUserState[row[2]],
                                      role=AdministrativeUserRole[row[3]])
        return None

    def delete(self, username: str) -> None:
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM administrative_users WHERE username = ?", (username,))
        conn.commit()
        conn.close()
