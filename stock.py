from helpers import PriceGenerator


class Stock:
    """
    The Stock class, representing a very simplified stock that can only be traded on one exchange and in one currency.
    """
    def __init__(self, name: str, currency: str, ticker: str):
        self.__name: str = name
        self.__currency: str = currency
        self.__ticker: str = ticker
        self.__generator: PriceGenerator = PriceGenerator()
        self.__price: int = self.__generator.get_price()

    def update_price(self):
        """
        We randomly generate the stock's current price. This function updates the price. You don't need to touch this.
        """
        self.__price = self.__generator.generate()
        return self.__price

    def get_price(self):
        """
        :return: The stock's current price.
        """
        return self.__price

    def get_name(self):
        """
        :return: The stock's name.
        """

    def get_currency(self):
        """
        :return: The stock's currency.
        """
        return self.__currency

    def get_ticker(self):
        """
        :return: The stock's short code.
        """

    def __str__(self) -> str:
        return "{} ({})".format(self.__name, self.__ticker)
