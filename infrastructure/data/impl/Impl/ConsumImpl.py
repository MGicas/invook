import sqlite3
from typing import List, Optional
from co.edu.uco.invook.applicationcore.domain.resource.Consum import Consum
from ConsumRepository import ConsumRepository


class ConsumImpl(ConsumRepository):
    def __init__(self, db_path: str = "database.db"):
        self.db_path = db_path
        self._create_table()

    def _create_table(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS consum (
                    id TEXT PRIMARY KEY,
                    count INTEGER NOT NULL,
                    rfidLender TEXT NOT NULL,
                    idLender TEXT NOT NULL,
                    idMonitor TEXT NOT NULL,
                    codeSupply TEXT NOT NULL,
                    quantity INTEGER NOT NULL
                )
            """)
            conn.commit()

    def find_all(self) -> List[Consum]:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, count, rfidLender, idLender, idMonitor, codeSupply, quantity FROM consum")
            rows = cursor.fetchall()
            return [
                Consum.build(
                    consum_id=row[0],
                    count=row[1],
                    rfidLender=row[2],
                    idLender=row[3],
                    idMonitor=row[4],
                    codeSupply=row[5],
                    quantity=row[6]
                )
                for row in rows
            ]

    def save(self, consum: Consum) -> None:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO consum (id, count, rfidLender, idLender, idMonitor, codeSupply, quantity)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(id) DO UPDATE SET
                    count=excluded.count,
                    rfidLender=excluded.rfidLender,
                    idLender=excluded.idLender,
                    idMonitor=excluded.idMonitor,
                    codeSupply=excluded.codeSupply,
                    quantity=excluded.quantity
            """, (
                consum.get_id(),
                consum.get_count(),
                consum.get_rfidLender(),
                consum.get_idLender(),
                consum.get_idMonitor(),
                consum.get_codeSupply(),
                consum.get_quantity()
            ))
            conn.commit()

    def find_by_id(self, consum_id: str) -> Optional[Consum]:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id, count, rfidLender, idLender, idMonitor, codeSupply, quantity FROM consum WHERE id = ?", (consum_id,))
            row = cursor.fetchone()
            if row:
                return Consum.build(
                    consum_id=row[0],
                    count=row[1],
                    rfidLender=row[2],
                    idLender=row[3],
                    idMonitor=row[4],
                    codeSupply=row[5],
                    quantity=row[6]
                )
            return None

    def delete(self, consum_id: str) -> None:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM consum WHERE id = ?", (consum_id,))
            conn.commit()
