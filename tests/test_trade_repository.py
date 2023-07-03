import unittest
from unittest.mock import MagicMock

from src.entity.trade import Trade
from src.model.trade_indicator import TradeIndicator
from src.repository.trade_repository import TradeRepository
from tests import test_data


class MyTestCase(unittest.TestCase):
    sut: TradeRepository

    def setUp(self) -> None:
        self.service_repository = MagicMock()
        self.sut = TradeRepository(self.service_repository)

    def test_record_trade(self):
        trade: Trade = Trade(quantity=100, indicator=TradeIndicator.BUY, price=10.0)

        self.sut.record_trade(trade, test_data.STOCK_POP)

        self.assertEqual(1, len(self.sut.fake_database), 'Trade was not recorded.')
        self.assertEqual(trade, self.sut.fake_database[0], 'Trade was not recorded.')
        self.service_repository.update.assert_called_once_with(test_data.STOCK_POP)


if __name__ == '__main__':
    unittest.main()
