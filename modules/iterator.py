import modules.shortlist as sl
import pandas_datareader.data as wb
import pandas as pd


def roller(tickers):
    newDataFrame = pd.Series([])
    data = pd.DataFrame()
    i = 1
    for t in tickers:
        df = wb.DataReader(t,data_source= 'yahoo',start = '2020-1-1')
        if(sl.checkPositive(df)):
            newDataFrame[i] = t
            i+=1

    data.insert(0, "Shortlisted Stocks", newDataFrame)    
    
    return data 



    
