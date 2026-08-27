import pandas as pd

trades = pd.DataFrame({
    "time": pd.to_datetime([
        "2026-08-27 09:31:00",
        "2026-08-27 09:36:00",
        "2026-08-27 09:45:00"
    ]),
    "ticker": ["AAPL", "AAPL", "AAPL"],
    "qty": [100, 200, 150]
})

quotes = pd.DataFrame({
    "time": pd.to_datetime([
        "2026-08-27 09:30:00",
        "2026-08-27 09:33:00"
    ]),
    "ticker": ["AAPL", "AAPL"],
    "price": [100.0, 101.0]
})

merged = pd.merge_asof(
    trades.sort_values('time'),
    quotes.sort_values('time'),
    on='time',
    by='ticker',
    direction='backward',
    tolerance=pd.Timedelta('5min')
)

print(merged)
