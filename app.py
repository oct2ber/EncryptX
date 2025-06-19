from flask import Flask, render_template, request
from encryption import encrypt_text, decrypt_text
import barcode
from barcode.writer import ImageWriter
import os
import uuid

app = Flask(__name__)

# Folder to store generated barcode images
BARCODE_FOLDER = 'static/barcodes'
os.makedirs(BARCODE_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    action = ""
    method = ""
    barcode_img_path = None

    if request.method == "POST":
        text = request.form.get("message", "")
        action = request.form.get("action", "")
        method = request.form.get("method", "")
        password = request.form.get("password", "")

        if method == "SuperSecure" and action == "Decrypt":
            if password != "oct2ber":
                result = "❌ Wrong password!"
                return render_template("index.html", result=result, action=action)

        if method == "Barcode" and action == "Encrypt":
            # Generate barcode image
            code = barcode.get('code128', text, writer=ImageWriter())
            filename = f"{uuid.uuid4()}.png"
            path = os.path.join(BARCODE_FOLDER, filename)
            code.save(path[:-4])
            barcode_img_path = "/" + path.replace("\\", "/")
            result = f"<img src='{barcode_img_path}' alt='Barcode Image' style='max-width:100%;' />"
        elif method == "Barcode" and action == "Decrypt":
            result = "❌ Cannot decrypt barcode!"
        elif method == "Auto":
            result, method = auto_decrypt(text)
            action = "Auto-Decrypted"
        elif action == "Encrypt":
            result = encrypt_text(text, method)
        elif action == "Decrypt":
            result = decrypt_text(text, method)

    return render_template("index.html", result=result, action=action)

def auto_decrypt(text):
    try:
        # Try all known methods and return first successful decryption
        if '#' in text and '!' in text:
            return decrypt_text(text, "SuperSecure"), "SuperSecure"
        elif all(c in ".-/ " for c in text.strip()):
            return decrypt_text(text, "Morse"), "Morse"
        elif text[::-1] != text and len(text) > 2:
            return decrypt_text(text, "Reverse"), "Reverse"
        elif any(c in "😀😎🥲😱🤯🛸" for c in text):
            return decrypt_text(text, "Emoji"), "Emoji"
        else:
            return decrypt_text(text, "Caesar"), "Caesar"
    except:
        return "❌ Auto-decryption failed.", "Unknown"

if __name__ == "__main__":
    app.run(debug=True)
