import os
import pytest
from dotenv import load_dotenv
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '../../../.env'))

from app.services.paypal import get_paypal_access_token

# API Credentials for Sandbox
PAYPAL_CLIENT_ID = os.getenv("PAYPAL_CLIENT_ID")
PAYPAL_CLIENT_SECRET = os.getenv("PAYPAL_CLIENT_SECRET")
PAYPAL_API_BASE = os.getenv("PAYPAL_API_BASE")


def test_live_get_paypal_access_token_success():
    # Succeeds with valid credentials and returns access token (200)

    token = get_paypal_access_token()

    assert token is not None


def test_live_get_paypal_access_token_error(monkeypatch):
    # Fails when invalid credentials are provided (401)
    monkeypatch.setattr("app.services.paypal.PAYPAL_CLIENT_ID", None)

    monkeypatch.delenv("PAYPAL_CLIENT_ID", raising=False)

    with pytest.raises(ValueError) as excinfo:
        get_paypal_access_token()