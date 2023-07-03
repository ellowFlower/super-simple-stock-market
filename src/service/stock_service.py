import datetime
import math

from src.entity.stock import Stock
from src.repository.stock_repository import StockRepository


class StockService:
    def __init__(self, stock_repository: StockRepository):
        self.stock_repository: StockRepository = stock_repository

    def calculate_dividend_yield(self, stock: Stock, price: float) -> float:
        """
        :param stock: the stock to calculate the dividend yield from
        :param price: the price used for calculation
        :return: the dividend yield regarding the given stock and price
        """
        return stock.calculate_dividend_yield(price)

    def calculate_pe_ratio(self, stock: Stock, price: float) -> float:
        """
        :param stock: the stock to calculate the P/E ratio from
        :param price: the price used for calculation
        :return: the P/E ratio regarding the given stock and price
        """
        return stock.calculate_pe_ratio(price)

    def get_volume_weighted_stock_price(self, past_min: int, stock: Stock) -> float:
        """
        :param past_min: the number of minutes to look back for trades
        :param stock: the stock to calculate the volume weighted stock price from
        :return: for the given stock the volume weighted stock price based on trades in past_min minutes
        """
        trades_past_x_min = [trade for trade in stock.trades
                             if trade.timestamp >= datetime.datetime.now() - datetime.timedelta(minutes=past_min)]
        # TODO division by zero
        return sum(trade.price * trade.quantity for trade in trades_past_x_min) / sum(
            trade.quantity for trade in trades_past_x_min)

    def get_all_stocks(self):
        return self.stock_repository.get_all_stocks()

    def get_gbce_all_share_index(self):
        """
        :return: the geometric mean of the volume weighted stock prices for all stocks
        """
        stocks = self.stock_repository.get_all_stocks()
        stocks_vwsp = [self.get_volume_weighted_stock_price(datetime.timedelta.max.days, stock) for stock in stocks
                       if stock.trades]
        # TODO division by zero
        return round(pow(math.prod(stocks_vwsp), 1 / len(stocks_vwsp)), 5)
