import pandas as pd


def filter_by_price(df, minimum_price):

    if df.empty:

        return df

    prices = (
        df["Price"]
        .astype(str)
        .str.replace("$", "", regex=False)
        .str.replace(",", "", regex=False)
    )

    df = df.copy()

    df["Price_Number"] = pd.to_numeric(
        prices,
        errors="coerce"
    )

    result = df[
        df["Price_Number"] >= minimum_price
    ]

    return result.drop(
        columns=["Price_Number"]
    )


def filter_by_change(df, minimum_change):

    if df.empty:

        return df

    df = df.copy()

    changes = (
        df["24h Change"]
        .astype(str)
        .str.replace("%", "", regex=False)
    )

    df["Change_Number"] = pd.to_numeric(
        changes,
        errors="coerce"
    )

    result = df[
        df["Change_Number"] >= minimum_change
    ]

    return result.drop(
        columns=["Change_Number"]
    )