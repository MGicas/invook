import sqlite3
from typing import List, Optional
from co.edu.uco.invook.applicationcore.domain.inventory.Hardware import Hardware
from co.edu.uco.invook.applicationcore.domain.inventory.HardwareState import HardwareState
from co.edu.uco.invook.applicationcore.domain.inventory.HardwareType import HardwareType
from co.edu.uco.invook.applicationcore.domain.inventory.HardwareAvailable import HardwareAvailable
from HardwareRepository import HardwareRepository


class HardwareImpl(HardwareRepository):
    def __init__(self, db_path: str = "database.db"):
        self.db_path = db_path
        self._create_table()

    def _create_table(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS hardware (
                    serial TEXT PRIMARY KEY,
                    name TEXT NOT NULL,
                    description TEXT NOT NULL,
                    comment TEXT,
                    state TEXT NOT NULL,
                    idType TEXT NOT NULL,
                    available TEXT NOT NULL
                )
            """)
            conn.commit()

    def find_all(self) -> List[Hardware]:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT serial, name, description, comment, state, idType, available FROM hardware")
            rows = cursor.fetchall()
            return [
                Hardware.build(
                    serial=row[0],
                    name=row[1],
                    description=row[2],
                    comment=row[3],
                    state=HardwareState[row[4]],
                    idType=HardwareType[row[5]],
                    available=HardwareAvailable[row[6]]
                )
                for row in rows
            ]

    def save(self, hardware: Hardware) -> None:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO hardware (serial, name, description, comment, state, idType, available)
                VALUES (?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(serial) DO UPDATE SET
                    name=excluded.name,
                    description=excluded.description,
                    comment=excluded.comment,
                    state=excluded.state,
                    idType=excluded.idType,
                    available=excluded.available
            """, (
                hardware.get_serial(),
                hardware.get_name(),
                hardware.get_description(),
                hardware.get_comment(),
                hardware.get_state().name,      
                hardware.get_idType().name,
                hardware.get_available().name
            ))
            conn.commit()

    def find_by_serial(self, serial: str) -> Optional[Hardware]:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT serial, name, description, comment, state, idType, available FROM hardware WHERE serial = ?", (serial,))
            row = cursor.fetchone()
            if row:
                return Hardware.build(
                    serial=row[0],
                    name=row[1],
                    description=row[2],
                    comment=row[3],
                    state=HardwareState[row[4]],
                    idType=HardwareType[row[5]],
                    available=HardwareAvailable[row[6]]
                )
            return None

    def delete(self, serial: str) -> None:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM hardware WHERE serial = ?", (serial,))
            conn.commit()
