from sqlalchemy import Column, Integer, String

from src.core.api.service.payment.model.shipping_info import ShippingInfo
from src.core.db.core.entity_manager import Base


class ShippingInfoEntity(Base):
    __tablename__ = "ShippingInfo"

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(50), nullable=False)
    country = Column(String(50), nullable=False)

    def to_model(self) -> ShippingInfo:
        """Convert entity to Pydantic ShippingInfo model."""
        return ShippingInfo.model_validate(self)
