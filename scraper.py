import requests


def scrape_crypto_data():

    url = "https://api.coingecko.com/api/v3/coins/markets"

    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 20,
        "page": 1,
        "sparkline": False
    }

    try:
        response = requests.get(
            url,
            params=params,
            timeout=15
        )

        response.raise_for_status()

        coins = response.json()

        data = []

        for rank, coin in enumerate(coins, start=1):

            data.append({
                "Rank": rank,
                "Name": coin["name"],
                "Symbol": coin["symbol"].upper(),
                "Price": coin["current_price"],
                "Market Cap": coin["market_cap"],
                "24h Change": coin["price_change_percentage_24h"]
            })

        print(f"{len(data)} cryptocurrency records collected.")

        return data

    except Exception as e:

        print("Error collecting cryptocurrency data:")
        print(e)

        return []