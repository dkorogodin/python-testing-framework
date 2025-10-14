from sqlalchemy import Integer, Column, String, ForeignKey
from sqlalchemy.orm import relationship

from src.core.api.service.payment.model.payment import Payment
from src.core.db.core.entity_manager import Base


class PaymentEntity(Base):
    __tablename__ = "Payment"

    id = Column(Integer, primary_key=True, autoincrement=True)
    credit_card_id = Column(Integer, ForeignKey("CreditCard.id"))
    shipping_info_id = Column(Integer, ForeignKey("ShippingInfo.id"))
    coupon = Column(String(50), nullable=True)

    # Relationships
    credit_card = relationship("CreditCardEntity", lazy="joined")
    shipping_info = relationship("ShippingInfoEntity", lazy="joined")

    def to_model(self) -> Payment:
        """Convert entity to Pydantic Payment model."""
        return Payment.model_validate({
            "id": self.id,
            "credit_card": self.credit_card.to_model(),
            "shipping_info": self.shipping_info.to_model(),
            "coupon": self.coupon
        })
