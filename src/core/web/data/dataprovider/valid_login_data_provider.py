from src.core.api.service.payment.model.payment import Payment
from src.core.api.service.product.model.product import Product
from src.core.data.factory.payment.payments_constant_data_builder import PaymentsConstantDataBuilder
from src.core.data.factory.payment.payments_factory import PaymentsFactory
from src.core.data.factory.product.products_constant_data_builder import ProductsConstantDataBuilder
from src.core.data.factory.product.products_factory import ProductsFactory


def valid_login_data() -> list[tuple[Product | None, Payment | None]]:
    """Provides valid login data combining product and payment info."""

    return [
        (
            ProductsFactory.get_random(ProductsConstantDataBuilder()),
            PaymentsFactory.get_random(PaymentsConstantDataBuilder())
        )
    ]
