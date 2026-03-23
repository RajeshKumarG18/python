import matplotlib.pyplot as plt
import pandas as pd

# Sample data (define `df` so the script can run)
data = {
    "Day": [1, 2, 3, 4, 5],
    "Open": [10, 12, 11, 13, 12],
    "High": [12, 13, 12, 14, 13],
    "Low": [9, 11, 10, 12, 11],
    "Close": [11, 12, 12, 13, 12]
}
df = pd.DataFrame(data)

# Moving Average
df["MA"] = df["Close"].rolling(window=3).mean()

plt.figure()

# Candlestick width
width = 0.6

for i in range(len(df)):
    # Draw High-Low line (wick)
    plt.plot(
        [df["Day"][i], df["Day"][i]],
        [df["Low"][i], df["High"][i]],
        color="black"
    )
    
    # Draw candle body
    plt.bar(
        df["Day"][i],
        abs(df["Close"][i] - df["Open"][i]),
        width=width,
        bottom=min(df["Open"][i], df["Close"][i]),
        color="green" if df["Close"][i] >= df["Open"][i] else "red"
    )

# Plot Moving Average
plt.plot(df["Day"], df["MA"], color="blue", label="MA (3)")

plt.title("Candlestick Type Chart with Moving Average")
plt.xlabel("Day")
plt.ylabel("Price")
plt.legend()
plt.show()