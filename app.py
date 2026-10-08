print("Python file is running!")

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "CI/CD Cloud Project is Running!"

if __name__ == "__main__":
    print("Starting Flask...")
    app.run(host="127.0.0.1", port=5000)