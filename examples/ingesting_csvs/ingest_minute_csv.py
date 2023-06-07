import vnpy_crypto
vnpy_crypto.init()
from vnpy.trader.constant import Exchange, Interval
from vnpy.trader.engine import MainEngine, EventEngine
from vnpy_datamanager import ManagerEngine
import pandas as pd
import multiprocessing


def ingest_crypto_minute(path, symbol):
    
    df = pd.read_csv(path)
    a = manager.import_data_from_csv(
        file_path=path,
        symbol=symbol,
        exchange=Exchange.BINANCE,
        interval=Interval.MINUTE,
        tz_name= 'Asia/Dhaka',
        datetime_head=df.columns[0],
        open_head=df.columns[1],
        high_head=df.columns[2],
        low_head=df.columns[3],
        close_head=df.columns[4],
        volume_head=df.columns[5],
        datetime_format = '%Y-%m-%d %H:%M:%S', # Need to match from the csv file manually
        turnover_head=None,
        open_interest_head=None)
    print(f'{symbol} imported: {a}')

if __name__ == '__main__':
    manager = ManagerEngine(MainEngine, EventEngine)
    pool = multiprocessing.Pool()
    pool.apply(ingest_crypto_minute, args=('examples/ingesting_csvs/Minute/BTC.csv', 'BTCUSD'))
    pool.close()
    pool.join()
    print('Minute data imported successfully')