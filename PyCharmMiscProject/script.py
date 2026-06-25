import os
import pandas as pd
import yfinance as yf

CACHE_FILE = "team_2024.csv"


def get_team_data():
    if os.path.exists(CACHE_FILE):
        print("Loading saved data from CSV...")
        return pd.read_csv(CACHE_FILE, index_col=0, parse_dates=True)

    print("Downloading  data...")

    df = yf.download(
        "TEAM",
        start="2020-01-01",
        auto_adjust=False,
        multi_level_index=False,
        progress=False,
        threads=False,
    )

    if df.empty:
        raise RuntimeError(
            "Download failed. Yahoo may be rate-limiting you. Try again later."
        )

    df.to_csv(CACHE_FILE)
    return df


df = get_team_data()
#SHIFTING THINGS
#df["Close_shifted_1"] = df["Close"].shift(1)
#df["factor"] = df["Adj Close"] / df["Close"]

print(df.head(5000))