import socket
from OpenSSL import SSL

# 1. Configuration
IP_ADDR = '127.0.0.1'
PORT = 4433
CERT_FILE = "certs/server.crt"
KEY_FILE = "certs/server.key"

def start_server():
    # 2. Setup the SSL Context (Identity Card)
    context = SSL.Context(SSL.DTLS_METHOD)
    context.use_certificate_file(CERT_FILE)
    context.use_privatekey_file(KEY_FILE)

    # 3. Create a raw UDP Socket
    # Notice: We do NOT wrap it immediately
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((IP_ADDR, PORT))
    
    print(f"[SERVER] UDP Server up and running on {IP_ADDR}:{PORT}")
    print("[SERVER] Waiting for the first packet to lock-in...")

    # 4. The "Lock-in" Trick for DTLS
    # We read the first packet just to know WHO is calling (Client Address)
    # peek(1) looks at data without removing it from the buffer
    data, addr = sock.recvfrom(1024, socket.MSG_PEEK) 
    print(f"[SERVER] Detected connection attempt from {addr}")

    # 5. Connect the UDP socket to this specific client
    # This turns the "mailbox" into a "private tunnel" for this session
    sock.connect(addr)

    # 6. NOW we wrap it with Security
    # We tell OpenSSL: "I am the server" (set_accept_state)
    server_conn = SSL.Connection(context, sock)
    server_conn.set_accept_state()

    try:
        print("[SERVER] Starting DTLS Handshake...")
        
        # 7. Read encrypted data
        # The handshake happens automatically inside the first recv()
        data = server_conn.recv(1024)
        print(f"[SERVER] Secure Message Received: {data.decode('utf-8')}")

        # 8. Send encrypted response
        server_conn.send(b"Hello Secure Client! I received your message.")
        print("[SERVER] Response sent.")

        # Keep connection open for a moment then close
        # server_conn.shutdown() 
        
    except SSL.Error as e:
        print(f"[ERROR] SSL Handshake failed: {e}")
    except Exception as e:
        print(f"[ERROR] General error: {e}")
    finally:
        server_conn.close()
        print("[SERVER] Connection closed.")

if __name__ == "__main__":
    start_server()