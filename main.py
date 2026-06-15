from flask import Flask, render_template_string, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# আপনার জিমিনি এপিআই কি
genai.configure(api_key="AQ.Ab8RN6LTMM_3qBCIwI_TOf0f47CmLJ-Raso_Q65D0qM2Nwqx0A")
model = genai.GenerativeModel('gemini-pro')

HTML = """
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>AI Chat</title>
    <style>
        body { font-family: sans-serif; max-width: 500px; margin: 20px auto; padding: 10px; background: #f4f4f4; }
        #chat-box { height: 400px; border: 1px solid #ddd; padding: 15px; overflow-y: scroll; background: #fff; border-radius: 5px; margin-bottom: 10px; }
        input { width: 75%; padding: 10px; border: 1px solid #ccc; border-radius: 5px; }
        button { padding: 10px; background: #007bff; color: white; border: none; border-radius: 5px; cursor: pointer; }
    </style>
</head>
<body>
    <h3>Gemini AI</h3>
    <div id="chat-box"></div>
    <input id="in" placeholder="কিছু জিজ্ঞেস করুন...">
    <button onclick="send()">পাঠান</button>
    <script>
        function send() {
            let m = document.getElementById('in').value;
            if(!m) return;
            fetch('/api', {
                method:'POST', 
                headers:{'Content-Type':'application/json'}, 
                body:JSON.stringify({msg:m})
            })
            .then(r=>r.json()).then(d=>{
                document.getElementById('chat-box').innerHTML += `<p><b>আপনি:</b> ${m}</p>`;
                document.getElementById('chat-box').innerHTML += `<p><b>AI:</b> ${d.r}</p>`;
                document.getElementById('in').value = '';
            });
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home(): return render_template_string(HTML)

@app.route('/api', methods=['POST'])
def api():
    try:
        msg = request.json.get('msg')
        # এখানে কোনো কন্ডিশন নেই, সরাসরি এআই উত্তর দিবে
        response = model.generate_content(msg)
        return jsonify({'r': response.text})
    except:
        return jsonify({'r': "দুঃখিত, আমি এই মুহূর্তে উত্তর দিতে পারছি না।"})

if __name__ == '__main__': app.run(host='0.0.0.0', port=5000)
