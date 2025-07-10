from flask import Flask, request, send_file
from datetime import datetime
import os

app = Flask(__name__)

@app.route('/')
def log_ip():
    # Get client IP and User-Agent
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    agent = request.headers.get('User-Agent')
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Save to logs.txt
    with open("logs.txt", "a") as file:
        file.write(f"{timestamp} | IP: {ip} | Agent: {agent}\n")

    # Serve image
    image_path = os.path.join(os.path.dirname(__file__), 'shopping.jpg')
    return send_file(image_path, mimetype='image/jpeg')


if __name__ == '__main__':
    # Run on host 0.0.0.0 and port 10000 (Render-compatible)
    app.run(host='0.0.0.0', port=10000)
