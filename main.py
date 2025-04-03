# Ethical Camera Access System - Educational Purposes Only
# Author: [Your Name]
# Institution: [Your School Name]

import os
import sys
import time
import cv2
import threading
import subprocess
from flask import Flask, Response, request

# Configuration
RECORDING_FOLDER = "ethical_recordings"
CONSENT_FILE = "user_consent.txt"
PASSWORD = "education123"  # Change for your project
PORT = 5000

# Ethical disclaimer
DISCLAIMER = """
ETHICAL CAMERA ACCESS SYSTEM - EDUCATIONAL USE ONLY
--------------------------------------------------
This system demonstrates camera access technology for:
- Computer vision education
- Security system principles
- Ethical hacking concepts

Features:
1. Requires explicit user consent
2. Password protected access
3. Clear activity logging
4. No hidden functionality

By using this system, you agree to:
- Use only for educational purposes
- Get proper consent for all recordings
- Comply with all privacy laws
"""


class EthicalCameraSystem:
    def __init__(self):
        self.camera_active = False
        self.app = Flask(__name__)
        self.setup_routes()

    def setup_routes(self):
        @self.app.route('/')
        def login():
            return """
            <h2>Educational Camera Access</h2>
            <form method="post" action="/authenticate">
            <p>Password: <input type="password" name="password">
            <input type="submit" value="Access"></p>
            </form>
            """

        @self.app.route('/authenticate', methods=['POST'])
        def authenticate():
            if request.form['password'] == PASSWORD:
                self.camera_active = True
                return Response(self.generate_frames(),
                                mimetype='multipart/x-mixed-replace; boundary=frame')
            return "Access Denied", 401

    def generate_frames(self):
        cap = cv2.VideoCapture(0)
        while self.camera_active:
            success, frame = cap.read()
            if not success:
                break
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        cap.release()

    def get_user_consent(self):
        if not os.path.exists(CONSENT_FILE):
            print(DISCLAIMER)
            consent = input("Do you consent to these terms? (yes/no): ").lower()
            if consent == 'yes':
                with open(CONSENT_FILE, 'w') as f:
                    f.write(f"Consent granted at {time.ctime()}\n")
                    f.write(f"Password: {PASSWORD}\n")
                return True
            return False
        return True

    def start_cloudflared(self):
        cloudflared_path = os.path.join(os.path.expanduser("~"), ".cffolder", "cloudflared")

        if not os.path.exists(cloudflared_path):
            print("Downloading Cloudflared...")
            os.makedirs(os.path.dirname(cloudflared_path), exist_ok=True)

            system = os.uname().sysname.lower()
            arch = os.uname().machine

            if system == "linux":
                if "arm" in arch or "aarch" in arch:
                    url = "https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-arm"
                else:
                    url = "https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-linux-amd64"
            elif system == "darwin":
                url = "https://github.com/cloudflare/cloudflared/releases/latest/download/cloudflared-darwin-amd64.tgz"
            else:
                print("Unsupported system for automatic download")
                return

            os.system(f"wget {url} -O {cloudflared_path}")
            os.chmod(cloudflared_path, 0o755)

        print("Starting secure tunnel...")
        tunnel = subprocess.Popen(
            [cloudflared_path, "tunnel", "--url", f"http://localhost:{PORT}"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        time.sleep(5)  # Wait for tunnel to establish
        for line in tunnel.stderr:
            if "trycloudflare.com" in line:
                url = line.split("https://")[1].strip()
                print(f"\nSecure Access URL: https://{url}")
                print(f"Access Password: {PASSWORD}")
                break

    def run(self):
        if not self.get_user_consent():
            print("System shutdown - consent not provided")
            return

        if not os.path.exists(RECORDING_FOLDER):
            os.makedirs(RECORDING_FOLDER)

        # Start tunnel in background
        threading.Thread(target=self.start_cloudflared, daemon=True).start()

        # Start web server
        print(f"Local access: http://localhost:{PORT}")
        self.app.run(host='0.0.0.0', port=PORT)


if __name__ == '__main__':
    system = EthicalCameraSystem()
    system.run()