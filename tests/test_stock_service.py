import unittest

from src.entity.stock import Stock
from src.entity.stock_common import StockCommon
from src.entity.stock_preferred import StockPreferred
from src.model.stock_symbol import StockSymbol
from src.service.stock_service import StockService


class TestStockService(unittest.TestCase):
    sut: StockService

    @classmethod
    def setUpClass(cls):
        cls.sut = StockService()

    def test_calculate_dividend_yield_common_last_dividend_0(self):
        stock_common: Stock = StockCommon(
            symbol=StockSymbol.TEA,
            last_dividend=0.0,
            par_value=100.0,
        )
        price: float = 40.0
        result: float = self.sut.calculate_dividend_yield(stock_common, price)
        self.assertEqual(result, 0, 'Dividend yield wrong.')

    def test_calculate_dividend_yield_common(self):
        stock_common: Stock = StockCommon(
            symbol=StockSymbol.TEA,
            par_value=100.0,
            last_dividend=8.0
        )
        price: float = 31.62
        result: float = self.sut.calculate_dividend_yield(stock_common, price)
        self.assertEqual(result, 0.25300, 'Dividend yield wrong.')

    def test_calculate_dividend_yield_preferred(self):
        stock_preferred: Stock = StockPreferred(
            symbol=StockSymbol.GIN,
            par_value=100.0,
            last_dividend=8.0,
            fixed_dividend=0.02
        )
        price: float = 16.0
        result: float = self.sut.calculate_dividend_yield(stock_preferred, price)
        self.assertEqual(result, 0.125, 'Dividend yield wrong.')


if __name__ == '__main__':
    unittest.main()
