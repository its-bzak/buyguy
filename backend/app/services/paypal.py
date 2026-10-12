import os
import requests
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '../../.env'))

PAYPAL_CLIENT_ID = os.getenv("PAYPAL_CLIENT_ID")
PAYPAL_CLIENT_SECRET = os.getenv("PAYPAL_CLIENT_SECRET")
PAYPAL_API_BASE = os.getenv("PAYPAL_API_BASE")

def get_paypal_access_token():
    
    if not PAYPAL_CLIENT_ID or not PAYPAL_CLIENT_SECRET:
        raise ValueError("Missing PayPal credentials in .env file")

    url = f"{PAYPAL_API_BASE}/v1/oauth2/token"
    headers = {
        "Accept": "application/json",
        "Accept-Language": "en_US"
    }
    data = {
        "grant_type": "client_credentials"
    }
    
    # Auth for PayPal API
    try:
        # Make Network call
        response = requests.post(
            url,
            headers=headers,
            data=data,
            auth=(PAYPAL_CLIENT_ID, PAYPAL_CLIENT_SECRET),
            timeout=10
        )
        
        if response.status_code != 200:
            print(f"PayPal Auth Failed: {response.status_code}")
            return None

        # Parse JSON
        response_data = response.json()
        return response_data["access_token"]

    except requests.exceptions.RequestException as err:
        # Catch network errors
        print(f"Network error communicating with PayPal: {err}")
        return None
    except ValueError as err:
        # Catch JSON errors
        print(f"Failed to parse PayPal response: {err}")
        return None
    except KeyError as err:
        # Catch missing keys
        print(f"Unexpected response format from PayPal: missing {err}")
        return None