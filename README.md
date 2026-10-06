Cryptocurrency Price Tracker
Project Details
Team Number: 5
Name: Sharmila K
Register Number: 512223149035
Department: B.E (CSE) Cyber Security
College: SKP Engineering College
Project Description
Cryptocurrency Price Tracker is a Python-based web automation project that collects cryptocurrency market information from CoinMarketCap using Selenium WebDriver. It reduces manual effort by collecting cryptocurrency details and storing them in CSV format for future reference and analysis.
Problem Statement
Cryptocurrency prices change continuously. Manually checking the current price, 24-hour change and market capitalization of multiple cryptocurrencies is time-consuming and repetitive. This project provides an automated solution to collect and organize this information.
Objectives
Automate cryptocurrency data collection.
Use Selenium to handle dynamic web pages.
Collect the top 10 cryptocurrency records.
Extract name, current price, 24-hour change and market capitalization.
Store data in CSV format.
Maintain historical records.
Support optional filtering.
Support headless browser execution.
Technologies Used
Python
Selenium
pandas
Google Chrome
Chrome WebDriver
CSV
Visual Studio Code
Features
Live Price Scraping
Dynamic Page Handling
Top 10 Coins Data
CSV Export
Headless Browser Option
Historical Logging
Filtering by Price or 24-hour Change
Project Workflow
CoinMarketCap
      ↓
Selenium WebDriver
      ↓
Dynamic Webpage Loading
      ↓
Cryptocurrency Table
      ↓
Data Extraction
      ↓
Python Processing
      ↓
pandas DataFrame
      ↓
CSV File
      ↓
Historical Data / Filtering
Project Structure
cryptocurrency_price_tracker_project/
│
├── venv/
├── data/
│   └── crypto_prices.csv
├── main.py
├── scraper.py
├── tracker.py
├── filter_data.py
├── config.py
├── requirements.txt
└── README.md
File Description
main.py
Main entry point of the application. It starts scraping, displays collected information and saves the data.
scraper.py
Creates the Selenium Chrome WebDriver and extracts cryptocurrency information.
tracker.py
Handles CSV storage and historical data reading.
filter_data.py
Provides filtering based on price or 24-hour change.
config.py
Stores project settings such as website URL, number of coins, CSV location and headless mode.
requirements.txt
Contains the required Python packages.
data/crypto_prices.csv
Stores collected cryptocurrency records.
Installation
1. Open the project
Open the project folder in Visual Studio Code.
2. Create virtual environment
python -m venv venv
3. Activate virtual environment on Windows
venv\Scripts\activate
4. Install packages
pip install selenium pandas
Or:
pip install -r requirements.txt
Running the Project
Make sure the virtual environment is activated and run:
python main.py
The program opens Chrome through Selenium, accesses the cryptocurrency website, collects the available data and saves it to the CSV file.
Expected Output
============================================================
       CRYPTOCURRENCY PRICE TRACKER
============================================================

Starting data collection...

Opening CoinMarketCap...

Top Cryptocurrency Data:

1 | Bitcoin | Price | 24h Change | Market Cap
2 | Ethereum | Price | 24h Change | Market Cap
...

Data saved successfully to data/crypto_prices.csv

Project completed successfully!
The actual values depend on the live market data available when the program runs.
CSV Data
The CSV file contains:
Rank
Name
Price
24h Change
Market Cap
Timestamp
Repeated executions can build a historical dataset.
Headless Mode
In config.py:
HEADLESS_MODE = True
This runs Chrome without displaying the browser window.
For normal browser execution:
HEADLESS_MODE = False
Troubleshooting
Selenium is not installed
If you see:
ModuleNotFoundError: No module named 'selenium'
activate the virtual environment and run:
pip install selenium
No cryptocurrency data collected
Check:
Internet connection.
CoinMarketCap availability.
Selenium installation.
Chrome installation.
Website loading.
Current webpage selectors.
create_driver is not defined
Make sure scraper.py contains the create_driver() function before scrape_crypto_data().
Limitations
Requires internet connectivity for live data.
Dynamic website layouts may change.
Web scraping selectors may need updates.
Cryptocurrency values change rapidly.
Intended mainly for educational and monitoring purposes.
Future Enhancements
Email or mobile price alerts.
Graphical price charts.
Flask or Streamlit dashboard.
Scheduled automatic data collection.
MySQL or PostgreSQL storage.
User-selected cryptocurrencies.
Portfolio tracking.
Advanced trend analysis.
Conclusion
Cryptocurrency Price Tracker demonstrates Selenium-based web automation, dynamic webpage handling, Python data processing and CSV storage. It reduces manual cryptocurrency monitoring and provides a foundation for historical analysis, filtering, alerts and dashboard development.
Author
Sharmila K
B.E (CSE) Cyber Security
SKP Engineering College
Team 5
