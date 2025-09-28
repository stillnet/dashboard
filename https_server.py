#!/usr/bin/env python3
"""
Simple HTTPS server for testing the dashboard locally.
Generates a self-signed certificate automatically.
"""

import http.server
import ssl
import socketserver
import os
from pathlib import Path

# Configuration
PORT = 8443
HOST = 'localhost'

def generate_self_signed_cert():
    """Generate a self-signed certificate for local testing."""
    try:
        import subprocess

        # Check if certificate files already exist
        if os.path.exists('server.crt') and os.path.exists('server.key'):
            print("Using existing certificate files...")
            return True

        print("Generating self-signed certificate...")

        # Generate private key and certificate
        subprocess.run([
            'openssl', 'req', '-x509', '-newkey', 'rsa:4096',
            '-keyout', 'server.key', '-out', 'server.crt',
            '-days', '365', '-nodes',
            '-subj', f'/C=US/ST=NE/L=Omaha/O=Dashboard/CN={HOST}'
        ], check=True)

        print("Certificate generated successfully!")
        return True

    except (subprocess.CalledProcessError, FileNotFoundError):
        print("OpenSSL not found. Using Python's built-in SSL context...")
        return False

def create_ssl_context():
    """Create SSL context with self-signed certificate."""
    if generate_self_signed_cert():
        # Use generated certificate
        context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        context.load_cert_chain('server.crt', 'server.key')
    else:
        # Use Python's built-in SSL context for testing
        context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
        context.check_hostname = False
        context.verify_mode = ssl.CERT_NONE

    return context

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    """Custom handler to serve our dashboard with proper headers."""

    def end_headers(self):
        # Add CORS headers for API requests
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type, Authorization')
        super().end_headers()

    def log_message(self, format, *args):
        """Custom logging to show clickable URLs."""
        message = format % args
        print(f"[{self.log_date_time_string()}] {message}")

def main():
    """Start the HTTPS server."""

    # Change to the directory containing the dashboard
    dashboard_dir = Path(__file__).parent
    os.chdir(dashboard_dir)

    print(f"Starting HTTPS server...")
    print(f"Directory: {dashboard_dir}")
    print(f"Files available:")
    for file in os.listdir('.'):
        if file.endswith(('.html', '.css', '.js')):
            print(f"  - {file}")

    # Create the server
    with socketserver.TCPServer((HOST, PORT), CustomHTTPRequestHandler) as httpd:
        # Add SSL
        ssl_context = create_ssl_context()
        httpd.socket = ssl_context.wrap_socket(httpd.socket, server_side=True)

        print(f"\n🚀 HTTPS Server running!")
        print(f"📱 Dashboard URL: https://{HOST}:{PORT}/dashboard.html")
        print(f"🔒 Using self-signed certificate (you'll see a security warning)")
        print(f"⚠️  Click 'Advanced' -> 'Proceed to localhost (unsafe)' in your browser")
        print(f"\n📂 All files: https://{HOST}:{PORT}/")
        print(f"\nPress Ctrl+C to stop the server")

        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n👋 Server stopped!")

if __name__ == "__main__":
    main()