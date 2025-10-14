from src.core.api.service.product.model.product import Product
from src.core.db.client.product.dao.product_dao import ProductDao


class ProductdbClient:
    def __init__(self, session):
        self.session = session
        self.product_dao = ProductDao(session)

    # ------------------- Product -------------------
    def get_all_products(self) -> list[Product]:
        """Fetch all Product records."""
        return [product.to_model() for product in self.product_dao.get_all()]

    def get_product_by_id(self, product_id: int) -> Product | None:
        """Fetch Product by ID."""
        return self.product_dao.get(product_id).to_model()
