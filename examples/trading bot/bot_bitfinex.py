import vnpy_crypto
vnpy_crypto.init()
from vnpy_ctastrategy.base import EVENT_CTA_LOG
from vnpy.trader.engine import MainEngine, EventEngine
from vnpy.trader.ui import MainWindow, create_qapp
from vnpy.trader.constant import Exchange, Interval
from vnpy_ctastrategy import CtaStrategyApp
from vnpy_ib.ib_gateway import IbGateway
from vnpy.trader.utility import load_json
from vnpy_scripttrader import init_cli_trading
from vnpy.trader.object import SubscribeRequest
from vnpy.chart import ChartWidget, VolumeItem, CandleItem
from vnpy_spreadtrading import SpreadTradingApp
from vnpy_algotrading import AlgoTradingApp
from vnpy_chartwizard import ChartWizardApp
from vnpy.trader.setting import SETTINGS
from vnpy_ctastrategy.strategies.my_strategy import MyStrategy
from vnpy_ctastrategy.strategies.atr_rsi_strategy import AtrRsiStrategy
from vnpy_ctastrategy.strategies.double_ma_strategy import DoubleMaStrategy
from vnpy_bitfinex import BitfinexGateway

from logging import INFO
from time import sleep
import multiprocessing
import json
import os

SETTINGS["log.active"] = True
SETTINGS["log.level"] = INFO
SETTINGS["log.console"] = True


def strat_config(strat_name: str, setting: dict):
    curr_dir = os.path.dirname(os.path.abspath(__file__))
    json_dir = '/home/shell007/.vntrader/cta_strategy_setting.json'
    with open(json_dir) as f:
        data = json.load(f)
    with open(json_dir, 'w') as f:
        data[strat_name] = setting
        json.dump(data, f, indent=4)
        print('Config Loaded')


def main():
    SETTINGS["log.file"] = True
    qpp = create_qapp()
    event_engine = EventEngine()
    main_engine = MainEngine(event_engine)
    api_key = '5hqbujaybQNFGU6cMlFVxmkplCAm0ugE7t4JER8YWrM'
    api_secret = 'z048543eDUcODQKN8QcrgTQ7mj3vHbMsjqQREqo61jO'
    setting = {
        "key": api_key,
        "secret": api_secret,
        "代理地址": "",
        "代理端口": 0,
        "margin": "False"
    }
    main_engine.add_gateway(BitfinexGateway)
    cta_engine = main_engine.add_app(CtaStrategyApp)
    main_engine.write_log("The main engine was created successfully")
    log_engine = main_engine.get_engine("log")
    event_engine.register(EVENT_CTA_LOG, log_engine.process_log_event)
    main_engine.write_log("Register log event listener")
    main_engine.connect(gateway_name="Bitfinex", setting=setting)
    main_engine.write_log("Connect to the CTP interface")
    sleep(10)

    main_engine.add_app(ChartWizardApp)
    # Strategy Stuffs
    cta_engine.init_engine()
    cta_engine.init_all_strategies()
    main_engine.write_log("CTA strategy activated")
    main_window = MainWindow(main_engine, event_engine)
    main_window.showMaximized()
    qpp.exec()


if __name__ == "__main__":
    process = multiprocessing.Process(target=main)
    process.start()
    print('Starting')
    process.close()
    sys.exit(0)
