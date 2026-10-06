import os
import pandas as pd

from config import CSV_FILE


def save_data(data):

    if not data:

        print("No data available to save.")

        return

    df = pd.DataFrame(data)

    folder = os.path.dirname(CSV_FILE)

    if folder:

        os.makedirs(folder, exist_ok=True)

    file_exists = os.path.exists(CSV_FILE)

    df.to_csv(
        CSV_FILE,
        mode="a",
        header=not file_exists,
        index=False
    )

    print(f"Data saved successfully to {CSV_FILE}")


def read_history():

    if not os.path.exists(CSV_FILE):

        print("No historical data found.")

        return pd.DataFrame()

    return pd.read_csv(CSV_FILE)