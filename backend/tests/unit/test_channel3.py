from unittest.mock import patch, MagicMock
from app.services.channel3 import search_channel3_products
from app.schemas.product import ProductSearchQuery

@patch("app.services.channel3.requests.get")
def test_search_channel3_products_success(mock_get):
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "products": [
            {
                "id": "prod_123",
                "title": "Minimalist Coffee Maker",
                "description": "Sleek black drip coffee machine",
                "price": 89.99,
                "currency": "USD",
                "image_url": "https://example.com/image.jpg",
                "product_url": "https://example.com/product",
                "merchant_name": "Brew Co"
            }
        ]
    }
    mock_get.return_value = mock_response

    query = ProductSearchQuery(query="coffee maker", max_price=100.0)
    results = search_channel3_products(query)

    assert len(results) == 1
    assert results[0].id == "prod_123"
    assert results[0].price == 89.99