import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

from src import logger
from src.core.api.service.payment.model.credit_card import CreditCard
from src.core.api.service.payment.model.payment import Payment
from src.core.api.service.payment.model.shipping_info import ShippingInfo
from src.core.web.pageobject.common.web_base_logged_in_page import WebBaseLoggedInPage
from src.core.web.pageobject.order_confirmation_page import OrderConfirmationPage


class PaymentPage(WebBaseLoggedInPage):
    """Page object for the Payment Page."""
    CREDIT_CARD_FLD = (By.XPATH, "//div[text()='Credit Card Number ']//following-sibling::input")
    CVV_CODE_FLD = (By.XPATH, "//div[text()='CVV Code ']//following-sibling::input")
    NAME_ON_CARD_FLD = (By.XPATH, "//div[text()='Name on Card ']//following-sibling::input")
    EXPIRY_DATE_MONTH_MENU = (By.XPATH, "//div[text()='Expiry Date ']//following-sibling::select[1]")
    EXPIRY_DATE_YEAR_MENU = (By.XPATH, "//div[text()='Expiry Date ']//following-sibling::select[2]")
    APPLY_COUPON_FLD = (By.XPATH, "//div[text()='Apply Coupon ']//following-sibling::input")
    APPLY_COUPON_BTN = (By.XPATH, "//button[text()='Apply Coupon']")
    EMAIL_FLD = (By.XPATH, "//div[contains(@class,'user__name')]/label/following-sibling::input")
    SECURITY_COUNTRY_FLD = (By.CSS_SELECTOR, "[placeholder='Select Country']")
    PLACE_ORDER_BTN = (By.XPATH, "//a[text()='Place Order ']")
    SHIPPING_INFO_COUNTRY_MENU_ITEMS = (By.XPATH, "//div[contains(@class,'user__name')]//section//span")

    @allure.step("Fill in all payment details: '{1}'.")
    def fill_in_all_payment_details(self, payment: Payment) -> "PaymentPage":
        self.fill_in_credit_card(payment.credit_card)
        self.apply_coupon(payment.coupon)
        self.fill_in_shipping_info(payment.shipping_info)
        return self

    @allure.step("Fill in credit card data: '{1}'.")
    def fill_in_credit_card(self, credit_card: CreditCard) -> "PaymentPage":
        logger.info(f"Fill in '{credit_card}' credit card data.")
        self._fill_in_credit_card_number(credit_card.number)
        self._fill_in_credit_card_expiry_date(credit_card.expiry_date)
        self.element_actions.clear_field_then_type_text(self.CVV_CODE_FLD, credit_card.cvv)
        self.element_actions.clear_field_then_type_text(self.NAME_ON_CARD_FLD, credit_card.name_on_card)
        return self

    @allure.step("Fill in Shipping Info data: '{1}'.")
    def fill_in_shipping_info(self, shipping_info: ShippingInfo) -> "PaymentPage":
        logger.info(f"Fill in '{shipping_info}' Shipping Info data.")
        self._fill_in_shipping_info_email(shipping_info.email)
        self._fill_in_shipping_info_country(shipping_info.country)
        return self

    @allure.step("Apply coupon: '{1}'.")
    def apply_coupon(self, coupon: str | None) -> "PaymentPage":
        if coupon:
            logger.info(f"Apply '{coupon}' coupon.")
            self.element_actions.type_text(self.APPLY_COUPON_FLD, coupon)
            self.element_actions.click(self.APPLY_COUPON_BTN)
        return self

    @allure.step("Place order.")
    def place_order(self) -> OrderConfirmationPage:
        logger.info("Place order.")
        self.element_actions.click(self.PLACE_ORDER_BTN)
        return OrderConfirmationPage(self.driver)

    def _fill_in_credit_card_expiry_date(self, credit_card_expiry_date) -> "PaymentPage":
        """Fill in expiry month and year from a date object."""
        month = credit_card_expiry_date.month
        year = credit_card_expiry_date.year % 100
        Select(self.element_actions.find_element(self.EXPIRY_DATE_MONTH_MENU)).select_by_visible_text(str(month))
        Select(self.element_actions.find_element(self.EXPIRY_DATE_YEAR_MENU)).select_by_visible_text(str(year))
        return self

    def _fill_in_credit_card_number(self, number: str) -> "PaymentPage":
        self.element_actions.clear_field_then_type_text(self.CREDIT_CARD_FLD, number)
        return self

    def _fill_in_shipping_info_email(self, email: str) -> "PaymentPage":
        self.element_actions.clear_field_then_type_text(self.EMAIL_FLD, email)
        return self

    def _fill_in_shipping_info_country(self, country: str) -> "PaymentPage":
        """Selects a country from the dropdown menu."""
        prefix = country[:4]
        self.element_actions.type_text(self.SECURITY_COUNTRY_FLD, prefix)

        self.wait_until.elements_visible((By.XPATH, "//div[contains(@class,'user__name')]//section//span"))
        for item in self.element_actions.find_elements(self.SHIPPING_INFO_COUNTRY_MENU_ITEMS):
            self.element_actions.type_text(self.SECURITY_COUNTRY_FLD, Keys.DOWN)
            if item.text == country:
                self.element_actions.type_text(self.SECURITY_COUNTRY_FLD, Keys.ENTER)
                break

        assert self.element_actions.get_attribute(self.SECURITY_COUNTRY_FLD, "value") == country, \
            f"Expected country '{country}' not selected."
        return self

    def wait_until_page_loaded(self) -> None:
        self.wait_until.element_clickable(self.PLACE_ORDER_BTN)
