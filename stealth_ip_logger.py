from flask import Flask, request, send_file
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def log_ip():
    ip = request.headers.get('X-Forwarded-For', request.remote_addr)
    agent = request.headers.get('User-Agent')
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    with open("logs.txt", "a") as file:
        file.write(f"{timestamp} | IP: {ip} | Agent: {agent}\n")

    return send_file("image.jpg", mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=10000)
