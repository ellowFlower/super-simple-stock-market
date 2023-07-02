import unittest
from datetime import datetime
from unittest import mock
from unittest.mock import MagicMock

from src.entity.trade import Trade
from src.model.stock_symbol import StockSymbol
from src.model.trade_indicator import TradeIndicator
from src.service.trade_service import TradeService
from tests.test_data import STOCK_POP


class MyTestCase(unittest.TestCase):
    sut: TradeService
    trade_repository_mock: MagicMock

    @classmethod
    @mock.patch('src.entity.trade.datetime')
    def setUpClass(cls, time_trades_executed):
        # trades at 20:00
        time_trades_executed.datetime.now = mock.Mock(return_value=datetime(2023, 7, 1, 20, 0, 0))
        cls.trade_pop_20 = Trade(quantity=100, indicator=TradeIndicator.SELL, price=10.0, stock=STOCK_POP)
        # trades at 21:00
        time_trades_executed.datetime.now = mock.Mock(return_value=datetime(2023, 7, 1, 21, 0, 0))
        cls.trade_pop_21_1 = Trade(quantity=2, indicator=TradeIndicator.SELL, price=20.0, stock=STOCK_POP)
        cls.trade_pop_21_2 = Trade(quantity=1, indicator=TradeIndicator.BUY, price=17.0, stock=STOCK_POP)
        # various times
        cls.time_20_30 = datetime(2023, 7, 1, 20, 30, 0)

    def setUp(self) -> None:
        self.trade_repository_mock = MagicMock()
        self.sut = TradeService(self.trade_repository_mock)

    # record one trade and get it back
    @mock.patch('src.entity.trade.datetime')
    def test_record_and_get_trade(self, time_trades_executed):
        time_trades_executed.datetime.now = mock.Mock(return_value=datetime(2023, 7, 1, 20, 0, 0))
        trade_pop_20: Trade = Trade(quantity=100, indicator=TradeIndicator.SELL, price=10.0, stock=STOCK_POP)
        time_19_55: datetime = datetime(2023, 7, 1, 19, 55, 0)
        self.trade_repository_mock.get_trades_by_stock_and_time.return_value = [trade_pop_20]

        self.sut.record_trade(trade_pop_20)
        result: list[Trade] = self.sut.get_trades_by_stock_and_time(StockSymbol.POP, time_19_55)

        self.trade_repository_mock.record_trade.assert_called_once_with(trade_pop_20)
        self.assertEqual(len(result), 1, 'get_trades_by_stock_and_time should return one trade')
        self.assertEqual(result[0], trade_pop_20, 'get_trades_by_stock_and_time should return trade_pop_20')

    def test_get_volume_weighted_stock_price(self):
        self.trade_repository_mock.get_trades_by_stock_and_time.return_value = [
            self.trade_pop_21_1, self.trade_pop_21_2
        ]
        result: float = self.sut.get_volume_weighted_stock_price(self.time_20_30, StockSymbol.POP)
        self.assertEqual(19, result, 'Volume weighted stock price is wrong.')


if __name__ == '__main__':
    unittest.main()
