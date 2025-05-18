from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hello from Sourav, I'm testing Reverse Proxy using NGINX!</h1>"

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000)
