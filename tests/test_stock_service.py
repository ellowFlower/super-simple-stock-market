import unittest
from datetime import datetime, timedelta
from unittest import mock
from unittest.mock import MagicMock, patch

from src.entity.stock import Stock
from src.entity.trade import Trade
from src.exception.calculation_exception import CalculationException
from src.model.trade_indicator import TradeIndicator
from src.service.stock_service import StockService
from tests import test_data


class TestStockService(unittest.TestCase):
    sut: StockService

    @classmethod
    @mock.patch('src.entity.trade.datetime')
    def setUpClass(cls, time_now_mock):
        # trades at 20:00
        time_now_mock.datetime.now.return_value = datetime(2023, 7, 1, 20, 0, 0)
        cls.trade_pop_20 = Trade(quantity=20, indicator=TradeIndicator.SELL, price=20.0)
        cls.trade_ale_20_1 = Trade(quantity=10, indicator=TradeIndicator.BUY, price=15.0)
        cls.trade_ale_20_2 = Trade(quantity=10, indicator=TradeIndicator.BUY, price=9.0)
        cls.trade_gin_20 = Trade(quantity=19, indicator=TradeIndicator.BUY, price=26.0)
        cls.trade_joe_20 = Trade(quantity=5, indicator=TradeIndicator.BUY, price=300.0)
        # trades at 21:00
        time_now_mock.datetime.now = mock.Mock(return_value=datetime(2023, 7, 1, 21, 0, 0))
        cls.trade_pop_21_1 = Trade(quantity=2, indicator=TradeIndicator.SELL, price=20.0)
        cls.trade_pop_21_2 = Trade(quantity=1, indicator=TradeIndicator.BUY, price=17.0)

    @classmethod
    def tearDownClass(cls) -> None:
        patch.stopall()

    def setUp(self) -> None:
        stock_repository = MagicMock()
        self.sut = StockService(stock_repository)

    def test_calculate_dividend_yield_common_last_dividend_0(self):
        price: float = 40.0
        result: float = self.sut.calculate_dividend_yield(test_data.STOCK_TEA, price)
        self.assertEqual(0, result, 'Dividend yield wrong.')

    def test_calculate_dividend_yield_common(self):
        price: float = 31.62
        result: float = self.sut.calculate_dividend_yield(test_data.STOCK_POP, price)
        self.assertEqual(0.25300, result, 'Dividend yield wrong.')

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
        self.assertEqual(0.125, result, 'Dividend yield wrong.')

    def test_calculate_pe_ratio(self):
        price: float = 19.0
        result: float = self.sut.calculate_pe_ratio(test_data.STOCK_GIN, price)
        self.assertEqual(2.375, result, 'PE ratio wrong.')

    def test_calculate_pe_ratio_division_by_zero(self):
        price: float = 19.0
        with self.assertRaises(CalculationException):
            self.sut.calculate_pe_ratio(test_data.STOCK_TEA, price)

    @mock.patch('src.service.stock_service.datetime')
    def test_get_volume_weighted_stock_price(self, time_now_stock_service):
        timedelta_min = 5
        stock_pop: Stock = test_data.STOCK_POP
        stock_pop.trades = [
            self.trade_pop_20,
            self.trade_pop_21_1,
            self.trade_pop_21_2
        ]

        time_now_stock_service.datetime.now.return_value = datetime(2023, 7, 1, 21, 2, 0)
        time_now_stock_service.timedelta.return_value = timedelta(minutes=timedelta_min)
        result: float = self.sut.calculate_volume_weighted_stock_price(timedelta_min, stock_pop)
        self.assertEqual(19, result, 'Volume weighted stock price is wrong.')

    def test_get_gbce_all_share_index(self):
        stock_tea: Stock = test_data.STOCK_TEA
        stock_pop: Stock = test_data.STOCK_POP
        stock_pop.trades = [self.trade_pop_20, self.trade_pop_21_1, self.trade_pop_21_2]
        stock_ale: Stock = test_data.STOCK_ALE
        stock_ale.trades = [self.trade_ale_20_1, self.trade_ale_20_2]
        stock_gin: Stock = test_data.STOCK_GIN
        stock_gin.trades = [self.trade_gin_20]
        stock_joe: Stock = test_data.STOCK_JOE
        stock_joe.trades = [self.trade_joe_20]

        self.sut.stock_repository.get_all_stocks.return_value = [
            stock_tea, stock_pop, stock_ale, stock_gin, stock_joe
        ]

        result: float = self.sut.calculate_gbce_all_share_index()
        self.assertEqual(36.92887, result, 'GBCE all share index is wrong.')


if __name__ == '__main__':
    unittest.main()
