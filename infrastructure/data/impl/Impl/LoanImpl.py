import sqlite3
from typing import List, Optional
from datetime import datetime
from co.edu.uco.invook.applicationcore.domain.resource.Loan import Loan
from LoanRepository import LoanRepository
from co.edu.uco.invook.applicationcore.domain.resource.LoanStatus import LoanStatus


class LoanImpl(LoanRepository):
    def __init__(self, db_path: str = "database.db"):
        self.db_path = db_path
        self._create_table()

    def _create_table(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS loan (
                    id TEXT PRIMARY KEY,
                    count INTEGER NOT NULL,
                    rfidLender TEXT NOT NULL,
                    idLender TEXT NOT NULL,
                    idMonitor TEXT NOT NULL,
                    serialHardware TEXT NOT NULL,
                    loanDate TEXT NOT NULL,
                    returnDate TEXT NOT NULL,
                    status TEXT NOT NULL
                )
            """)
            conn.commit()

    def find_all(self) -> List[Loan]:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT id, count, rfidLender, idLender, idMonitor, serialHardware, loanDate, returnDate, status 
                FROM loan
            """)
            rows = cursor.fetchall()
            return [
                Loan.build(
                    id=row[0],
                    count=row[1],
                    rfidLender=row[2],
                    idLender=row[3],
                    idMonitor=row[4],
                    serialHardware=row[5],
                    loanDate=datetime.fromisoformat(row[6]),
                    returnDate=datetime.fromisoformat(row[7]),
                    status=LoanStatus[row[8]]
                )
                for row in rows
            ]

    def save(self, loan: Loan) -> None:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO loan (id, count, rfidLender, idLender, idMonitor, serialHardware, loanDate, returnDate, status)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(id) DO UPDATE SET
                    count=excluded.count,
                    rfidLender=excluded.rfidLender,
                    idLender=excluded.idLender,
                    idMonitor=excluded.idMonitor,
                    serialHardware=excluded.serialHardware,
                    loanDate=excluded.loanDate,
                    returnDate=excluded.returnDate,
                    status=excluded.status
            """, (
                loan.get_id(),
                loan.get_count(),
                loan.get_rfidLender(),
                loan.get_idLender(),
                loan.get_idMonitor(),
                loan.get_serialHardware(),
                loan.get_loadDate().isoformat(),
                loan.get_returnDate().isoformat(),
                loan.get_status().name
            ))
            conn.commit()

    def find_by_id(self, loan_id: str) -> Optional[Loan]:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                SELECT id, count, rfidLender, idLender, idMonitor, serialHardware, loanDate, returnDate, status 
                FROM loan WHERE id = ?
            """, (loan_id,))
            row = cursor.fetchone()
            if row:
                return Loan.build(
                    id=row[0],
                    count=row[1],
                    rfidLender=row[2],
                    idLender=row[3],
                    idMonitor=row[4],
                    serialHardware=row[5],
                    loanDate=datetime.fromisoformat(row[6]),
                    returnDate=datetime.fromisoformat(row[7]),
                    status=LoanStatus[row[8]]
                )
            return None

    def delete(self, loan_id: str) -> None:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM loan WHERE id = ?", (loan_id,))
            conn.commit()
