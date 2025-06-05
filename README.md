
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
├── main.py                # Main script to run the scraping process
├── scrapper.py            # Contains core web scraping logic
├── stocks.py              # Helper functions for stock symbol handling
├── balance_sheet.csv      # Output: balance sheet data
├── Equity.csv             # Output: equity data
├── cList.txt              # Input: list of company symbols
├── dList.txt              # Input: list of dates or data-related config
├── LICENSE                # Open-source license (Apache 2.0)
├── README.md              # You’re reading it!
└── __pycache__/           # Python bytecode cache
```

---

## 🛠️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/myselfRaifMondal/Fundamental-Financial-Data-Scrapper.git
cd Fundamental-Financial-Data-Scrapper
```

### 2. Set Up Inputs

- `cList.txt`: Add the stock tickers/symbols (one per line) of companies you want to scrape.
- `dList.txt`: Used optionally if scraping for specific dates/sectors (depends on implementation).

### 3. Run the Scraper

```bash
python main.py
```

### 4. Output

Scraped data will be saved in:
- `balance_sheet.csv`
- `Equity.csv`

---

## 📦 Dependencies

This project requires Python 3.7 or above.

Install dependencies using:

```bash
pip install -r requirements.txt
```

> Note: If `requirements.txt` is missing, you can manually install likely packages:
```bash
pip install requests pandas
```

---

## 🧰 Example Use Case

1. Add companies like `TCS`, `INFY`, `RELIANCE` in `cList.txt`.
2. Run `main.py`.
3. Open `balance_sheet.csv` and `Equity.csv` for clean, tabular financial data.

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
