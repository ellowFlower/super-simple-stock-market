from datetime import datetime

from src.entity.trade import Trade
from src.model.stock_symbol import StockSymbol
from src.repository.trade_repository import TradeRepository


class TradeService:
    def __init__(self, trade_repository: TradeRepository):
        self.trade_repository: TradeRepository = trade_repository

    def record_trade(self, trade: Trade) -> None:
        """
         :param trade: the trade to save
         """
        self.trade_repository.record_trade(trade)

    def get_trades_by_stock_and_time(self, stock_symbol: StockSymbol, time_from: datetime) -> list[Trade]:
        """
        :param stock_symbol: the symbol representing the stock to get the trades from
        :param time_from: the starting time from where to get the trades
        :return: trades after the given time (time_from) for a specific stock represented by the parameter stock_symbol
        """
        return self.trade_repository.get_trades_by_stock_and_time(stock_symbol, time_from)

    def get_volume_weighted_stock_price(self, time_from: datetime, stock_symbol: StockSymbol) -> float:
        trades: list[Trade] = self.get_trades_by_stock_and_time(stock_symbol, time_from)
        return sum(trade.price * trade.quantity for trade in trades) / sum(trade.quantity for trade in trades)
