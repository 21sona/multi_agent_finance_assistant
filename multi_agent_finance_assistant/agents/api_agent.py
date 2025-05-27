import yfinance as yf

def get_asia_tech_data():
    tickers = ['TSM', 'SSNLF']  # TSMC, Samsung (OTC)
    data = {}
    for ticker in tickers:
        stock = yf.Ticker(ticker)
        hist = stock.history(period='2d')
        earnings = stock.earnings_dates
        data[ticker] = {
            'price_data': hist,
            'earnings': earnings
        }
    return data