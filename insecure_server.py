import socket

IP = '127.0.0.1'
PORT = 9999 # Non-DTLS port

def start_plain_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((IP, PORT))
    
    print(f"[PLAIN SERVER] Listening on {PORT} (No Encryption)")
    
    while True:
        # Direct recv (No Handshake)
        data, addr = sock.recvfrom(1024)
        print(f"[RECV] from {addr}: {data.decode()}")
        
        sock.sendto(b"ACK: Data received (Plaintext)", addr)

if __name__ == "__main__":
    start_plain_server()