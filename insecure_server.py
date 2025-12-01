import socket

# 1. Configuration
IP_ADDR = '127.0.0.1'
PORT = 9999  # Let's use a different port to avoid confusion with DTLS (4433)

def start_insecure_server():
    # 2. Create a standard UDP Socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # 3. Bind to the port
    sock.bind((IP_ADDR, PORT))
    
    print(f"[INSECURE SERVER] Listening on {IP_ADDR}:{PORT} (No Encryption)")
    
    while True:
        # 4. Receive Data directly
        # No 'accept', no 'handshake'. Just raw data.
        data, addr = sock.recvfrom(1024)
        
        message = data.decode('utf-8')
        print(f"[INSECURE SERVER] Received from {addr}: {message}")
        
        # 5. Send plain text reply
        response = "ACK: Data received (but everyone saw it!)"
        sock.sendto(response.encode('utf-8'), addr)

if __name__ == "__main__":
    start_insecure_server()