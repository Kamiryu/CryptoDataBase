import pandas as pd
from pandas.tseries.offsets import MonthEnd
from sqlalchemy import create_engine
from binance.client import Client

client = Client(api_key,api_secret)

def getdata(symbol,start):
    end = pd.to_datetime(start) + MonthEnd(0) #Setting end of month
    frame = pd.DataFrame(client.get_historical_klines(symbol,
                                                      "1m",
                                                      start,end))
    frame = frame.iloc[:,:6]
    frame.columns = ["Time","Open","High","Low","Close","Volume"]
    frame.set_index("Time",inplace=True)
    frame.index = pd.to_datetime(frame.index,unit="ms")
    frame = frame.astype(float)
    return frame

getdata("BTCUSDT","2022-09-01")
    
    
coins = ('BTCUSDT','ETHUSDT','BNBUSDT','SOLUSDT','ADAUSDT','XRPUSDT','DOTUSDT','LUNAUSDT','DOGEUSDT','AVAXUSDT','SHIBUSDT','MATICUSDT','LTCUSDT','UNIUSDT','ALGOUSDT','TRXUSDT',
         'LINKUSDT','MANAUSDT','ATOMUSDT','VETUSDT')
