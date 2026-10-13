import os
import requests
from dotenv import load_dotenv
from app.schemas.product import Product, ProductSearchQuery

load_dotenv()

CHANNEL3_API_KEY = os.getenv("CHANNEL3_API_KEY")
CHANNEL3_BASE_URL = os.getenv("CHANNEL3_BASE_URL", "https://api.channel3.ai/v1")

def search_channel3_products(search_params: ProductSearchQuery) -> list[Product]:
    if not CHANNEL3_API_KEY:
        raise ValueError("Missing CHANNEL3_API_KEY in environment variables")

    headers = {
        "Authorization": f"Bearer {CHANNEL3_API_KEY}",
        "Content-Type": "application/json"
    }
    
    params = {
        "q": search_params.query,
        "limit": search_params.limit,
    }
    if search_params.max_price:
        params["max_price"] = search_params.max_price

    try:
        response = requests.get(
            f"{CHANNEL3_BASE_URL}/products/search",
            headers=headers,
            params=params,
            timeout=10
        )
        response.raise_for_status()
        data = response.json()
        
        # Parse list of products into validated Pydantic objects
        raw_products = data.get("products", [])
        return [Product(**item) for item in raw_products]

    except requests.exceptions.RequestException as err:
        print(f"Channel3 API Error: {err}")
        return []
    except Exception as err:
        print(f"Data parsing error in Channel3 response: {err}")
        return []