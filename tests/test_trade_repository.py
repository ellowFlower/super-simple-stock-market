import unittest
from datetime import datetime
from unittest import mock

from src.entity.trade import Trade
from src.model.trade_indicator import TradeIndicator
from src.repository.trade_repository import TradeRepository
from tests import test_data
from tests.test_data import STOCK_TEA, STOCK_POP


class MyTestCase(unittest.TestCase):
    sut: TradeRepository
    trade_pop_20: Trade
    trade_tea_20: Trade
    trade_pop_21: Trade
    time_19_55: datetime
    time_20_30: datetime

    @classmethod
    @mock.patch('src.entity.trade.datetime')
    def setUpClass(cls, time_trades_executed):
        time_trades_executed.datetime.now = mock.Mock(return_value=datetime(2023, 7, 1, 20, 0, 0))
        # trades at 20:00
        cls.trade_pop_20 = Trade(quantity=100, indicator=TradeIndicator.SELL, price=10.0, stock=STOCK_POP)
        cls.trade_tea_20 = Trade(quantity=100, indicator=TradeIndicator.BUY, price=10.0, stock=STOCK_TEA)
        # trade at 21:00
        time_trades_executed.datetime.now = mock.Mock(return_value=datetime(2023, 7, 1, 21, 0, 0))
        cls.trade_pop_21 = Trade(quantity=100, indicator=TradeIndicator.SELL, price=10.0, stock=STOCK_POP)
        # time 19:55
        cls.time_19_55 = datetime(2023, 7, 1, 19, 55, 0)
        cls.time_20_30 = datetime(2023, 7, 1, 20, 30, 0)

    def setUp(self) -> None:
        self.sut = TradeRepository()

    # two stocks, both in correct time range but only one has the correct stock.type
    def test_record_different_stocks(self):
        self.sut.record_trade(self.trade_tea_20)
        self.sut.record_trade(self.trade_pop_20)
        result: list = self.sut.get_trades_by_stock_and_time(test_data.STOCK_TEA, self.time_19_55)

        # only tea trade is returned (time would be ok for both)
        self.assertEqual(1, len(result))
        self.assertEqual(self.trade_tea_20, result[0])

    # two trades from same stock but only one is in correct time range
    def test_record_different_time(self):
        self.sut.record_trade(self.trade_pop_20)
        self.sut.record_trade(self.trade_pop_21)
        result: list = self.sut.get_trades_by_stock_and_time(test_data.STOCK_POP, self.time_20_30)

        # only trade from 21:00 is returned
        self.assertEqual(1, len(result))
        self.assertEqual(self.trade_pop_21, result[0])


if __name__ == '__main__':
    unittest.main()
