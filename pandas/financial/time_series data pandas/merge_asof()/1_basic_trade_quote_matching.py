import pandas as pd

trades = pd.DataFrame({
    "time": pd.to_datetime([
        "2026-08-27 09:31:00",
        "2026-08-27 09:35:00",
        "2026-08-27 09:40:00"
    ]),
    "qty": [100, 200, 150]
})

quotes = pd.DataFrame({
    "time": pd.to_datetime([
        "2026-08-27 09:30:00",
        "2026-08-27 09:33:00",
        "2026-08-27 09:38:00"
    ]),
    "price": [10.0, 10.2, 10.5]
})

merged = pd.merge_asof(
    trades.sort_values('time'),
    quotes.sort_values('time'),
    on='time',
    direction='backward'
)

print(merged)
