import unittest

import test_data
from src.service.stock_service import StockService


class TestStockService(unittest.TestCase):
    sut: StockService

    @classmethod
    def setUpClass(cls):
        cls.sut = StockService()

    def test_calculate_dividend_yield_common_last_dividend_0(self):
        price: float = 40.0
        result: float = self.sut.calculate_dividend_yield(test_data.STOCK_TEA, price)
        self.assertEqual(result, 0, 'Dividend yield wrong.')

    def test_calculate_dividend_yield_common(self):
        price: float = 31.62
        result: float = self.sut.calculate_dividend_yield(test_data.STOCK_POP, price)
        self.assertEqual(result, 0.25300, 'Dividend yield wrong.')

    def test_calculate_dividend_yield_common_division_by_zero(self):
        price: float = 0.0
        with self.assertRaises(ZeroDivisionError):
            self.sut.calculate_dividend_yield(test_data.STOCK_POP, price)

    def test_calculate_dividend_yield_preferred_division_by_zero(self):
        price: float = 0.0
        with self.assertRaises(ZeroDivisionError):
            self.sut.calculate_dividend_yield(test_data.STOCK_GIN, price)

    def test_calculate_dividend_yield_preferred(self):
        price: float = 16.0
        result: float = self.sut.calculate_dividend_yield(test_data.STOCK_GIN, price)
        self.assertEqual(result, 0.125, 'Dividend yield wrong.')

    def test_calculate_pe_ratio(self):
        price: float = 19.0
        result: float = self.sut.calculate_pe_ratio(test_data.STOCK_GIN, price)
        self.assertEqual(result, 2.375, 'PE ratio wrong.')

    def test_calculate_pe_ratio_division_by_zero(self):
        price: float = 19.0
        with self.assertRaises(ZeroDivisionError):
            self.sut.calculate_pe_ratio(test_data.STOCK_TEA, price)


if __name__ == '__main__':
    unittest.main()
