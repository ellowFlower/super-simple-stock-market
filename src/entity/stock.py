from abc import ABC, abstractmethod

from src.model.stock_symbol import StockSymbol


class Stock(ABC):
    """
        Representing a stock.
    """

    def __init__(self,
                 symbol: StockSymbol,
                 last_dividend: float,
                 par_value: float
                 ):
        self.symbol: StockSymbol = symbol
        self.last_dividend: float = last_dividend
        self.par_value = par_value

    @abstractmethod
    def calculate_dividend_yield(self, price: float) -> float:
        """
        :param price: the price used for the calculation
        :return: the dividend yield regarding the used stock and price
        """
        pass
