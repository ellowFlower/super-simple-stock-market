from src.entity.stock_common import StockCommon
from src.entity.stock_preferred import StockPreferred
from src.model.stock_symbol import StockSymbol

STOCK_TEA = StockCommon(symbol=StockSymbol.TEA, par_value=100.0, last_dividend=0.0)
STOCK_POP = StockCommon(symbol=StockSymbol.POP, par_value=100.0, last_dividend=8.0)
STOCK_ALE = StockCommon(symbol=StockSymbol.ALE, par_value=60.0, last_dividend=23.0)
STOCK_GIN = StockPreferred(symbol=StockSymbol.GIN, par_value=100.0, last_dividend=8.0, fixed_dividend=0.02)
STOCK_JOE = StockCommon(symbol=StockSymbol.JOE, par_value=250.0, last_dividend=13.0)
