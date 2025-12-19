import socket
from OpenSSL import SSL

# Konfiguration
SERVER_IP = '127.0.0.1'
PORT = 4433
CA_FILE = "certs/ca.crt"

def start_client():
    # Setup SSL Context
    ctx = SSL.Context(SSL.DTLS_METHOD)
    
    # Load CA for verification / CA laden zur Verifizierung
    ctx.load_verify_locations(CA_FILE)
    ctx.set_verify(SSL.VERIFY_PEER, lambda conn, cert, errno, depth, ret: True)

    # UDP Socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.connect((SERVER_IP, PORT)) # Set remote address

    # Wrap Socket
    conn = SSL.Connection(ctx, sock)
    conn.set_connect_state() # Client mode

    try:
        # User Input / Benutzereingabe
        print(f"[CLIENT] Verbunden mit {SERVER_IP}:{PORT}")
        print("Geben Sie eine Nachricht ein (Enter für Default):")
        user_input = input("> ")

        # Default message if input is empty
        if not user_input:
            msg = "SECRET_TELEMETRY: Temp=42C"
        else:
            msg = user_input

        print(f"[SEND] Verschlüsselt senden: '{msg}'")
        
        # Trigger Handshake & Send
        conn.send(msg.encode())

        # Receive reply
        resp = conn.recv(1024)
        print(f"[RECV] Server antwortete: {resp.decode()}")

    except Exception as e:
        print(f"[ERROR] Handshake failed: {e}")
    finally:
        conn.close()

if __name__ == "__main__":
    start_client()