import sqlite3
from typing import List, Optional
from co.edu.uco.invook.applicationcore.domain.inventory.Supply import Supply
from SupplyRepository import SupplyRepository

class SupplyImpl(SupplyRepository):
    def __init__(self, db_path: str = "database.db"):
        self.db_path = db_path
        self._create_table()

    def _create_table(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS supplies (
                    code TEXT PRIMARY KEY,
                    name TEXT NOT NULL,
                    description TEXT NOT NULL,
                    stock INTEGER NOT NULL
                )
            """)
            conn.commit()

    def find_all(self) -> List[Supply]:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT code, name, description, stock FROM supplies")
            rows = cursor.fetchall()
            return [Supply.build(code, name, description, stock) for (code, name, description, stock) in rows]

    def save(self, supply: Supply) -> None:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO supplies (code, name, description, stock)
                VALUES (?, ?, ?, ?)
                ON CONFLICT(code) DO UPDATE SET
                    name=excluded.name,
                    description=excluded.description,
                    stock=excluded.stock
            """, (supply.get_code(), supply.get_name(), supply.get_description(), supply.get_stock()))
            conn.commit()

    def find_by_code(self, code: str) -> Optional[Supply]:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT code, name, description, stock FROM supplies WHERE code = ?", (code,))
            row = cursor.fetchone()
            if row:
                return Supply.build(*row)
            return None

    def delete(self, code: str) -> None:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM supplies WHERE code = ?", (code,))
            conn.commit()
