from sqlalchemy import Integer, Column, String

from src.core.api.service.product.model.product import Product
from src.core.db.core.entity_manager import Base


class ProductEntity(Base):
    __tablename__ = "Product"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))
    price = Column(Integer)
    details = Column(String(255))
    currency = Column(String(8), default="$")

    def to_model(self) -> Product:
        """Convert SQLAlchemy entity to Pydantic Product model."""
        return Product.model_validate(self)
