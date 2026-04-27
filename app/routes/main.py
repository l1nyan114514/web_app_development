from flask import Blueprint, render_template

main_bp = Blueprint('main', __name__)

@main_bp.route('/', methods=['GET'])
def index():
    """
    首頁路由
    輸入：無
    處理邏輯：
        1. 檢查並觸發固定扣款背景新增邏輯，確保新扣款已過帳
        2. 呼叫 Transaction.get_total_balance() 計算總餘額
        3. 呼叫 Transaction.get_all() 獲取最近幾筆紀錄
    輸出：渲染 templates/main/index.html，傳入餘額與紀錄清單以呈現儀表板
    錯誤處理：若是初次使用無資料，顯示餘額為 0 與空白清單即可。
    """
    pass
