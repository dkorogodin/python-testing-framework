from sqlalchemy import Column, Integer, String, Date

from src.core.api.service.payment.model.credit_card import CreditCard
from src.core.db.core.entity_manager import Base


class CreditCardEntity(Base):
    __tablename__ = "CreditCard"

    id = Column(Integer, primary_key=True, autoincrement=True)
    number = Column(String(50), nullable=False)
    expiry_date = Column(Date, nullable=False)
    cvv = Column(String(3), nullable=False)
    name_on_card = Column(String(50), nullable=False)

    def to_model(self) -> CreditCard:
        """Convert entity to Pydantic CreditCard model."""
        return CreditCard.model_validate(self)
