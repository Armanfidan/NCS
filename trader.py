from typing import Dict
from stock import Stock
from exchange import Exchange


class Trader:
    def __init__(self, name: str, book: str, initial_balance: int, exchange: Exchange):
        self.__name = name  # The trader's name
        self.__book = book  # The trader's book, or "code"
        self.__balance = initial_balance  # We start with some savings!
        self.__portfolio: Dict[Stock, int] = {}
        self.__exchange = exchange  # The exchange the trader is trading on.

    def get_book(self):
        """
        :return: The trader's book (code).
        """

    def get_name(self):
        """
        :return: The trader's name.
        """
        return self.__name

    def get_balance(self):
        """
        :return: The trader's balance.
        """

    def get_stock_shares(self):
        """
        :return: The number of shares of the stock if present in the portfolio, or 0 if not present.
        """

    def get_portfolio(self):
        """
        :return: The trader's portfolio.
        """

    def get_exchange(self):
        """
        :return: The name of the exchange that the trader is trading on.
        """

    def buy(self, stock: Stock, number_of_shares: int):
        """
        The buy function, This function should:
            - Capture the current ASK price of a stock from the exchange, multiply it by the number of shares requested
              and add it to the trader's balance
            - Add the specified number of shares of the stock to the trader's portfolio
            - If the trade was successful, return 0,
            - If the trader's balance was too low to buy the specified number of shares of the stock,
              print "Low balance" and return 1.
        :return: 0 (if the trade was successful) or 1 (if the balance was low)
        """

    def sell(self, stock: Stock, number_of_shares: int):
        """
        Similar to the buy function. This function should:
            - Check if the  stock is in the trader's portfolio and, if so, check if the trader holds enough shares.
            - If so, capture the stock's BID price from the exchange, multiply it by the number of shares and
              subtract it from the balance.
            - Remove the specified number of shares of the stock from the trader's portfolio,
            - If there are 0 shares of the stock left in the portfolio, remove the stock from the portfolio.
            - If the stock was sold, return 0,
            - If the trader didn't have enough shares of the stock, print "Low balance" and return 1.
        :return: 0 (if the trade was successful) or 1 (if not enough shares of the stock were in the portfolio)
        """

    def limit_buy(self, stock: Stock, number_of_shares: int, limit: int):
        """
        Buy the requested number of the selected stock if the stock price is lower than the limit.
        """

    def limit_sell(self, stock: Stock, number_of_shares: int, limit: int):
        """
        Sell the requested number of the selected stock if the stock price is higher than the limit.
        """
