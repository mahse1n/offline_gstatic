import http.server
import ssl
import os
import mimetypes
import requests

PORT = 443
ASSET_DIR = "assets"

# Hardcoded IPs from your ping results to bypass hosts file
IP_WWW = "142.250.201.67"    # www.gstatic.com
IP_FONTS = "142.250.202.35"  # fonts.gstatic.com    

class CachingGStaticProxy(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', '*')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def do_GET(self):
        # Remove query strings for local storage (e.g. ?v=12.3.0)
        clean_path = self.path.split('?')[0]
        local_path = os.path.join(os.getcwd(), ASSET_DIR, clean_path.lstrip('/'))

        # 1. Check if we already have it locally
        if not (os.path.exists(local_path) and os.path.isfile(local_path)):
            print(f"--- [MISSING] {self.path} -> Attempting IP-Bypass Download...")
            self.download_with_ip_bypass(clean_path, local_path)

        # 2. Serve the file if it exists
        if os.path.exists(local_path) and os.path.isfile(local_path):
            self.send_response(200)
            
            # MIME type handling
            content_type, _ = mimetypes.guess_type(local_path)
            if local_path.endswith('.wasm'): content_type = 'application/wasm'
            if local_path.endswith('.js'): content_type = 'application/javascript'
            if content_type:
                self.send_header('Content-Type', content_type)
            
            self.end_headers()
            with open(local_path, 'rb') as f:
                self.wfile.write(f.read())
        else:
            self.send_error(404, f"File not found: {self.path}")

    def download_with_ip_bypass(self, path, save_to):
        # Determine target domain and corresponding IP
        if path.startswith("/s/"):
            target_ip = IP_FONTS
            host_header = "fonts.gstatic.com"
        else:
            target_ip = IP_WWW
            host_header = "www.gstatic.com"
        
        # We connect to the IP but verify against the Host Header
        url = f"https://{target_ip}{path}"
        
        try:
            # We must set verify=False or provide the cert because the 
            # IP won't match the 'gstatic.com' cert in a standard check.
            response = requests.get(url, headers={"Host": host_header}, verify=False, timeout=15)
            
            if response.status_code == 200:
                os.makedirs(os.path.dirname(save_to), exist_ok=True)
                with open(save_to, 'wb') as f:
                    f.write(response.content)
                print(f"--- [SUCCESS] Downloaded via {target_ip} and saved to {save_to}")
            else:
                print(f"--- [FAILED] Server {target_ip} returned {response.status_code}")
        except Exception as e:
            print(f"--- [ERROR] Could not download from {target_ip}: {e}")

# Register MIME types for Windows
mimetypes.add_type('application/wasm', '.wasm')
mimetypes.add_type('font/woff2', '.woff2')
mimetypes.add_type('application/javascript', '.js')

print(f"Serving and Caching HTTPS on port {PORT} (IP-Bypass Enabled)...")
httpd = http.server.HTTPServer(('0.0.0.0', PORT), CachingGStaticProxy)

# SSL setup
context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")

httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

try:
    httpd.serve_forever()
except KeyboardInterrupt:
    print("\nShutting down server.")