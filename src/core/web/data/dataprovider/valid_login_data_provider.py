from src.core.data.factory.payment.payments_constant_data_builder import PaymentsConstantDataBuilder
from src.core.data.factory.payment.payments_factory import PaymentsFactory
from src.core.data.factory.product.products_constant_data_builder import ProductsConstantDataBuilder
from src.core.data.factory.product.products_factory import ProductsFactory


def valid_login_data():
    """Provides valid login data combining product and payment info."""

    return [
        (
            ProductsFactory.get_random(ProductsConstantDataBuilder()),
            PaymentsFactory.get_random(PaymentsConstantDataBuilder())
        )
    ]
