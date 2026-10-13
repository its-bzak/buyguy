from pydantic import BaseModel, HttpUrl, Field

class Product(BaseModel):
    id: str
    title: str
    description: str | None = None
    price: float = Field(..., ge=0)
    currency: str = "USD"
    image_url: HttpUrl
    product_url: HttpUrl
    merchant_name: str | None = None

class ProductSearchQuery(BaseModel):
    query: str
    max_price: float | None = None
    limit: int = Field(default=5, ge=1, le=20)