# Secure IoT Communication Protocol Simulation (DTLS)

This project demonstrates a secure communication channel designed for IoT (Internet of Things) devices using **DTLS (Datagram Transport Layer Security)**. It simulates a sensor-server architecture where sensitive data is transmitted over UDP.

The project includes a comparison between **Cleartext UDP** (Insecure) and **DTLS Encrypted UDP** (Secure) to showcase the importance of encryption in network security.

## 🚀 Features

* **Secure Communication:** Uses DTLS v1.2 via OpenSSL to encrypt UDP packets.
* **PKI Implementation:** Includes a shell script to automate Certificate Authority (CA) and Key generation.
* **Packet Analysis:** Designed to be analyzed with Wireshark to verify encryption.
* **Insecure Baseline:** Includes a plain UDP implementation for side-by-side comparison.
* **Cross-Platform:** Developed in Python, compatible with Linux and macOS.

## 🛠 Technology Stack

* **Language:** Python 3.x
* **Library:** `pyOpenSSL` (Wrapper for OpenSSL)
* **Protocol:** UDP / DTLS
* **Tools:** Wireshark (for traffic analysis), OpenSSL (for certificates)

## 📸 Proof of Concept (Wireshark Analysis)

We analyzed the network traffic for both secure and insecure implementations to demonstrate the effectiveness of DTLS.

### 🔒 1. Secure Communication (DTLS)
*With DTLS enabled, the payload is fully encrypted. As seen below, Wireshark captures only meaningless bytes (Application Data). The attacker cannot read the sensor data.*

![Secure DTLS Traffic](images/secure_dtls.png)

### 🔓 2. Insecure Communication (Plain UDP)
*Without encryption, the data is transmitted in cleartext. The sensitive information (`SECRET_DATA...`) is clearly visible to anyone listening on the network.*

![Insecure UDP Traffic](images/insecure_udp.png)

## 📦 Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Mitisdre/SecureIoT-DTLS.git](https://github.com/Mitisdre/SecureIoT-DTLS.git)
    cd SecureIoT-DTLS
    ```

2.  **Create a Virtual Environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Generate Certificates:**
    *Note: Certificates are not included in the repo for security reasons. You must generate them locally.*
    ```bash
    chmod +x gen_certs.sh
    ./gen_certs.sh
    ```

## 🚦 Usage

### Secure Mode (DTLS)
1.  **Start the Server:** `python server.py`
2.  **Start the Client:** `python client.py`
3.  *Result: Data is encrypted. Wireshark shows "Application Data".*

### Insecure Mode (Plain UDP)
1.  **Start the Server:** `python insecure_server.py`
2.  **Start the Client:** `python insecure_client.py`
3.  *Result: Data is cleartext. Wireshark shows the actual message content.*

## 📄 License
This project is for educational purposes as part of the IT Security module.
