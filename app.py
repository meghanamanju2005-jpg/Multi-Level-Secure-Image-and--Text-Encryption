from flask import Flask, render_template, request
from hill_cipher import encrypt, decrypt
from steganography import hide_message, extract_message
import os

app = Flask(__name__)

UPLOAD_FOLDER = "images"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/encrypt", methods=["POST"])
def encrypt_message():
    message = request.form["message"]
    file = request.files["image"]

    filename = os.path.join(app.config["UPLOAD_FOLDER"], "input.png")
    file.save(filename)

    encrypted = encrypt(message)

    hide_message(
        "images/input.png",
        encrypted,
        "images/secret.png"
    )

    return render_template(
        "index.html",
        result=encrypted,
        success="Message hidden successfully in secret.png"
    )

@app.route("/decrypt", methods=["POST"])
def decrypt_message():
    encrypted_text = extract_message("images/secret.png")
    original_message = decrypt(encrypted_text)

    return render_template(
        "index.html",
        decrypted=original_message
    )

if __name__ == "__main__":
    app.run(debug=True)