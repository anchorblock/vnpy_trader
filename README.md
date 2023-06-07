# By Traders, For Traders

<p align="center">
  <img src ="https://vnpy.oss-cn-shanghai.aliyuncs.com/vnpy-logo.png"/>
</p>

<p align="center">
    <img src ="https://img.shields.io/badge/version-3.7.0-blueviolet.svg"/>
    <img src ="https://img.shields.io/badge/platform-windows|linux|macos-yellow.svg"/>
    <img src ="https://img.shields.io/badge/python-3.10-blue.svg" />
    <img src ="https://img.shields.io/github/workflow/status/vnpy/vnpy/Python%20application/master"/>
    <img src ="https://img.shields.io/github/license/vnpy/vnpy.svg?color=orange"/>
</p>

VeighNa is a Python-based open-source quantitative trading system development framework, officially released in January 2015. It has grown into a full-featured quantitative trading platform with 6 years of continuous contributions from the open-source community. Currently, it has many users from domestic and international financial institutions, including hedge funds, investment banks, futures brokers, university research institutions, proprietary trading companies, etc.

This Repository is a fork of the original VeighNa project. The UI of VnTrader is translated to English, and the code is modified to support global exchanges and crypto markets. This fork contains custom strategies and trading bots used in global exchanges.

## Installation Steps

### Environment preparation

- Supported system versions: Windows 10 or above/Windows Server 2016 or above/Ubuntu 20.04 LTS
- Supported Python version: Python 3.7 64-bit or higher.

1. Install Anaconda: Download and install Anaconda from the official website: <https://www.anaconda.com/products/individual>

2. Create a virtual environment: Open a terminal and create a new virtual environment using the following command:

   ```
   conda create --name myenv python=3.9
   ```

   This will create a new virtual environment named `myenv` with Python 3.9 installed.

3. Activate the virtual environment: Activate the virtual environment using the following command:

   ```
   conda activate myenv
   ```

4. Clone this repository: Clone this repository using the following command:

   ```
   git clone https://github.com/anchorblock/vnpy_trader.git
   ```

5. Change directory: Change to the cloned repository directory using the following command:

   ```
   cd vnpy_trader
   ```

6. Install vnpy

    Windows

        install.bat

    Ubuntu

        . install.sh

    Macos

        bash install_osx.sh

7. After that, run the following command to install the dependent library.

    ```Python
    pip install -r requirements.txt
    ```

## Script Run

Create `run.py` in any directory and write the following sample code.

```Python
from vnpy.event import EventEngine
from vnpy.trader.engine import MainEngine
from vnpy.trader.ui import MainWindow, create_qapp
from vnpy_ctp import CtpGateway
from vnpy_ctastrategy import CtaStrategyApp
from vnpy_ctabacktester import CtaBacktesterApp

def main():
    qapp = create_qapp()

    event_engine = EventEngine()
    main_engine = MainEngine(event_engine)

    main_engine.add_gateway(CtpGateway)
    main_engine.add_app(CtaStrategyApp)
    main_engine.add_app(CtaBacktesterApp)

    main_window = MainWindow(main_engine, event_engine)
    main_window.showMaximized()

    qapp.exec()

if __name__ == "__main__":
    main()
```

## Demo Examples

All of the examples are located in the examples folder, including those from the original VeighNa project.

Here are a few examples:

| Example                                                                                                                                                   | Description                                       |
| --------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- |
| [Ingesting Custom CSVs](https://github.com/anchorblock/vnpy_trader/blob/master/examples/ingesting_csvs/ingest_minute_csv.py)                              | Ingesting custom CSVs into the system             |
| [Creating Custom Strategy](https://github.com/anchorblock/vnpy_trader/blob/master/examples/custom%20strategies/my_strategy.py)                            | Creating custom strategies                        |
| [Importing Custom Strategies to Trading Module](https://github.com/anchorblock/vnpy_trader/blob/master/examples/custom%20strategies/import_strategies.sh) | Importing custom strategies to the trading module |
| [Creating Custom Trading Bot](https://github.com/anchorblock/vnpy_trader/blob/master/examples/trading%20bot/bot_crypto.py)                                | Creating custom trading bots                      |
| [Backtesting Strategies](https://github.com/anchorblock/vnpy_trader/blob/master/examples/backtesting_on_custom_csvs/backtest_daily.ipynb)                 | Backtesting strategies                            |
