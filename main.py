from flask import Flask, render_template_string, request, jsonify
import requests
import threading
import time

app = Flask(__name__)

TELEGRAM_BOT_TOKEN = "8443047294:AAHNR76KLcFYg4LGn2yXwip7y9Zf7bOJSpg"
YOUR_CHAT_ID = "8762376045" 
PANEL_GROUP_LINK = "https://t.me/Ridoy_Official_penal"

order_status = {} 

def keep_alive():
    while True:
        try: requests.get("https://ai-bot-1.onrender.com/") 
        except: pass
        time.sleep(300)
threading.Thread(target=keep_alive, daemon=True).start()

def send_to_telegram(name, num, tid, order_id):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": YOUR_CHAT_ID,
        "text": f"🔔 নতুন অর্ডার #{order_id}!\n👤 নাম: {name}\n📱 বিকাশ: {num}\n🆔 ট্রানজেকশন: {tid}",
        "reply_markup": {"inline_keyboard": [[
            {"text": "✅ এপ্রুভ", "callback_data": f"approve_{order_id}"},
            {"text": "❌ রিজেক্ট", "callback_data": f"reject_{order_id}"}
        ]]}
    }
    requests.post(url, json=payload)

def bot_listener():
    last_update_id = 0
    while True:
        try:
            url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/getUpdates?offset={last_update_id + 1}"
            r = requests.get(url).json()
            if r.get('result'):
                for update in r['result']:
                    last_update_id = update['update_id']
                    if 'callback_query' in update:
                        data = update['callback_query']['data']
                        order_id = int(data.split('_')[1])
                        if "approve_" in data: order_status[order_id] = "approved"
                        elif "reject_" in data: order_status[order_id] = "rejected"
        except: pass
        time.sleep(2)
threading.Thread(target=bot_listener, daemon=True).start()

HTML = """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body { background: url('https://i.ibb.co/dsBgKftF/5162.jpg') no-repeat center center fixed; background-size: cover; color: #fff; font-family: 'Segoe UI', sans-serif; margin: 0; display: flex; justify-content: center; height: 100vh; }
        .container { width: 100%; max-width: 400px; height: 100vh; background: rgba(0, 0, 0, 0.85); backdrop-filter: blur(15px); display: flex; flex-direction: column; }
        .sticky-header { text-align: center; padding: 20px 15px 10px; }
        .sticky-header img { width: 90px; height: 90px; border-radius: 50%; border: 3px solid #007bff; box-shadow: 0 0 15px #007bff; object-fit: cover; }
        .box { flex: 1; padding: 20px; overflow-y: auto; text-align: center; }
        .card { background: rgba(255, 255, 255, 0.08); border-radius: 15px; padding: 20px; border: 1px solid #007bff; }
        .menu-wrapper { padding: 15px; background: rgba(0,0,0,0.9); border-top: 1px solid #333; display: grid; grid-template-columns: 1fr 1fr; gap: 10px; }
        .sub-menu { display: none; grid-template-columns: 1fr; gap: 8px; margin-top: 10px; grid-column: span 2; }
        button { padding: 12px; background: #007bff; border: none; color: white; border-radius: 8px; font-weight: bold; cursor: pointer; }
        input { width: 90%; padding: 10px; margin-bottom: 10px; border-radius: 5px; border: 1px solid #444; background: #222; color: #fff; }
    </style>
</head>
<body>
    <div class="container">
        <div class="sticky-header">
            <img src="https://i.ibb.co/dsBgKftF/5162.jpg" alt="Logo">
            <h1>RIDOY RAJ</h1>
            <h2>FF HOLOGRAM PANEL</h2>
        </div>
        <div id="box" class="box">
            <div id="homeContent" class="card">
                <h2>⚡ স্বাগতম Boss ⚡</h2>
                <p>🔥 প্রফেশনাল গেমিং সলিউশনস 🔥</p>
                <div style="background: rgba(0, 123, 255, 0.2); padding: 15px; border-radius: 12px; border: 1px dashed #007bff; margin: 15px 0;">
                    <p>✅ এন্টি-ব্যান প্রোটেকশন</p><p>✅ ২৪/৭ নিরবচ্ছিন্ন সাপোর্ট</p>
                </div>
                <div style="background:#007bff; padding:10px; border-radius:10px; font-weight:bold;">৳ ৩০০ টাকা | ০৬ মাস মেয়াদী 💎</div>
            </div>
        </div>
        <div class="menu-wrapper">
            <button onclick="toggleMenu()">☰ মেনু</button>
            <button onclick="window.location.reload()">🏠 হোম</button>
            <div id="mainMenu" class="sub-menu">
                <button onclick="showOrderForm()">🛒 ক্রয় প্যানেল</button>
            </div>
        </div>
    </div>
    <script>
        function toggleMenu() { let m = document.getElementById('mainMenu'); m.style.display = (m.style.display === 'grid') ? 'none' : 'grid'; }
        function showOrderForm() {
            document.getElementById('box').innerHTML = `<div class="card"><input id="name" placeholder="আপনার নাম"><input id="num" placeholder="বিকাশ লাস্ট ৪ ডিজিট"><input id="tid" placeholder="ট্রানজেকশন আইডি"><button style="width:95%;" onclick="submitOrder()">সাবমিট করুন</button></div>`;
        }
        function submitOrder() {
            let data = { name: document.getElementById('name').value, num: document.getElementById('num').value, tid: document.getElementById('tid').value };
            document.getElementById('box').innerHTML = "<h3>এডমিন চেক করছেন, দয়া করে অপেক্ষা করুন...</h3>";
            fetch('/order', {method:'POST', headers:{'Content-Type':'application/json'}, body:JSON.stringify(data)})
            .then(r=>r.json()).then(d => {
                let check = setInterval(() => {
                    fetch('/check_status/' + d.order_id).then(r=>r.json()).then(res => {
                        if(res.status == "approved") { document.getElementById('box').innerHTML = "<h3>✅ অভিনন্দন! এই নিন আপনার লিংক: <a href='{{ PANEL_GROUP_LINK }}' style='color:yellow;'>ক্লিক করুন</a></h3>"; clearInterval(check); }
                        else if(res.status == "rejected") { document.getElementById('box').innerHTML = "<h3>❌ পেমেন্ট রিজেক্ট হয়েছে! আবার ট্রাই করুন।</h3>"; clearInterval(check); }
                    });
                }, 3000);
            });
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home(): return render_template_string(HTML, PANEL_GROUP_LINK=PANEL_GROUP_LINK)

@app.route('/order', methods=['POST'])
def order():
    d = request.json
    order_id = int(time.time())
    order_status[order_id] = "pending"
    send_to_telegram(d['name'], d['num'], d['tid'], order_id)
    return jsonify({'order_id': order_id})

@app.route('/check_status/<int:order_id>')
def check_status(order_id):
    return jsonify({'status': order_status.get(order_id, "pending")})

if __name__ == '__main__': app.run(host='0.0.0.0', port=5000)
