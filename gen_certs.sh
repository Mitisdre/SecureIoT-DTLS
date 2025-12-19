#!/bin/bash
set -e  # Stop on error

CERT_DIR="certs"

# Check OpenSSL
if ! command -v openssl &> /dev/null; then
    echo "Error: OpenSSL not found!"
    exit 1
fi

# 1. Setup Directory / Verzeichnis erstellen
mkdir -p "$CERT_DIR"
rm -f "$CERT_DIR"/* || true

echo "--- Generating Root CA ---"
# CA Key & Self-signed Certificate
openssl req -x509 -new -nodes -newkey rsa:2048 \
    -keyout "$CERT_DIR/ca.key" \
    -out "$CERT_DIR/ca.crt" \
    -days 365 \
    -subj "/C=DE/ST=NRW/L=Dusseldorf/O=IoT-CA/CN=RootCA"

echo "--- Generating Server Cert ---"
# Server Key & CSR
openssl req -new -nodes -newkey rsa:2048 \
    -keyout "$CERT_DIR/server.key" \
    -out "$CERT_DIR/server.csr" \
    -subj "/C=DE/ST=NRW/L=Dusseldorf/O=IoT-Project/CN=localhost"

# Sign with CA / Mit CA signieren
openssl x509 -req -in "$CERT_DIR/server.csr" \
    -CA "$CERT_DIR/ca.crt" -CAkey "$CERT_DIR/ca.key" -CAcreateserial \
    -out "$CERT_DIR/server.crt" -days 365

echo "--- Generating Client Cert ---"
# Client Key & CSR
openssl req -new -nodes -newkey rsa:2048 \
    -keyout "$CERT_DIR/client.key" \
    -out "$CERT_DIR/client.csr" \
    -subj "/C=DE/ST=NRW/L=Dusseldorf/O=IoT-Project/CN=SensorDevice"

# Sign with CA
openssl x509 -req -in "$CERT_DIR/client.csr" \
    -CA "$CERT_DIR/ca.crt" -CAkey "$CERT_DIR/ca.key" \
    -out "$CERT_DIR/client.crt" -days 365

echo "Done. Certificates in $CERT_DIR/"
ls -l "$CERT_DIR"