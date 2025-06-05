import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import random
from stocks import getStocks
import yfinance as yf
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

# Setup a retrying session
session = requests.Session()
retries = Retry(
    total=5,
    backoff_factor=10,
    status_forcelist=[500, 502, 503, 504],
    raise_on_status=False,
)
session.mount("https://", HTTPAdapter(max_retries=retries))
session.mount("http://", HTTPAdapter(max_retries=retries))

headers = {
    "User-Agent": "Mozilla/5.0"
}

def get_valid_soup(symbol, consolidated=True):
    url = f"https://www.screener.in/company/{symbol}/{'consolidated/' if consolidated else ''}"
    try:
        response = session.get(url, headers=headers, timeout=20)
        if response.status_code != 200:
            return None, None

        soup = BeautifulSoup(response.content, "html.parser")
        table_section = soup.find("section", id="balance-sheet")
        if not table_section or not table_section.find("table"):
            return None, None

        return soup, consolidated
    except requests.exceptions.RequestException as e:
        print(f"[⚠️] Request failed for {symbol}: {e}")
        return None, None

def fetch_balance_sheet(stock_symbol):
    soup, used_consolidated = get_valid_soup(stock_symbol, consolidated=True)
    if soup is None:
        soup, used_consolidated = get_valid_soup(stock_symbol, consolidated=False)
        if soup is None:
            print(f"[❌] No balance sheet found for {stock_symbol}")
            return None

    print(f"[✅] Using {'consolidated' if used_consolidated else 'standalone'} for {stock_symbol}")

    table = soup.find("section", id="balance-sheet").find("table")
    rows = table.find_all("tr")
    ths = table.find_all("th")[1:]

    data = {}
    periods = []

    for th in ths:
        text = th.text.strip()
        try:
            date = pd.to_datetime(text, format="%b %Y") + pd.offsets.MonthEnd(0)
            periods.append(date.date())
        except Exception as e:
            print(f"Couldn't parse period: {text} - {e}")

    for row in rows[1:]:
        cols = row.find_all("td")
        if len(cols) < 2:
            continue
        key = cols[0].text.strip()
        values = [td.text.strip().replace(",", "") for td in cols[1:]]
        data[key] = values

    df = pd.DataFrame.from_dict(data, orient='index').transpose()
    df.index = periods
    df["id"] = stock_symbol
    return df

# Load stock list
stocks = list(getStocks())
dList = []
cList = []

for i in stocks:
    df = fetch_balance_sheet(i)
    if df is not None:
        try:
            df.to_csv("stocks.csv", mode="a", index=True, header=False)
            print(f"✅ Stock: {i} appended into stocks.csv")
            dList.append(i)
        except Exception as e:
            print(f"❌ Failed to write for {i} — {e}")
            cList.append(i)
    else:
        cList.append(i)

    time.sleep(random.uniform(15, 20))  # Safe scraping interval

# Summary and file outputs
print(f"\n✅ Tickers Successfully Appended: {len(dList)}")
print(f"❌ Tickers Unable to append: {len(cList)}")

with open('dList.txt', 'a') as file1:
    for i in dList:
        file1.write(i + "\n")

with open('cList.txt', 'a') as file2:
    for j in cList:
        file2.write(j + "\n")
