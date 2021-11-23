# import required modules
import pandas as pd
import numpy as np
import time
from pprint import pprint
import multiprocessing as mp
numbertoread = 10**4
samples = 10000
# time taken to read data
s_time_dask = time.time()
pandas_df = pd.read_csv('nanorate.csv',nrows=numbertoread)
e_time_dask = time.time()
  
print("Read with pandas: ", (e_time_dask-s_time_dask), "seconds")

def bust(data):
    bet = 0.00001
    startbet = bet
    start = 2
    mult = 2
    check = start
    balance = 5.5
    index = 0
    highestBet = 0
    for i in data:
        if(i >= check):
            balance += check * bet
            bet = startbet
            #print(f"rate: {i}, balance: {balance}, bet: {bet}")
        else:
            balance -= bet
            bet *= mult
            #print(f"rate: {i}, balance: {balance}, bet: {bet}")
        if(bet > highestBet):
            #print(f"New highest bet: {index} {bet}")
            highestBet = bet
        index = index + 1
        if(balance <= 0):
            #print(f"busted at {index - 1}")
            return True
    return False
# data
data = pandas_df["rate"][0:numbertoread]
outcomes = []
s_time_dask = time.time()
data = pandas_df.sample(frac=1).reset_index(drop=True)["rate"][0:numbertoread]
for x in range(samples):
    bet = 0.00001
    startbet = bet
    start = 2
    mult = 2
    check = start
    balance = 5.5
    index = 0
    highestBet = 0
    for i in data:
        if(i >= check):
            balance += check * bet
            bet = startbet
            #print(f"rate: {i}, balance: {balance}, bet: {bet}")
        else:
            balance -= bet
            bet *= mult
            #print(f"rate: {i}, balance: {balance}, bet: {bet}")
        if(bet > highestBet):
            #print(f"New highest bet: {index} {bet}")
            highestBet = bet
        index = index + 1
        if(balance <= 0):
            #print(f"busted at {index - 1}")
            outcomes.append("busted")
            outcomes.append(index - 1)
            break
    #outcomes.append(f"balance: {round(balance,3)}")
e_time_dask = time.time()
print(f"Looped through {numbertoread} * {samples} datapoints: ", (e_time_dask-s_time_dask), "seconds")  
print("end")