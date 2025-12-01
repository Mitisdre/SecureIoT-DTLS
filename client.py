import socket
from OpenSSL import SSL

# 1. Configuration
SERVER_IP = '127.0.0.1'
PORT = 4433

# Note: In a real production scenario, the client would need the CA certificate
# to verify that the server is NOT a fake one. 
# For this demo, we will skip strict verification (VERIFY_NONE) to keep it simple.

def start_client():
    print(f"[CLIENT] Connecting to {SERVER_IP}:{PORT}...")

    # 2. Setup SSL Context
    context = SSL.Context(SSL.DTLS_METHOD)
    # We are the client, so we don't necessarily need a certificate for ourselves
    # unless we do Mutual Authentication (which we might add later).
    
    # 3. Create UDP Socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # 4. Connect (UDP Style)
    # In UDP, 'connect' just sets the default destination address.
    sock.connect((SERVER_IP, PORT))

    # 5. Wrap the socket
    client_conn = SSL.Connection(context, sock)
    
    # Critical: Tell OpenSSL "I am the Client"
    client_conn.set_connect_state()

    try:
        # 6. Send Data (This triggers the Handshake!)
        # The handshake happens automatically before the first data is sent.
        message = "SECRET_SENSOR_DATA: Temp=42.5C"
        print(f"[CLIENT] Sending encrypted message: {message}")
        
        client_conn.send(message.encode('utf-8'))

        # 7. Wait for Server Response
        response = client_conn.recv(1024)
        print(f"[CLIENT] Server replied: {response.decode('utf-8')}")

    except SSL.Error as e:
        print(f"[ERROR] SSL Handshake failed: {e}")
    except Exception as e:
        print(f"[ERROR] General error: {e}")
    finally:
        client_conn.close()
        print("[CLIENT] Connection closed.")

if __name__ == "__main__":
    start_client()