from flask import Blueprint, request, redirect, render_template, flash, url_for

fixed_deduction_bp = Blueprint('fixed_deduction', __name__, url_prefix='/fixed-deductions')

@fixed_deduction_bp.route('/', methods=['GET'])
def index():
    """
    檢視所有的每月固定扣款清單
    輸入：無
    處理邏輯：呼叫 FixedDeduction.get_all() 獲取資料
    輸出：渲染 templates/fixed_deductions/index.html
    """
    pass

@fixed_deduction_bp.route('/new', methods=['GET'])
def new_fixed_deduction():
    """
    顯示新增固定扣款的表單介面
    輸入：無
    處理邏輯：無複雜邏輯
    輸出：渲染 templates/fixed_deductions/form.html
    """
    pass

@fixed_deduction_bp.route('/', methods=['POST'])
def create_fixed_deduction():
    """
    寫入新的固定扣款設定
    輸入：表單資料 (amount, category, deduct_day)
    處理邏輯：
        1. 驗證金額與 deduct_day（應介於 1 到 31）
        2. 呼叫 FixedDeduction.create 寫入設定
    輸出：重新導向至扣款清單頁面
    錯誤處理：資料不齊或範圍錯誤時，透過 flash 推播提示，重回表單輸入頁
    """
    pass

@fixed_deduction_bp.route('/<int:deduction_id>/delete', methods=['POST'])
def delete_fixed_deduction(deduction_id):
    """
    刪除指定的每月固定扣款
    輸入：FixedDeduction 對應的 ID (從 URL 解析)
    處理邏輯：呼叫 FixedDeduction.delete(deduction_id) 關閉這筆設定
    輸出：重新導向至清單首頁
    """
    pass
