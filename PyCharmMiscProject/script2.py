import os
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

CACHE_FILE = "aapl_2020.csv"

df = yf.download(
    "AAPL",
    start="2020-01-01",
    auto_adjust=False,
    multi_level_index=False,
    progress=False,
    threads=False,
)

def get_aapl_data():
    if os.path.exists(CACHE_FILE):
        print("Loading saved AAPL data from CSV...")
        return pd.read_csv(CACHE_FILE, index_col=0, parse_dates=True)

    print("Downloading AAPL data...")


    if df.empty:
        raise RuntimeError(
            "Download failed. Yahoo may be rate-limiting you. "
            "Wait 30–60 minutes, then try again."
        )

    df.to_csv(CACHE_FILE)
    return df


def main():
    df = get_aapl_data()

    df["Close_shifted_1"] = df["Close"].shift(1)
    df["factor"] = df["Adj Close"] / df["Close"]

    print(df.tail())

    plt.figure(figsize=(12, 6))
    plt.plot(df.index, df["Close"], label="Close")
    plt.plot(df.index, df["Close_shifted_1"], label="Close shifted by 1", alpha=0.7)

    plt.title("AAPL Close Price")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    plt.show()


if __name__ == "__main__":
    main()
