from flask import Flask, render_template

# 初始化 Flask 後端，指定在當前目錄尋找靜態資源與網頁模板
app = Flask(__name__, static_folder='.', template_folder='.')

@app.route('/')
def home():
    # 當瀏覽網頁時，動態渲染整合了炫彩字體與立體按鈕的 index.html
    return render_template('index.html')

if __name__ == '__main__':
    # 啟動本地開發伺服器，通訊埠設為 5000
    app.run(host='127.0.0.1', port=5000, debug=True)