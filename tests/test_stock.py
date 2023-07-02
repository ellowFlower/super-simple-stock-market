import unittest

from src.entity.stock import Stock
from src.entity.stock_common import StockCommon
from src.entity.stock_preferred import StockPreferred
from src.model.stock_symbol import StockSymbol


class TestStock(unittest.TestCase):
    def test_eq(self):
        stock_tea1: Stock = StockCommon(symbol=StockSymbol.TEA, par_value=100.0, last_dividend=0.0)
        stock_tea2: Stock = StockCommon(symbol=StockSymbol.TEA, par_value=100.0, last_dividend=5.0)
        stock_gin: Stock = StockPreferred(
            symbol=StockSymbol.GIN, par_value=100.0, last_dividend=8.0, fixed_dividend=0.02
        )

        self.assertEqual(stock_tea1, stock_tea1, 'Stocks are equal.')
        self.assertNotEqual(stock_tea1, stock_tea2, 'Stocks are not equal.')
        self.assertNotEqual(stock_tea1, stock_gin, 'Stocks are not equal.')


if __name__ == '__main__':
    unittest.main()
