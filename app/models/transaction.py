from app.models.db import get_db_connection

class Transaction:
    @staticmethod
    def create(tx_type, amount, category, transaction_date):
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO transactions (type, amount, category, transaction_date) VALUES (?, ?, ?, ?)",
                (tx_type, amount, category, transaction_date)
            )
            conn.commit()
            return cursor.lastrowid

    @staticmethod
    def get_all():
        with get_db_connection() as conn:
            return conn.execute(
                "SELECT * FROM transactions ORDER BY transaction_date DESC, created_at DESC"
            ).fetchall()

    @staticmethod
    def get_by_date_range(start_date, end_date):
        with get_db_connection() as conn:
            return conn.execute(
                "SELECT * FROM transactions WHERE transaction_date >= ? AND transaction_date <= ? ORDER BY transaction_date DESC, created_at DESC",
                (start_date, end_date)
            ).fetchall()

    @staticmethod
    def get_by_id(tx_id):
        with get_db_connection() as conn:
            return conn.execute("SELECT * FROM transactions WHERE id = ?", (tx_id,)).fetchone()

    @staticmethod
    def delete(tx_id):
        with get_db_connection() as conn:
            conn.execute("DELETE FROM transactions WHERE id = ?", (tx_id,))
            conn.commit()

    @staticmethod
    def get_total_balance():
        with get_db_connection() as conn:
            # 簡化計算方式，取收入總和與支出總和
            result = conn.execute("""
                SELECT 
                    SUM(CASE WHEN type='INCOME' THEN amount ELSE 0 END) as total_income,
                    SUM(CASE WHEN type='EXPENSE' THEN amount ELSE 0 END) as total_expense
                FROM transactions
            """).fetchone()
            
            income = result['total_income'] if result['total_income'] else 0
            expense = result['total_expense'] if result['total_expense'] else 0
            return income - expense
