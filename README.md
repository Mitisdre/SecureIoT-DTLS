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

## 📦 Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/YOUR_USERNAME/SecureIoT-DTLS.git](https://github.com/YOUR_USERNAME/SecureIoT-DTLS.git)
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
    ```bash
    chmod +x gen_certs.sh
    ./gen_certs.sh
    ```

## 🚦 Usage

### 1. Secure Mode (DTLS)
* **Start the Server:** `python server.py`
* **Start the Client:** `python client.py`
* *Result: Data is encrypted. Wireshark shows "Application Data".*

### 2. Insecure Mode (Plain UDP)
* **Start the Server:** `python insecure_server.py`
* **Start the Client:** `python insecure_client.py`
* *Result: Data is cleartext. Wireshark shows the actual message content.*


## 📄 License
This project is for educational purposes as part of the IT Security module.