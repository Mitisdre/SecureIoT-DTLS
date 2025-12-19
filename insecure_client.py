import socket

IP = '127.0.0.1'
PORT = 9999

def start_plain_client():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    print(f"[INSECURE CLIENT] Ziel: {IP}:{PORT}")
    print("Geben Sie eine Nachricht ein (Enter für Default):")
    user_input = input("> ")

    if not user_input:
        msg = "CRITICAL_DATA: Password=12345"
    else:
        msg = user_input

    print(f"[SEND] Sende Klartext: '{msg}'")
    
    # Send plain text
    sock.sendto(msg.encode(), (IP, PORT))
    
    # Wait for ACK
    data, _ = sock.recvfrom(1024)
    print(f"[RECV] {data.decode()}")
    
    sock.close()

if __name__ == "__main__":
    start_plain_client()