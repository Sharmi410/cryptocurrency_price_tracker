from scraper import scrape_crypto_data
from tracker import save_data, read_history
from filter_data import filter_by_change


def main():

    print("=" * 60)
    print("       CRYPTOCURRENCY PRICE TRACKER")
    print("=" * 60)

    print("\nStarting data collection...\n")

    data = scrape_crypto_data()

    if not data:

        print("\nNo cryptocurrency data collected.")

        print("Please check:")
        print("1. Internet connection")
        print("2. CoinMarketCap availability")
        print("3. Selenium installation")

        return

    print("\nTop Cryptocurrency Data:\n")

    for coin in data:

        print(
            f"{coin['Rank']} | "
            f"{coin['Name']} | "
            f"{coin['Price']} | "
            f"{coin['24h Change']} | "
            f"{coin['Market Cap']}"
        )

    print("\nSaving data...\n")

    save_data(data)

    print("\nHistorical data:\n")

    history = read_history()

    if not history.empty:

        print(history.tail(10).to_string(index=False))

    print("\nProject completed successfully!")


if __name__ == "__main__":

    main()