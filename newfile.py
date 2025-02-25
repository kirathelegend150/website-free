from flask import Flask, render_template
import os

app = Flask(__name__, template_folder="templates", static_folder="static")

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    os.system("termux-open-url http://127.0.0.1:5000")
    app.run(host="0.0.0.0", port=5000, debug=True)