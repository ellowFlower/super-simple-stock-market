import datetime

from src.entity.trade import Trade
from src.model.stock_symbol import StockSymbol


class TradeRepository:
    fake_database: list[Trade] = []

    def record_trade(self, trade: Trade):
        list.append(self.fake_database, trade)

    def get_trades_by_stock_and_time(self, stock_symbol: StockSymbol, from_time: datetime) -> list[Trade]:
        """
        :param stock_symbol: stock to get trades for
        :param from_time: time point to get trades from
        :return: all trades for the given stock in the time after from_time
        """
        return [trade for trade in self.fake_database if trade.stock.symbol == stock_symbol
                and trade.timestamp >= from_time]
