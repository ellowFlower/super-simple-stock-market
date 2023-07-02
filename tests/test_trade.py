import unittest

from src.entity.trade import Trade
from src.model.trade_indicator import TradeIndicator
from tests.test_data import STOCK_TEA


class MyTestCase(unittest.TestCase):
    def test_eq(self):
        trade1: Trade = Trade(quantity=100, indicator=TradeIndicator.BUY, price=10.0, stock=STOCK_TEA)
        trade2: Trade = Trade(quantity=100, indicator=TradeIndicator.BUY, price=10.0, stock=STOCK_TEA)

        self.assertNotEqual(trade1, trade2)


if __name__ == '__main__':
    unittest.main()
