def checkPositive(dataset):
    dataset['sma44'] = dataset.Close.rolling(44).mean()
    reduced = dataset.tail(10)['sma44']
    flag = True
    for i in range(9):
        if(reduced[i]>reduced[i+1]):
            flag = False
    
    return flag

