from pandas import DataFrame
from tinkoff.invest import Client, InstrumentStatus, SharesResponse, InstrumentIdType
from tinkoff.invest.services import InstrumentsService, MarketDataService



import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


TOKEN=""
def run():
    with Client(TOKEN) as cl:
        instruments: InstrumentsService = cl.instruments
        market_data: MarketDataService = cl.market_data


        r=instruments.shares(instrument_status=InstrumentStatus.INSTRUMENT_STATUS_ALL).instruments
        ruShare=[]
        for i in range(len(r)):
            if r[i].currency == 'rub' and r[i].currency != 'usd'  and r[i].buy_available_flag==True and r[i].api_trade_available_flag==True:
                # delattr(r[i].currency, 'first_1day_candle_date')


                d = dict(figi=r[i].figi, ticker=r[i].ticker, name=r[i].name, lot=r[i].lot, short_enabled_flag=r[i].short_enabled_flag, units=r[i].min_price_increment.units, nano=r[i].min_price_increment.nano)
                # my_dict = r[i].dict(keys=['ticker', 'figi'])
                # print(d)
                # ruShare.append(r[i])
                print(r[i])
                ruShare.append(d)
        print('1')

        # for i in range(len(ruShare)):
        #     for j in range(len(ruShare)):
        #         # if ruShare[i].ticker == ruShare[j].ticker and ruShare[i].figi !=ruShare[j].figi:
        #             print(ruShare[i])

        df = pd.DataFrame(ruShare)

        df.to_excel(r'C:\Users\AATsv\PycharmProjects\tikersSearch\dataExl.xlsx', index=False)

if __name__ == '__main__':
    run()