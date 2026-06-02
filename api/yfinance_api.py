import yfinance as yf

FIELDS = [
    "currentPrice", "previousClose", "open", "dayLow", "dayHigh",
    "regularMarketChangePercent", "bid", "ask", "currency",
    "volume", "averageVolume", "averageVolume10days",
    "fiftyTwoWeekHigh", "fiftyTwoWeekLow", "fiftyTwoWeekChangePercent",
    "fiftyDayAverage", "twoHundredDayAverage", "marketCap",
    "priceToBook", "pegRatio", "dividendRate", "dividendYield",
    "payoutRatio", "trailingEps", "forwardEps", "earningsGrowth",
    "revenueGrowth", "profitMargins", "grossMargins",
    "recommendationKey", "recommendationMean", "targetMeanPrice",
    "targetHighPrice", "targetLowPrice", "numberOfAnalystOpinions",
    "shortName", "longName", "sector", "industry",
    "fullTimeEmployees", "website", "beta", "shortRatio",
    "sharesShort", "returnOnEquity", "freeCashflow",
    "quickRatio", "debtToEquity"
]

class YFinance:
    def __init__(self):
        pass

    def fetch_stocks(self, stock_ids: list, currencies: list):
        try:
            results = {}
            for stocks in stock_ids:
                ticker = yf.Ticker(stocks)
                info = ticker.info
                results[stocks] = {key: info.get(key) for key in FIELDS}
            return results
        except Exception as e:
            print(f"Fehler beim API-Call: {e}")
            return None


