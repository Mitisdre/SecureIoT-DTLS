#!/bin/bash

# 1. Define where to store certificates
CERT_DIR="certs"

# 2. Create the directory if it does not exist
# -p flag ensures no error if folder already exists
mkdir -p $CERT_DIR

echo "--- Cleaning up old certificates ---"
rm -f $CERT_DIR/*.pem $CERT_DIR/*.crt $CERT_DIR/*.key

echo "--- Generating SERVER Certificates ---"
# Generating a self-signed certificate for the Server
# CN (Common Name) is set to 'localhost' for local testing
openssl req -x509 -newkey rsa:2048 -days 365 -nodes \
    -keyout $CERT_DIR/server.key \
    -out $CERT_DIR/server.crt \
    -subj "/C=DE/ST=NRW/L=Dusseldorf/O=IoT-University/CN=localhost"

echo "--- Generating CLIENT Certificates ---"
# Generating a self-signed certificate for the Client (Sensor)
openssl req -x509 -newkey rsa:2048 -days 365 -nodes \
    -keyout $CERT_DIR/client.key \
    -out $CERT_DIR/client.crt \
    -subj "/C=DE/ST=NRW/L=Dusseldorf/O=IoT-University/CN=IoTSensorDevice"

echo "--- Success! Certificates are ready in '$CERT_DIR/' ---"
ls -l $CERT_DIR