import time

import numpy as np

from exchange import Exchange
from stock import Stock
from trader import Trader

import matplotlib; matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib.animation import FuncAnimation
from functools import reduce
import multiprocessing


def run(exchange: Exchange, duration: int = 50, trader: Trader = None, buy_limit: int = None, sell_limit: int = None):
    buys = []
    sells = []

    def simulate():
        fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(6, 5))
    
        plt.xlabel("Time (units)")
        plt.ylabel("Stock prices ({})".format(exchange.get_currency()))
        plt.title("Stock prices in the {}".format(exchange.get_name()))
    
        x = []
        x_var = iter(range(duration))
        x.append(next(x_var))
    
        lines = []
        for index in range(len(exchange.get_stocks())):
            lobj = axes.plot([], [], lw=2)[0]
            lines.append(lobj)
        
        def animate(i):
            try:
                x.append(next(x_var))
                exchange.update_all()
            except StopIteration:
                return lines
            y: list = list(exchange.get_all_histories().values())
            for lnum, line in enumerate(lines):
                line.set_data(x, y[lnum])
                _max = reduce(max, reduce(lambda a, b: a + b, y))
            axes.set_xlim(0, len(x))
            axes.set_ylim(-5, _max + 5)
            return lines
    
        
        anim = FuncAnimation(fig, animate, interval=100, frames=duration)
        plt.show()

    p = multiprocessing.Process(target=simulate)
    print(exchange.get_all_histories())
    p.start()
    time.sleep(5)
    print(exchange.get_all_histories())

    print("End of simulation: time =", duration)


def main():
    nyse = Exchange('New York Stock Exchange', 'USD', spread=5)
    goog = Stock('Google', 'USD', 'GOOG')
    nyse.add_stock(goog)
    meta = Stock('Meta', 'USD', 'META')
    nyse.add_stock(meta)
    amzn = Stock('Amazon', 'USD', 'AMZN')
    nyse.add_stock(amzn)

    # Exercise 0: Replace this with your name and make up a book name.
    trader = Trader("Your Name", "some_book", 1000, nyse)

    print("Hi {}, welcome to the {}! The stocks being traded are {}."
          .format(trader.get_name(), nyse.get_name(), ', '.join(list(map(str, nyse.get_stocks())))))

    # Exercise 1: Run the main function, implement the method missing and see how the stock prices change!
    run(nyse)

    # Exercise 2: Try adding a new exchange, then research some tickers and experiment with adding new stocks.
    # Question:   What happens when you try to trade the stock on the wrong exchange, or use a different currency than
    # that of the exchange?

    # Exercise 3: Implement all getter functions to access class data. This practice is encapsulation!

    # Exercise 4: Implement the buy/sell functions. Once this is complete, uncomment the below and start trading!
    # trader.buy(goog, 10)
    # trader.buy(goog, 10)
    # trader.sell(goog, 5)
    # trader.sell(goog, 7)
    # trader.sell(meta, 12)
    # Observe the trader's balance and portfolio after each buy and sell - do they change like they should?
    # Some of these might fail even if you implement the functions correctly - why is that?
    # You can remove this print statement after you implement the buy and sell functions:)
    print("Implement the necessary functions to start trading!")

    # Exercise 5: Implement the limit buy and limit sell functions. After this, you can set the limits in the beginning
    # and run the simulation - see how the balance is changing at every step!


if __name__ == '__main__':
    main()
