from flask import Flask, send_file

app = Flask(__name__)

@app.route("/")
def home():
    return send_file("payment.html")

@app.route("/payment")
def payment():
    return send_file("payment.html")

@app.route("/camera")
def camera():
    return send_file("camera.html")

@app.route("/edit")
def edit():
    return send_file("edit.html")

@app.route("/thanks")
def thanks():
    return send_file("thanks.html")

if __name__ == "__main__":
    app.run(debug=True)
