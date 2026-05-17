from flask import Flask, jsonify, render_template, request
from cipher import encrypt_columnar, decrypt_columnar

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/encrypt", methods=["POST"])
def encrypt():
    data = request.get_json()

    plaintext = data.get("text", "")
    key = data.get("key", "").strip()

    if not key:
        return jsonify({"error": "Enter a key before encrypting."}), 400

    encrypted = encrypt_columnar(plaintext, key)

    return jsonify({
        "result": encrypted
    })


@app.route("/decrypt", methods=["POST"])
def decrypt():
    data = request.get_json()

    ciphertext = data.get("text", "")
    key = data.get("key", "").strip()

    if not key:
        return jsonify({"error": "Enter a key before decrypting."}), 400

    if not ciphertext:
        return jsonify({"error": "Encrypt a message before decrypting."}), 400

    decrypted = decrypt_columnar(ciphertext, key)

    return jsonify({
        "result": decrypted
    })


if __name__ == "__main__":
    app.run(debug=True)
