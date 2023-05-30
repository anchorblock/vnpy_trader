# By Traders, For Traders.

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

VeighNa is a Python-based open source quantitative trading system development framework, officially released in January 2015, has grown step by step into a full-featured quantitative trading platform with 6 years of continuous contributions from the open source community, and currently has many users from domestic and international financial institutions, including: hedge funds, investment banks, futures brokers, university research institutions, proprietary trading companies, etc.

This Repository is a fork of the original VeighNa project. The UI of VnTrader is translated to English and the code is modified to support global exchanges. This fork contains custom strategies and trading bot which are used in global exchanges.


## Installation steps

Close this repo, unzip it and run the following command to install it.

**Windows**

```
install.bat
```

**Ubuntu**

```
. install.sh
```

**Macos**

```
bash install_osx.sh
```

## Script Run

In addition to the graphical start-up method based on VeighNa Station, you can also create run.py in any directory and write the following sample code.

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

if __name__ == "__main__"。
    main()
```

Open CMD in that directory (hold Shift->click right mouse button->open command window/PowerShell here) and then run the following command to start VeighNa Trader.

    python run.py
    



