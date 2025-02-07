import requests

# Replace these with your bot token and chat ID
TELEGRAM_BOT_TOKEN = "7948703164:AAFmyzMmNy2r9nuXF10LnPFRq1VrS08T68s"
CHAT_ID = "5031537782"

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    response = requests.post(url, json=payload)
    
    # Print response for debugging
    print("Response Status Code:", response.status_code)
    print("Response JSON:", response.json())

    return response.json()

# Send a test message
send_telegram_message("Hello! This is a test message from your Forex News Bot.")
 