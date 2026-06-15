from flask import Flask, render_template_string, request, jsonify
import google.generativeai as genai
import threading
import time
import requests

app = Flask(__name__)
# আপনার এপিআই কি
genai.configure(api_key="AQ.Ab8RN6Ivn3B8x36GguUFwImshyvC5-kGoV9dx9DzBbLexpTkbQ")
model = genai.GenerativeModel('gemini-pro')

# --- বট ২৪ ঘণ্টা সচল রাখার কোড ---
def keep_alive():
    while True:
        try:
            # আপনার রেন্ডার লিংকটি নিচে বসান
            requests.get("https://YOUR_RENDER_URL.onrender.com/")
        except:
            pass
        time.sleep(300) # ৫ মিনিট পর পর নিজেকে পিন করবে

threading.Thread(target=keep_alive, daemon=True).start()
# ---------------------------------

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
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <img src="https://i.ibb.co/v4h8zWp9/ds-Bg-Kft-F.jpg" alt="Logo">
            <div style="margin-top:10px; font-weight:bold;">FF Hologram AI Bot</div>
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
            document.getElementById('box').innerHTML = `<div class='msg bot'>স্বাগতম Boss! আমাদের FF Hologram লোকেশন প্যানেলে আপনাকে স্বাগতম।<br><br>
            🔥 **অফার:** মাত্র ৩০০ টাকায় ৬ মাস সার্ভিস!<br>
            ✅ এন্টি-ব্যান ও এন্টি-ব্ল্যাকলিস্ট সুবিধা。<br>
            ✅ রিয়েল-টাইম লোকেশন ট্র্যাকিং ও র‍্যাঙ্ক পুশ সুবিধা。<br>
            🚀 আপডেট আসার আগ পর্যন্ত কোনো প্রবলেম ছাড়াই চলবে।<br><br>
            প্যানেল নিতে আগ্রহী হলে 'ক্রয় প্যানেল' বাটনে ক্লিক করুন।</div>`;
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home(): return render_template_string(HTML)

@app.route('/api', methods=['POST'])
def api():
    msg = request.json.get('msg', '').lower()
    
    if msg == "ridoy_raj409": return jsonify({'r': "জি Boss, আমি আপনার আদেশের অপেক্ষায় আছি!"})
    
    if 'টেলিগ্রাম' in msg: return jsonify({'r': "টেলিগ্রাম সাপোর্ট: https://t.me/Ridoy_Official_penal"})
    if 'হোয়াটসঅ্যাপ' in msg: return jsonify({'r': "হোয়াটসঅ্যাপ সাপোর্ট: https://wa.me/8801727671230"})
    if 'ভিডিও' in msg: return jsonify({'r': "রিভিউ ভিডিও: https://vt.tiktok.com/ZSQXNja3P/"})
    if 'ক্রয়' in msg or 'প্যানেল' in msg: return jsonify({'r': "আমাদের বিকাশ পার্সোনাল নাম্বার: 01727671230। টাকা পাঠানোর পর স্ক্রিনশট দিন। সতর্কতা: অন্য কাউকে টাকা দেবেন না!"})
    
    try:
        response = model.generate_content(f"You are the admin's AI assistant. User says: {msg}")
        return jsonify({'r': response.text})
    except:
        return jsonify({'r': "জি Boss, বলুন আমি কীভাবে সাহায্য করতে পারি?"})

if __name__ == '__main__': app.run(host='0.0.0.0', port=5000)
