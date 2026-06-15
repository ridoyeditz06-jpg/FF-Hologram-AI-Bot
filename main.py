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
    except:
        pass

# বট সচল রাখার লজিক
def keep_alive():
    while True:
        try:
            requests.get("https://ai-bot-1.onrender.com/")
        except: pass
        time.sleep(300)
threading.Thread(target=keep_alive, daemon=True).start()

HTML = """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body { background: #000; color: #fff; font-family: sans-serif; display: flex; justify-content: center; height: 100vh; margin: 0; }
        .container { width: 100%; max-width: 400px; display: flex; flex-direction: column; height: 100vh; background: #111; }
        .header { text-align: center; padding: 15px; }
        .header img { width: 100px; border-radius: 10px; border: 2px solid #007bff; }
        .box { flex: 1; padding: 15px; overflow-y: auto; }
        .menu-wrapper { padding: 10px; background: #222; }
        .menu-btn { padding: 12px; background: #333; color: white; border: 1px solid #444; width: 100%; cursor: pointer; }
        .btns, .sub-btns { display: none; grid-template-columns: 1fr 1fr; gap: 8px; margin-top: 10px; }
        button { padding: 10px; background: #007bff; border: none; color: white; border-radius: 5px; font-weight: bold; cursor: pointer; }
        .input-row { padding: 15px; display: flex; background: #111; }
        input { flex: 1; padding: 12px; border-radius: 5px; border: none; color: black; }
        .msg { margin-bottom: 10px; padding: 10px; border-radius: 10px; }
        .bot { background: #333; }
        .user { background: #007bff; align-self: flex-end; }
        .copy-btn { color: #007bff; text-decoration: underline; cursor: pointer; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <img src="https://i.ibb.co/v4h8zWp9/ds-Bg-Kft-F.jpg" alt="Logo">
            <div style="margin-top:10px; font-weight:bold;">FF Hologram Bot</div>
        </div>
        <div id="box" class="box"></div>
        <div class="menu-wrapper">
            <button class="menu-btn" onclick="toggle('btns')">☰ মেনু বক্স</button>
            <div id="btns" class="btns">
                <button onclick="send('রিভিউ ভিডিও')">রিভিউ ভিডিও</button>
                <button onclick="toggle('sub-btns')">কাস্টমার সার্ভিস</button>
                <button onclick="send('ক্রয় প্যানেল')">ক্রয় প্যানেল</button>
            </div>
            <div id="sub-btns" class="sub-btns">
                <button onclick="send('টেলিগ্রাম')">টেলিগ্রাম সাপোর্ট</button>
                <button onclick="send('হোয়াটসঅ্যাপ')">হোয়াটসঅ্যাপ সাপোর্ট</button>
            </div>
        </div>
        <div class="input-row">
            <input id="in" placeholder="লিখুন Boss...">
            <button onclick="send()">পাঠান</button>
        </div>
    </div>
    <script>
        function toggle(id) { let el = document.getElementById(id); el.style.display = (el.style.display === 'grid') ? 'none' : 'grid'; }
        function copyText(text) { navigator.clipboard.writeText(text); alert("বিকাশ নাম্বার কপি হয়েছে: " + text); }
        function send(t) {
            let m = t || document.getElementById('in').value;
            if(!m) return;
            document.getElementById('box').innerHTML += `<div class='msg user'>${m}</div>`;
            fetch('/api', {method:'POST', headers:{'Content-Type':'application/json'}, body:JSON.stringify({msg:m})})
            .then(r=>r.json()).then(d=>{
                document.getElementById('box').innerHTML += `<div class='msg bot'>${d.r}</div>`;
                document.getElementById('box').scrollTop = document.getElementById('box').scrollHeight;
            });
            document.getElementById('in').value = '';
        }
        window.onload = function() {
            document.getElementById('box').innerHTML = `<div class='msg bot'>স্বাগতম! আমাদের FF Hologram প্যানেলে আপনাকে স্বাগতম।<br><br>
            🔥 **অফার:** ৩০০ টাকায় ৬ মাস সার্ভিস!<br>
            🚀 প্যানেল নিতে 'ক্রয় প্যানেল' বাটনে ক্লিক করুন।</div>`;
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home(): return render_template_string(HTML)

@app.route('/api', methods=['POST'])
def api():
    msg = request.json.get('msg', '')
    lower_msg = msg.lower()
    
    # পেমেন্ট রিকোয়েস্ট চেক
    if 'নাম' in lower_msg and 'বিকাশ' in lower_msg and 'ট্রানজেকশন' in lower_msg:
        send_to_telegram(f"🔔 নতুন অর্ডার:\n\n{msg}")
        return jsonify({'r': "আপনার তথ্য এডমিনের কাছে পাঠানো হয়েছে!"})
    
    # মেনু রেসপন্স
    if 'টেলিগ্রাম' in lower_msg: return jsonify({'r': "টেলিগ্রাম সাপোর্ট: https://t.me/Ridoy_Official_penal"})
    if 'হোয়াটসঅ্যাপ' in lower_msg: return jsonify({'r': "হোয়াটসঅ্যাপে ক্লিক করুন: https://wa.me/qr/SIZBFCXQT2AUG1"})
    if 'ভিডিও' in lower_msg: return jsonify({'r': "রিভিউ ভিডিও: https://vt.tiktok.com/ZSQXNja3P/"})
    if 'ক্রয়' in lower_msg or 'প্যানেল' in lower_msg: 
        return jsonify({'r': "প্যানেল কিনতে:\n১. এই নাম্বারে টাকা পাঠান (ক্লিক করে কপি করুন):\n<span class='copy-btn' onclick='copyText(\"01727671230\")'>01727671230</span>\n২. নাম, বিকাশ নাম্বার (শেষ ৪ ডিজিট) ও ট্রানজেকশন আইডি লিখে পাঠান।"})
    
    return jsonify({'r': "জি Boss, আমি আপনার আদেশ পালনের জন্য প্রস্তুত। মেনু থেকে অপশন সিলেক্ট করুন।"})

if __name__ == '__main__': app.run(host='0.0.0.0', port=5000)
