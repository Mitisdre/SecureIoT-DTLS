import socket
from OpenSSL import SSL

# Config
IP = '127.0.0.1'
PORT = 4433
CERT = "certs/server.crt"
KEY = "certs/server.key"

def start_server():
    # Setup Context (DTLS)
    ctx = SSL.Context(SSL.DTLS_METHOD)
    ctx.use_certificate_file(CERT)
    ctx.use_privatekey_file(KEY)

    # UDP Socket init
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((IP, PORT))

    print(f"[SERVER] Listening on {IP}:{PORT} (DTLS)")

    # Wait for incoming connection
    # Peek data to get client address / Adresse abrufen ohne Daten zu entfernen
    data, addr = sock.recvfrom(1024, socket.MSG_PEEK)
    print(f"[SERVER] Connection from {addr}")

    # Connect UDP socket to client (required for DTLS session)
    sock.connect(addr)

    # Wrap socket with SSL
    conn = SSL.Connection(ctx, sock)
    conn.set_accept_state() # Server mode

    try:
        # Handshake happens on first read
        data = conn.recv(1024)
        print(f"[RECV] {data.decode()}")

        # Send response
        conn.send(b"ACK: Secure Message Received")

    except Exception as e:
        print(f"[ERROR] {e}")
    finally:
        conn.close()
        print("[SERVER] Closed")

if __name__ == "__main__":
    start_server()