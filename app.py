import webview
from threading import Thread
from flask import Flask, render_template, request, send_file
import qrcode
import io
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    link = request.form.get("url")  # Get URL from form input
    if not link.strip():
        return "Error! Please enter a valid Link!", 400 # Default URL
    
    # Generate QR code (Keeping your existing logic)
    qr = qrcode.make(link)

    # Save QR code to an in-memory file
    img_io = io.BytesIO()
    qr.save(img_io, format="PNG")
    img_io.seek(0)

    return send_file(img_io, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
