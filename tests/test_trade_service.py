import unittest
from datetime import datetime
from unittest import mock
from unittest.mock import MagicMock

from src.entity.trade import Trade
from src.model.trade_indicator import TradeIndicator
from src.service.trade_service import TradeService
from tests import test_data


class MyTestCase(unittest.TestCase):
    sut: TradeService
    trade_repository_mock: MagicMock

    @classmethod
    @mock.patch('src.entity.trade.datetime')
    def setUpClass(cls, time_trades_executed):
        # trades at 20:00
        time_trades_executed.datetime.now = mock.Mock(return_value=datetime(2023, 7, 1, 20, 0, 0))
        cls.trade_pop_20 = Trade(quantity=100, indicator=TradeIndicator.SELL, price=10.0)
        cls.trade_tea_20 = Trade(quantity=100, indicator=TradeIndicator.BUY, price=10.0)
        # trades at 21:00
        time_trades_executed.datetime.now = mock.Mock(return_value=datetime(2023, 7, 1, 21, 0, 0))
        cls.trade_pop_21_1 = Trade(quantity=2, indicator=TradeIndicator.SELL, price=20.0)
        cls.trade_pop_21_2 = Trade(quantity=1, indicator=TradeIndicator.BUY, price=17.0)
        # various times
        cls.time_20_30 = datetime(2023, 7, 1, 20, 30, 0)
        cls.time_19_55: datetime = datetime(2023, 7, 1, 19, 55, 0)

    def setUp(self) -> None:
        self.trade_repository_mock = MagicMock()
        self.sut = TradeService(self.trade_repository_mock, MagicMock())

    def test_record_trade(self):
        self.sut.record_trade(self.trade_pop_20, test_data.STOCK_POP)
        self.trade_repository_mock.record_trade.assert_called_once_with(self.trade_pop_20, test_data.STOCK_POP)

if __name__ == '__main__':
    unittest.main()
