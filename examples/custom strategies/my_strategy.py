from vnpy_ctastrategy import (
    CtaTemplate,
    StopOrder,
    TickData,
    BarData,
    TradeData,
    OrderData,
    BarGenerator,
    ArrayManager,
)

from vnpy.trader.constant import Exchange, Interval


class MyStrategy(CtaTemplate):
    author = 'ornob'
    fast_window = 3
    slow_window = 5
    parameters = ["fast_window", "slow_window"]
    variables = ['inited', 'trading', 'pos']

    def __init__(self, cta_engine, strategy_name, vt_symbol, setting):
        super().__init__(cta_engine, strategy_name, vt_symbol, setting)
        self.bg = BarGenerator(self.on_bar, interval=Interval.TICK)
        self.am = ArrayManager()

    def on_init(self):
        self.write_log("Strategy initialization")
        print("Strategy initialization")
        self.load_bar(max(10, self.slow_window, self.fast_window))

    def on_start(self):
        self.write_log("Strategy start")
        print('Strategy start')
        self.put_event()

    def on_stop(self):
        self.write_log("Strategy stop")
        print('Strategy stop')
        self.put_event()

    def on_tick(self, tick: TickData):
        self.bg.update_tick(tick)

    def on_bar(self, bar: BarData):
        self.cancel_all()
        self.am.update_bar(bar)

        if not self.am.inited:
            return

        fast_ma = self.am.sma(self.fast_window, array=True)
        slow_ma = self.am.sma(self.slow_window, array=True)
        if self.pos == 0:
            if fast_ma[-1] > slow_ma[-1]:
                self.buy(bar.close_price, 1)
                print(f'Placing buy order at {bar.close_price}')
            elif fast_ma[-1] < slow_ma[-1]:
                self.short(bar.close_price, 1)
                print(f'Placing short order at {bar.close_price}')

        elif self.pos > 0:
            if fast_ma[-1] < slow_ma[-1]:
                self.sell(bar.close_price, 1)
                print(f'Placing sell order at {bar.close_price}')

        elif self.pos < 0:
            if fast_ma[-1] > slow_ma[-1]:
                self.cover(bar.close_price, 1)
                print(f'Placing cover order at {bar.close_price}')

        self.put_event()

    def on_order(self, order: OrderData):
        pass

    def on_trade(self, trade: TradeData):
        self.put_event()

    def on_stop_order(self, stop_order: StopOrder):
        pass
