#!/bin/bash
# Find the current local IP address on macOS
IP_ADDR=$(ipconfig getifaddr en0)
# If en0 is blank, try en1 (standard for Wi-Fi)
if [ -z "$IP_ADDR" ]; then
    IP_ADDR=$(ipconfig getifaddr en1)
fi
echo "Current Mac IP detected: $IP_ADDR"
# Overwrite the .env file with the new IP
echo "EXPO_PUBLIC_API_URL=http://$IP_ADDR:8000" > .env
echo ".env file updated successfully!"