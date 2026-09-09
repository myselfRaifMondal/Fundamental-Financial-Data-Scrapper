
# 📊 Fundamental-Financial-Data-Scrapper

Welcome to the **Fundamental-Financial-Data-Scrapper** repository! This project is designed to automate the extraction of fundamental financial data (such as balance sheets and equity reports) for listed companies. It’s a great tool for investors, traders, financial analysts, or developers looking to analyze company fundamentals at scale.

---

## 🧠 Motivation

Tired of manually downloading financial data from websites? This scrapper automates the boring stuff and lets you focus on building models, visualizations, or backtests with clean data.

---

## 🚀 Features

- 🔍 Scrapes fundamental financial data such as:
  - Balance Sheets
  - Equity Information
- 🏷️ Supports batch processing of multiple companies via `cList.txt`
- 📁 Outputs structured `.csv` files for downstream analysis
- 🧱 Modular Python codebase (easy to extend and integrate)
- ⚡ Fast, lightweight, and free to use

---

## 📂 Project Structure

```
Fundamental-Financial-Data-Scrapper/
│
├── scrapper.py            # Run this: scrapes balance sheets from screener.in
├── main.py                # Local analysis script over balance_sheet.csv
├── stocks.py              # Reads the ticker universe out of Equity.csv
├── balance_sheet.csv      # Balance sheet data
├── Equity.csv             # Input: ticker universe ("Security Id" column)
├── cList.txt              # Output: tickers that failed to scrape
├── dList.txt              # Output: tickers scraped successfully
├── requirements.txt       # Python dependencies
├── LICENSE                # Open-source license (Apache 2.0)
├── README.md              # You’re reading it!
└── __pycache__/           # Python bytecode cache
```

---

## 🛠️ Setup / Usage

### 1. Clone the Repository

```bash
git clone https://github.com/myselfRaifMondal/Fundamental-Financial-Data-Scrapper.git
cd Fundamental-Financial-Data-Scrapper
```

### 2. Install Dependencies

Python 3.9 or above is recommended. Using a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

`requirements.txt` pins the third-party packages actually imported by the code:
`pandas`, `numpy`, `requests`, `urllib3`, `beautifulsoup4` and `yfinance`.

### 3. Run the Scraper

The scraping job lives in `scrapper.py`, and running that file is what performs the scrape:

```bash
python scrapper.py
```

It reads the ticker universe from `Equity.csv` (via `getStocks()` in `stocks.py`, which
returns the `Security Id` column), fetches each company's balance sheet from
screener.in — trying the consolidated statement first and falling back to standalone —
and sleeps 15–20 seconds between requests, so a full run takes a long time.

Output of a run:

- `stocks.csv` — scraped balance-sheet rows, **appended** one ticker at a time
- `dList.txt` — tickers that were scraped and written successfully
- `cList.txt` — tickers that failed (no balance sheet found, or a write error)

### 4. Inspect the Data

`main.py` is a small local analysis script, **not** the scraper. It loads
`balance_sheet.csv` with an explicit column list and parses the index into
timestamps:

```bash
python main.py
```

Run it once you have a CSV of scraped data to look at.

---

## 🧰 Example Use Case

1. Put the tickers you care about in the `Security Id` column of `Equity.csv`.
2. Run `python scrapper.py`.
3. Open `stocks.csv` for clean, tabular financial data.

Perfect for:
- Investment Research 📈
- Quant Strategy Backtests 🤖
- Financial Dashboards 📊

---

## 📌 Future Enhancements

- Add more financial statements (P&L, Cash Flow)
- Integration with a live financial API
- Automate periodic updates
- Web dashboard using Streamlit or Flask

---

## 📄 License

This project is licensed under the **Apache 2.0 License**.  
See the [LICENSE](LICENSE) file for more details.

---

## 🤝 Contributing

Pull requests are welcome!  
For major changes, please open an issue first to discuss what you’d like to change.

---

## 📬 Contact

**Author:** Raif Mondal  
Feel free to connect with me via:
- GitHub: [@myselfRaifMondal](https://github.com/myselfRaifMondal)
- LinkedIn: [Raif Mondal](https://www.linkedin.com/in/raifmondal/)

---

> Happy Scraping! 🚀 Let the data do the talking.
