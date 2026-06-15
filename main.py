import requests
import google.generativeai as genai
from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

# 🔑 আপনার সিক্রেট কোড এবং টোকেন
GEMINI_API_KEY = "AQ.Ab8RN6Ivn3B8x36GguUFwImshyvC5-kGoV9dx9DzBbLexpTkbQ"
TELEGRAM_BOT_TOKEN = "8443047294:AAHNR76KLcFYg4LGn2yXwip7y9Zf7bOJSpg"
YOUR_TELEGRAM_CHAT_ID = "8762376045"
BOSS_SECRET_KEY = "RIDOY_RAJ409" # আপনার সিক্রেট কোড

# 🔗 সব লিংকসমূহ
TELEGRAM_SUPPORT_LINK = "https://t.me/Ridoy_Official_penal" 
WHATSAPP_SUPPORT_LINK = "https://wa.me/qr/SIZBFCXQT2AUG1"
PAID_GROUP_LINK = "https://t.me/+oe_rcewUi142ZmNl"
TIKTOK_REVIEW_LINK = "https://vt.tiktok.com/ZSQXNja3P/" 
BKASH_NUMBER = "01727671230"

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-pro')

# অ্যাডভান্সড চ্যাট স্ক্রিন (FF Hologram AI Bot)
HTML_TEMPLATE = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>FF Hologram AI Bot</title>
    <style>
        body {{ font-family: sans-serif; background: #f0f2f5; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }}
        .chat-container {{ width: 100%; max-width: 450px; height: 95vh; background: #fff; border-radius: 15px; box-shadow: 0 5px 25px rgba(0,0,0,0.1); display: flex; flex-direction: column; }}
        .chat-header {{ background: #007bff; color: white; padding: 15px; text-align: center; font-weight: bold; font-size: 18px; }}
        .chat-box {{ flex: 1; padding: 15px; overflow-y: auto; background: #f8f9fa; }}
        .message {{ padding: 10px 14px; border-radius: 15px; margin-bottom: 10px; font-size: 14px; word-wrap: break-word; }}
        .user-message {{ background: #007bff; color: white; align-self: flex-end; }}
        .bot-message {{ background: #e4e6eb; color: #050505; align-self: flex-start; }}
        .input-area {{ display: flex; padding: 10px; border-top: 1px solid #ddd; }}
        input {{ flex: 1; padding: 10px; border-radius: 20px; border: 1px solid #ddd; outline:none; }}
        button {{ padding: 10px 20px; border-radius: 20px; border: none; background: #007bff; color: white; margin-left: 5px; cursor: pointer; }}
    </style>
</head>
<body>
    <div class="chat-container">
        <div class="chat-header">🔥 FF Hologram AI Bot</div>
        <div id="chat-box" class="chat-box">
            <div class='message bot-message'>হ্যালো! আমি আপনার স্মার্ট অ্যাসিস্ট্যান্ট। যেকোনো বিষয় বা প্যানেল সম্পর্কে প্রশ্ন থাকলে আমাকে জানান!</div>
        </div>
        <div class="input-area">
            <input type="text" id="user-input" placeholder="লিখুন..." onkeypress="if(event.key === 'Enter') sendMessage()">
            <button onclick="sendMessage()">Send</button>
        </div>
    </div>
    <script>
        const chatBox = document.getElementById("chat-box");
        function addBotMessage(html) {{ chatBox.innerHTML += `<div class='message bot-message'>${{html}}</div>`; chatBox.scrollTop = chatBox.scrollHeight; }}
        
        async function sendMessage() {{
            const input = document.getElementById("user-input");
            if (!input.value.trim()) return;
            chatBox.innerHTML += `<div class='message user-message'>${{input.value}}</div>`;
            const msg = input.value;
            input.value = "";
            const response = await fetch('/chat-api', {{
                method: "POST", headers: {{ "Content-Type": "application/json" }},
                body: JSON.stringify({{ message: msg }})
            }});
            const data = await response.json();
            addBotMessage(data.reply);
        }}
    </script>
</body>
</html>
"""

@app.route('/', methods=['GET'])
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/chat-api', methods=['POST'])
def chat_bot():
    data = request.json
    msg = data.get("message", "").strip()
    
    # 1. Boss কে চেনার জাদুকরী লজিক
    if msg == BOSS_SECRET_KEY:
        return jsonify({"reply": "জি Boss, আপনাকে চিনতে পেরেছি! আমি আপনার সব নির্দেশ পালনের জন্য রেডি। বলুন Boss, এখন কী করতে হবে?"})
    
    # 2. সাধারণ বুদ্ধিমত্তার উত্তর (প্যানেল বা যেকোনো বিষয়ের ওপর)
    prompt = (
        f"You are a highly intelligent, witty AI assistant for FF Hologram AI Bot. "
        f"Talk naturally and logically in Bengali. "
        f"If the user asks about general topics, answer intelligently like a friend. "
        f"If the user asks about Free Fire or the location panel, highlight that our panel is 100% safe, Anti-Ban, and gives perfect location accuracy. "
        f"Customer query: {msg}"
    )
    
    try:
        reply = model.generate_content(prompt).text
    except:
        reply = "আপনার পেমেন্ট রিকোয়েস্টটি আমরা পেয়েছি, দয়া করে অপেক্ষা করুন Boss ভেরিফাই না করা পর্যন্ত।"
        
    return jsonify({"reply": reply})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
