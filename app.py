from flask import Flask, render_template, send_from_directory
import os

# 初始化 Flask 後端，指定在當前目錄尋找靜態資源與網頁模板
app = Flask(__name__, static_folder='.', template_folder='.')

@app.route('/')
def home():
    # 當瀏覽網頁時，動態渲染 index.html
    return render_template('index.html')

# ✨ 完美解決方案：當瀏覽器來偷偷要網站圖示時，正確把 favicon.ico 給它，防止它無限轉圈圈！
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(
        app.static_folder,
        'favicon.ico', 
        mimetype='image/vnd.microsoft.icon'
    )

if __name__ == '__main__':
    # 啟動本地開發伺服器
    app.run(host='127.0.0.1', port=5000, debug=True)