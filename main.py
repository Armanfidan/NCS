from exchange import Exchange
from stock import Stock
from trader import Trader

import matplotlib

matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.animation import FuncAnimation
from functools import reduce


def run(exchange: Exchange, duration: int = 50, trader: Trader = None, buy_limits: dict = None, sell_limits: dict = None):
    fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(6, 5))

    plt.xlabel("Time (units)")
    plt.ylabel("Stock prices ({})".format(exchange.get_currency()))
    plt.title("Stock prices in the {}".format(exchange.get_name()))
            
    x = []
    x_var = iter(range(duration))
    x.append(next(x_var))

    lines = []
    for stock in exchange.get_stocks():
        lobj = axes.plot([], [], label=str(stock), lw=2)[0]
        lines.append(lobj)
    plt.legend()

    def animate(i):
        try:
            x.append(next(x_var))
            exchange.update_all()
            if trader and sell_limits:
                for stock in sell_limits:
                    if type(stock) == Stock and trader.limit_sell(stock, sell_limits[stock]) == 0:
                        print("Sold {} for {}.".format(stock, exchange.get_bid_price(stock)))
            if trader and buy_limits:
                for stock in buy_limits:
                    if type(stock) == Stock and trader.limit_buy(stock, buy_limits[stock]) == 0:
                        print("Bought {} for {}.".format(stock, exchange.get_ask_price(stock)))
                print("Current balance of {} is {} {}.".format(trader.get_name(), exchange.get_currency(), trader.get_balance()))
        except StopIteration:
            plt.savefig('plot.png', bbox_inches='tight')
            plt.close()
        y: list = list(exchange.get_all_histories().values())
        for lnum, line in enumerate(lines):
            line.set_data(x, y[lnum])
            _max = reduce(max, reduce(lambda a, b: a + b, y))
        axes.set_xlim(0, len(x))
        axes.set_ylim(-5, _max + 5)
        return lines

    _ = FuncAnimation(fig, animate, interval=80, frames=duration - 1)
    plt.show()
    _ = plt.imshow(mpimg.imread('plot.png'), aspect='equal')
    plt.axis('off')
    plt.show(block=False)
    print("End of simulation: time={}".format(duration))


def main():
    nyse = Exchange('New York Stock Exchange', 'USD', spread=5)
    goog = Stock('Google', 'USD', 'GOOG')
    nyse.add_stock(goog)
    meta = Stock('Meta', 'USD', 'META')
    nyse.add_stock(meta)
    amzn = Stock('Amazon', 'USD', 'AMZN')
    nyse.add_stock(amzn)

    # Exercise 0: Replace this with your name and make up a book name.
    trader = Trader("\"Your Name\"", "some_book", 1000, nyse)

    print("Hi {}, welcome to the {}! The stocks being traded are {}.".format(
        trader.get_name(), nyse.get_name(),
        ', '.join(list(map(str, nyse.get_stocks())))))

    # Exercise 1: Run the main function, implement the missing method and see how the stock prices change!
    run(nyse)

    # Exercise 2: Try adding a new exchange, then research some tickers and experiment with adding new stocks.
    # Question:   What happens when you try to trade the stock on the wrong exchange, or use a different currency than that of the exchange?

    # Exercise 3: Implement all getter functions to access class data. This practice is encapsulation!

    # Exercise 4: Implement the buy/sell functions. Once this is complete, uncomment the below and start trading!
    # run(nyse, duration=50)
    # trader.buy(goog, 10)
    # trader.buy(amzn, 10)
    # trader.sell(goog, 5)
    # trader.sell(goog, 7)
    # trader.sell(meta, 12)
    # print(trader.get_balance())
    # Observe the trader's balance and portfolio after each buy and sell - do they change like they should?
    # Some of these might fail even if you implement the functions correctly - why is that?
    # You can remove this print statement after you implement the buy and sell functions:)
    print("Implement the necessary functions to start trading!")

    # Exercise 5: Implement the limit buy and limit sell functions. After this, you can simply uncomment the below code snippet to see how the balance is changing at every step!
    # run(nyse, duration=200, trader=trader, buy_limits={goog: 5, meta: 10, amzn: 20}, sell_limits={goog: 50, meta: 40, amzn: 65})
    # Try changing these limits - how does the trader's balance change?


if __name__ == '__main__':
    main()
