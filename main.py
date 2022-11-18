import time

from exchange import Exchange
from stock import Stock
import matplotlib.pyplot as plt


def run(exchange: Exchange, duration: int = 1000):
    for _ in range(duration):
        exchange.update_all()
        for history in list(exchange.get_all_histories().values()):
            plt.plot(history)
        plt.show()
        plt.clf()
        time.sleep(0.1)


def main():
    nyse = Exchange('NYSE', 'USD', spread=5)
    nyse.add_stock(Stock('Google', 'USD', 'GOOGL'))
    nyse.add_stock(Stock('Meta', 'USD', 'META'))
    nyse.add_stock(Stock('Amazon', 'USD', 'AMZN'))

    # Exercise 1: Run the main function, implement the method missing and see how the stock prices change!

    # Exercise 2: Try adding a new exchange, then research some tickers and experiment with adding new stocks.
    # Question:   What happens when you try to trade the stock on the wrong exchange, or use a different currency than
    # that of the exchange?

    run(nyse)


if __name__ == '__main__':
    main()
