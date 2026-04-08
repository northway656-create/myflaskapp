from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "<h1>My Flask App is Live!</h1><p>Website successfully hosted on Render.</p>"

if __name__ == '__main__':
    app.run(debug=True)
  
