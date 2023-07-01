from src.entity.stock import Stock


class StockService:
    def calculate_dividend_yield(self, stock: Stock, price: float) -> float:
        """
        :param stock: the stock to calculate the dividend yield from
        :param price: the price used for calculation
        :return: the dividend yield regarding the given stock and price
        """
        try:
            return stock.calculate_dividend_yield(price)
        except ZeroDivisionError:
            # TODO
            pass


if __name__ == '__main__':
    stock_service: StockService = StockService()
