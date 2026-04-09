from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <html>
    <head>
        <title>Free Fire Tournament</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
    </head>
    <body style="background:#121212; color:white; text-align:center; font-family:sans-serif; padding-top:50px;">
        <h2 style="color:#ffcc00;">💎 FREE FIRE REGISTRATION 💎</h2>
        <div style="background:#1e1e1e; border:1px solid #333; display:inline-block; padding:30px; border-radius:15px; box-shadow: 0px 0px 20px rgba(255,204,0,0.2);">
            <form action="/submit" method="post">
                <input type="text" name="uid" placeholder="FF Player UID" required style="padding:12px; width:90%; margin-bottom:15px; border-radius:5px; border:none;"><br>
                <input type="email" name="email" placeholder="Email Address" required style="padding:12px; width:90%; margin-bottom:15px; border-radius:5px; border:none;"><br>
                <input type="text" name="phone" placeholder="WhatsApp Number" required style="padding:12px; width:90%; margin-bottom:15px; border-radius:5px; border:none;"><br>
                <select name="account" style="padding:12px; width:96%; margin-bottom:20px; border-radius:5px; border:none;">
                    <option value="Google">Google Account</option>
                    <option value="Facebook">Facebook Account</option>
                    <option value="VK">VK Account</option>
                </select><br>
                <button type="submit" style="background:#ffcc00; color:black; font-weight:bold; padding:15px 40px; border:none; border-radius:5px; cursor:pointer; width:100%;">
                    REGISTER NOW
                </button>
            </form>
        </div>
        <p style="margin-top:20px; font-size:12px; color:#666;">Enter your details to join the custom match.</p>
    </body>
    </html>
    '''

@app.route('/submit', methods=['POST'])
def submit():
    return '<body style="background:#121212; color:white; text-align:center; padding-top:100px;"><h2>✅ Registration Successful!</h2><p>Wait for the tournament details on your WhatsApp.</p></body>'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
    
