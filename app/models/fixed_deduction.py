from app.models.db import get_db_connection

class FixedDeduction:
    @staticmethod
    def create(amount, category, deduct_day):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO fixed_deductions (amount, category, deduct_day) VALUES (?, ?, ?)",
                (amount, category, deduct_day)
            )
            conn.commit()
            return cursor.lastrowid

    @staticmethod
    def get_all():
        with get_db_connection() as conn:
            return conn.execute("SELECT * FROM fixed_deductions ORDER BY deduct_day ASC").fetchall()

    @staticmethod
    def get_by_id(deduction_id):
        with get_db_connection() as conn:
            return conn.execute("SELECT * FROM fixed_deductions WHERE id = ?", (deduction_id,)).fetchone()

    @staticmethod
    def update_last_processed(deduction_id, processed_month):
        with get_db_connection() as conn:
            conn.execute(
                "UPDATE fixed_deductions SET last_processed_month = ? WHERE id = ?",
                (processed_month, deduction_id)
            )
            conn.commit()

    @staticmethod
    def delete(deduction_id):
        with get_db_connection() as conn:
            conn.execute("DELETE FROM fixed_deductions WHERE id = ?", (deduction_id,))
            conn.commit()
