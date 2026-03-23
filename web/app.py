from flask import Flask, render_template
import os

app = Flask(__name__)

LOG_FILE = "../data/sample_logs.txt"

@app.route("/")
def index():
    logs = []
    
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, "r") as f:
            logs = f.readlines()
    
    return render_template("index.html", logs=logs)

if __name__ == "__main__":
    app.run(debug=True)
