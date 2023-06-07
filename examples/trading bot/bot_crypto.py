import vnpy_crypto
vnpy_crypto.init()

from vnpy.event import EventEngine
from vnpy.trader.engine import MainEngine
from vnpy.trader.ui import MainWindow, create_qapp
from vnpy_chartwizard import ChartWizardApp
from vnpy_ctastrategy import CtaStrategyApp
import vnpy_crypto
from vnpy_binance_pro import (
    BinanceSpotGateway,
    BinanceUsdtGateway,
    BinanceInverseGateway
)
import multiprocessing


def main():
    qapp = create_qapp()

    event_engine = EventEngine()
    main_engine = MainEngine(event_engine)
    # main_engine.add_gateway(BinanceSpotGateway)
     # main_engine.add_gateway(BinanceInverseGateway)
    main_engine.add_gateway(BinanceUsdtGateway)
    main_engine.add_app(ChartWizardApp)
    main_engine.add_app(CtaStrategyApp)
    main_window = MainWindow(main_engine, event_engine)
    main_window.showMaximized()
    qapp.exec()


if __name__ == "__main__":
    # pool = multiprocessing.Pool()
    # pool.apply(main)
    # pool.close()
    # pool.join()
    process = multiprocessing.Process(target=main)
    process.start()
    process.join()
