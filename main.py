# কোডের HTML অংশটি নিচে বসিয়ে দিন
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
        .menu-wrapper { padding: 15px; background: rgba(0,0,0,0.9); border-top: 1px solid #333; }
        .sub-menu { display: none; margin-top: 10px; }
        button { padding: 12px; background: #007bff; border: none; color: white; border-radius: 8px; font-weight: bold; cursor: pointer; width: 100%; margin-bottom: 5px; }
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
            <div id="mainMenu" class="sub-menu">
                <button onclick="showOrderForm()">🛒 ক্রয় প্যানেল</button>
                <button onclick="window.location.href='https://vt.tiktok.com/ZSQXNja3P/'">🎬 রিভিউ ভিডিও</button>
                <button onclick="window.location.href='https://t.me/Ridoy_Official_penal'">📢 টেলিগ্রাম সাপোর্ট</button>
                <button onclick="window.location.href='https://wa.me/qr/SIZBFCXQT2AUG1'">💬 হোয়াটসঅ্যাপ সাপোর্ট</button>
            </div>
        </div>
    </div>
    <script>
        function toggleMenu() { 
            var m = document.getElementById('mainMenu'); 
            if (m.style.display === 'block') { m.style.display = 'none'; } 
            else { m.style.display = 'block'; }
        }
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
                        if(res.status == "approved") { 
                            document.getElementById('box').innerHTML = "<h3>✅ অভিনন্দন! পেমেন্ট সফল।<br><br><a href='https://t.me/+oe_rcewUi142ZmNl' target='_blank' style='color:yellow; font-size:20px; text-decoration:none;'>👉 এখানে ক্লিক করে সরাসরি গ্রুপে জয়েন করুন 👈</a></h3>"; 
                            clearInterval(check); 
                        }
                        else if(res.status == "rejected") { 
                            document.getElementById('box').innerHTML = "<h3>❌ পেমেন্ট রিজেক্ট হয়েছে! আবার ট্রাই করুন।</h3>"; 
                            clearInterval(check); 
                        }
                    });
                }, 3000);
            });
        }
    </script>
</body>
</html>
"""
