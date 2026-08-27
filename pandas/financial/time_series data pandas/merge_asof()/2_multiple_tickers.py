import pandas as pd

trades = pd.DataFrame({
    "time": pd.to_datetime([
        "2026-08-27 09:31:00",
        "2026-08-27 09:32:00",
        "2026-08-27 09:35:00",
        "2026-08-27 09:36:00"
    ]),
    "ticker": ["AAPL", "MSFT", "AAPL", "MSFT"],
    "qty": [100, 50, 200, 80]
})

quotes = pd.DataFrame({
    "time": pd.to_datetime([
        "2026-08-27 09:30:00",
        "2026-08-27 09:30:30",
        "2026-08-27 09:33:00",
        "2026-08-27 09:34:00"
    ]),
    "ticker": ["AAPL", "MSFT", "AAPL", "MSFT"],
    "price": [100.0, 200.0, 101.0, 202.0]
})

merged = pd.merge_asof(
    trades.sort_values('time'),
    quotes.sort_values('time'),
    on='time',
    direction='backward',
    by='ticker'
)

print(merged)