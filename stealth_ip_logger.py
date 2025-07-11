from flask import Flask, request, send_file
from datetime import datetime
import os

app = Flask(__name__)

@app.route('/')
def log_ip():
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    agent = request.headers.get('User-Agent')
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    with open("logs.txt", "a") as file:
        file.write(f"{timestamp} | IP: {ip} | Agent: {agent}\n")

    image_path = os.path.join(os.path.dirname(__file__), 'image.jpg')
    return send_file(image_path, mimetype='image/jpeg')

@app.route('/logs')
def show_logs():
    # Simple protection with key
    secret = request.args.get('key')
    if secret != "vulpix123":
        return "Access Denied", 403

    try:
        with open("logs.txt", "r") as f:
            return "<pre>" + f.read() + "</pre>"
    except FileNotFoundError:
        return "No logs yet."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
