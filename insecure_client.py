import socket

SERVER_IP = '127.0.0.1'
PORT = 9999

def start_insecure_client():
    print(f"[INSECURE CLIENT] Sending data to {SERVER_IP}:{PORT}...")
    
    # 1. Create UDP Socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    # 2. Send Data (Plain Text)
    message = "DANGER_DATA: My Password is '123456'"
    print(f"[INSECURE CLIENT] Sending: {message}")
    
    sock.sendto(message.encode('utf-8'), (SERVER_IP, PORT))
    
    # 3. Receive Reply
    data, _ = sock.recvfrom(1024)
    print(f"[INSECURE CLIENT] Server replied: {data.decode('utf-8')}")
    
    sock.close()

if __name__ == "__main__":
    start_insecure_client()