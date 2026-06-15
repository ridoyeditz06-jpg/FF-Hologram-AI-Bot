from flask import Flask, render_template_string, request, jsonify
import requests
import threading
import time

app = Flask(__name__)

# টেলিগ্রাম কনফিগারেশন
TELEGRAM_BOT_TOKEN = "8443047294:AAHNR76KLcFYg4LGn2yXwip7y9Zf7bOJSpg"
YOUR_CHAT_ID = "8762376045" 

def send_to_telegram(text):
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
        payload = {"chat_id": YOUR_CHAT_ID, "text": text}
        requests.post(url, json=payload)
    except: pass

# বট ২৪ ঘণ্টা সচল রাখার লজিক
def keep_alive():
    while True:
        try: requests.get("https://ai-bot-1.onrender.com/")
        except: pass
        time.sleep(300)
threading.Thread(target=keep_alive, daemon=True).start()

HTML = """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body { background: #000; color: #fff; font-family: 'Segoe UI', sans-serif; display: flex; justify-content: center; height: 100vh; margin: 0; }
        .container { width: 100%; max-width: 400px; display: flex; flex-direction: column; height: 100vh; background: radial-gradient(circle, #111 0%, #000 100%); }
        .header { text-align: center; padding: 25px 15px 10px; }
        .header img { width: 120px; height: 120px; border-radius: 50%; border: 3px solid #007bff; box-shadow: 0 0 15px #007bff; object-fit: cover; }
        .box { flex: 1; padding: 15px; overflow-y: auto; text-align: center; }
        .welcome-card { background: rgba(255, 255, 255, 0.03); border: 1px solid #333; border-radius: 15px; padding: 20px; text-align: left; }
        .features { font-size: 13px; color: #ccc; margin: 10px 0; line-height: 1.6; }
        .price-tag { display: block; background: #007bff; color: #fff; padding: 8px; border-radius: 8px; font-weight: bold; text-align: center; margin: 15px 0; }
        .input-group { display: flex; flex-direction: column; gap: 8px; padding: 10px; background: #1a1a1a; border-radius: 10px; border: 1px solid #444; }
        input { padding: 10px; border-radius: 5px; border: 1px solid #444; background: #222; color: #fff; width: 100%; box-sizing: border-box; }
        button { padding: 12px; background: #007bff; border: none; color: white; border-radius: 8px; font-weight: bold; cursor: pointer; width: 100%; margin-top: 5px; }
        .menu-wrapper { padding: 15px; background: #000; border-top: 1px solid #333; display: grid; gap: 8px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <img src="https://i.ibb.co/dsBgKftF/5162.jpg" alt="Logo">
            <h2 style="margin: 15px 0 0; color:#007bff;">FF HOLOGRAM</h2>
        </div>
        <div id="box" class="box">
            <div class="welcome-card">
                <h3 style="margin-top:0;">স্বাগতম Boss! 🚀</h3>
                <div class="features">
                    ✅ **এন্টি ব্যান & এন্টি ব্ল্যাক লিস্ট**<br>
                    ✅ **২৪/৭ নিরবচ্ছিন্ন সার্ভিস**<br>
                    ✅ **আপডেট পর্যন্ত ফুল নিশ্চয়তা**<br>
                    ✅ **কোনো সমস্যা ছাড়াই ব্যবহারযোগ্য**
                </div>
                <div class="price-tag">৳ ৩০০ টাকা | ০৬ মাস মেয়াদী</div>
            </div>
        </div>
        <div class="menu-wrapper">
            <button onclick="showOrderForm()">🛒 ক্রয় প্যানেল</button>
            <button style="background:#333;" onclick="window.location.href='https://t.me/Ridoy_Official_penal'">📢 টেলিগ্রাম সাপোর্ট</button>
        </div>
    </div>
    <script>
        function showOrderForm() {
            document.getElementById('box').innerHTML = `
            <div class="welcome-card">
                <p style="text-align:center;">বিকাশ নাম্বার (ক্লিক করে কপি করুন):<br>
                <span style="color:#007bff; font-weight:bold; cursor:pointer;" onclick="navigator.clipboard.writeText('01727671230')">01727671230</span></p>
                <div class="input-group">
                    <input id="name" placeholder="আপনার নাম">
                    <input id="num" placeholder="বিকাশ লাস্ট ৪ ডিজিট">
                    <input id="tid" placeholder="ট্রানজেকশন আইডি">
                    <button onclick="submitOrder()">সাবমিট করুন</button>
                </div>
            </div>`;
        }
        function submitOrder() {
            let name = document.getElementById('name').value;
            let num = document.getElementById('num').value;
            let tid = document.getElementById('tid').value;
            if(!name || !num || !tid) { alert("সব তথ্য পূরণ করুন!"); return; }
            
            fetch('/order', {method:'POST', headers:{'Content-Type':'application/json'}, body:JSON.stringify({name, num, tid})})
            .then(r=>r.json()).then(d => {
                document.getElementById('box').innerHTML = `<div class="welcome-card" style="text-align:center;">${d.r}</div>`;
            });
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home(): return render_template_string(HTML)

@app.route('/order', methods=['POST'])
def order():
    d = request.json
    msg = f"🔔 নতুন অর্ডার রিকোয়েস্ট:\n👤 নাম: {d['name']}\n📱 বিকাশ লাস্ট ৪ ডিজিট: {d['num']}\n🆔 ট্রানজেকশন আইডি: {d['tid']}"
    send_to_telegram(msg)
    return "✅ তথ্য সফলভাবে পাঠানো হয়েছে। এডমিন চেক করতেছেন, দয়া করে একটু অপেক্ষা করুন!"

if __name__ == '__main__': app.run(host='0.0.0.0', port=5000)
