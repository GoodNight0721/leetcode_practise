import pandas as pd

# ============================================================
# Practice 4 — Trade Execution Analysis
#
# Question:
# You are given two asynchronous datasets:
#
# 1. trades:
#    - time
#    - ticker
#    - side
#    - trade_price
#    - qty
#
# 2. quotes:
#    - time
#    - ticker
#    - bid
#    - ask
#
# Tasks:
#
# 1. For each trade, attach the most recent quote for the same
#    ticker at or before the trade time.
#
# 2. A quote can only be used if it is no more than 5 minutes old.
#    Otherwise, the trade should have no matched quote.
#
# 3. Create:
#
#       mid = (bid + ask) / 2
#
# 4. Create execution_cost:
#
#       BUY:
#           execution_cost = trade_price - mid
#
#       SELL:
#           execution_cost = mid - trade_price
#
#    A larger positive execution_cost means worse execution.
#
# 5. Calculate the average execution cost for each ticker.
#
# Final output should conceptually look like:
#
#       ticker    avg_execution_cost
#       AAPL      ...
#       MSFT      ...
#
# Hint:
# Think about:
# - exact vs inexact merge
# - merge_asof
# - by="ticker"
# - tolerance
# - groupby
# - how unmatched quotes / NaN values should be handled
# ============================================================


trades = pd.DataFrame({
    "time": pd.to_datetime([
        "2026-08-27 09:31:00",
        "2026-08-27 09:32:00",
        "2026-08-27 09:35:00",
        "2026-08-27 09:37:00",
        "2026-08-27 09:45:00"
    ]),
    "ticker": ["AAPL", "MSFT", "AAPL", "MSFT", "AAPL"],
    "side": ["BUY", "BUY", "SELL", "SELL", "BUY"],
    "trade_price": [100.4, 200.5, 101.2, 201.8, 103.0],
    "qty": [100, 50, 200, 80, 120]
})


quotes = pd.DataFrame({
    "time": pd.to_datetime([
        "2026-08-27 09:30:00",
        "2026-08-27 09:30:30",
        "2026-08-27 09:33:00",
        "2026-08-27 09:34:00",
        "2026-08-27 09:36:00"
    ]),
    "ticker": ["AAPL", "MSFT", "AAPL", "MSFT", "MSFT"],
    "bid": [100.0, 200.0, 101.0, 201.0, 201.5],
    "ask": [100.2, 200.4, 101.4, 201.4, 201.9]
})


# ============================================================
# Write your solution below
# ============================================================

# Step 1:
# Match each trade with the latest valid quote.
merged = pd.merge_asof(
    trades.sort_values("time"),
    quotes.sort_values('time'),
    on='time',
    by='ticker',
    tolerance=pd.Timedelta(minutes=5),
    direction='backward'
).dropna(subset=['bid', 'ask'])

# Step 2:
# Calculate mid price.
merged['mid'] = (merged['bid'] + merged['ask']) / 2

# Step 3:
# Calculate execution_cost depending on BUY / SELL.
merged.loc[merged['side'] == 'BUY', 'execution_cost'] = merged['trade_price'] - merged['mid']
merged.loc[merged['side'] == 'SELL', 'execution_cost'] = merged['mid'] - merged['trade_price']
print(merged)

# Step 4:
# Calculate average execution cost for each ticker.
merged = merged.groupby('ticker', as_index=False)['execution_cost'].mean().rename(columns={'execution_cost': 'avg_execution_cost'})

# Step 5:
# Print your intermediate result and final result if useful.
print(merged)

