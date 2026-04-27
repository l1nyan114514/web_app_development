from flask import Blueprint, request, redirect, render_template, flash, url_for

transaction_bp = Blueprint('transaction', __name__, url_prefix='/transactions')

@transaction_bp.route('/', methods=['GET'])
def index():
    """
    收支查詢清單路由
    輸入：支援 URL query parameters (start_date, end_date)
    處理邏輯：
        - 若有帶入合理的日期範圍參數，呼叫 Transaction.get_by_date_range()
        - 否則呼叫 Transaction.get_all() 取出所有紀錄
    輸出：渲染 templates/transactions/index.html
    錯誤處理：日期字串格式錯誤則設定 Flash 錯誤訊息並以無條件載入所有資料
    """
    pass

@transaction_bp.route('/new', methods=['GET'])
def new_transaction():
    """
    新增收支表單頁面
    輸入：URL query param (可帶入 type=INCOME 或 EXPENSE 以載入正確的 UI 狀態)
    處理邏輯：依據類型選擇，顯示對應的視覺提示
    輸出：渲染 templates/transactions/form.html
    """
    pass

@transaction_bp.route('/', methods=['POST'])
def create_transaction():
    """
    儲存新的收支紀錄
    輸入：來自表單的資料 (type, amount, category, transaction_date)
    處理邏輯：
        1. 驗證金額是否為正整數、日期是否合理
        2. 呼叫 Transaction.create 寫入資料庫
    輸出：Redirect 重導向至首頁以直接確認更新後的總餘額
    錯誤處理：若必填欄位空白，存放 Flash 錯誤訊息並重導向回新增頁面
    """
    pass

@transaction_bp.route('/<int:record_id>/delete', methods=['POST'])
def delete_transaction(record_id):
    """
    刪除特定收支紀錄
    輸入：Transaction 紀錄的 ID (從 URL 提供)
    處理邏輯：呼叫 Transaction.delete(record_id)
    輸出：完成後重新導向至原本的收支查詢頁面
    """
    pass
