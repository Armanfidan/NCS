from typing import Dict, List
from stock import Stock


class Exchange:
    def __init__(self, name: str, currency: str, spread: int):
        self.__name = name
        self.__currency = currency
        self.__spread = spread
        self.__stocks_and_prices: Dict[Stock, List[int]] = {}

    def get_name(self):
        return self.__name

    def get_currency(self):
        return self.__currency

    def add_stock(self, stock: Stock):
        if not stock.get_currency():
            print("Have you forgotten to implement the Stock.get_currency() method?")
            exit(1)
        if stock.get_currency() != self.__currency:
            print("Please only add stocks traded on the same currency as the exchange's.")
        self.__stocks_and_prices[stock] = [stock.get_price()]

    def update_stock_price(self, stock: Stock):
        self.__stocks_and_prices[stock].append(stock.update_price())

    def update_all(self):
        for stock in self.__stocks_and_prices.keys():
            self.update_stock_price(stock)

    def get_ask_price(self, stock):
        return self.__stocks_and_prices[stock][-1] + self.__spread

    def get_bid_price(self, stock):
        return self.__stocks_and_prices[stock][-1] - self.__spread

    def get_price_history(self, stock):
        return self.__stocks_and_prices[stock]

    def get_all_histories(self):
        return self.__stocks_and_prices

    def get_stocks(self):
        return list(self.__stocks_and_prices.keys())

    def get_time_average(self, stock):
        """
        Return the time average, or E[stock] of the stock requested.
        If stock is not listed on the exchange, return -1.
        :param stock: The stock whose time average should be returned.
        :return: The time average of the price of that stock, or -1 if stock is not listed on the exchange.
        """
        pass

    def get_variance(self, stock):
        """
        Return the variance of the requested stock, given by formula E[stock²] - E[stock]².
        If stock is not listed on the exchange, return -1.
        :param stock: The stock whose variance should be returned.
        :return: The variance of the price of that stock, or -1 if stock is not listed on the exchange.
        """
        pass

    def get_stock_with_highest_peak_price(self):
        """
        Go through the stock prices throughout the day, find the peak stock price, return the stock and the price.
        :return: The stock with the highest peak price, and the highest peak price.
        """

    def highest_possible_profit(self, stock):
        """
        [DIFFICULT]
        Find the highest possible profit a trader can make by buying and selling the requested stock, with the given
        histories.
        If the stock is not traded in the exchange, return -1.
        :return: Highest possible profit or -1 if stock is not traded in exchange.
        """

    def lowest_possible_profit(self, stock):
        """
        [DIFFICULT]
        Find the lowest possible profit a trader can make by buying and selling the requested stock, with the given
        histories.
        If the stock is not traded in the exchange, return -1.
        :return: Lowest possible profit or -1 if stock is not traded in exchange.
        """
