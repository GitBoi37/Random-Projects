# import required modules
import pandas as pd
import numpy as np
import time
import random
from pprint import pprint
import multiprocessing as mp

def simulateMartingale(data):
    bet = 0.00001
    startbet = bet
    start = 2
    mult = 2
    check = start
    balance = 5.5
    index = 0
    #highestBet = 0
    for i in data["rate"]:
        if(i >= check):
            balance += check * bet
            bet = startbet
        else:
            balance -= bet
            bet *= mult
        #if(bet > highestBet):
            #highestBet = bets
        index = index + 1
        if(balance <= 0):
            return index
    return 0

def simulateUnlimitedMartingale(data):
    bet = .00001
    startbet = bet
    start = 2
    mult = 2
    check = start
    balance = 5.5
    index = 0
    startBalance = balance
    #highestBet = 0
    i = 0
    indexcap = 10**8
    while balance > 0 and index < indexcap:
        for i in data["rate"]:
            if(i >= check):
                balance += check * bet
                bet = startbet
            else:
                balance -= bet
                bet *= mult
            #if(bet > highestBet):
                #highestBet = bets
            index = index + 1
            if(balance <= 0):
                return index
            #elif(balance > startBalance * 4):
                #balance = startBalance
        #if(index > 10**8):
            #return 10**8
        data.sample(frac=1).reset_index(drop=True)
    return index

def simulateBetHigh(data):
    bet = .00001
    check = 1.5
    balance = 5.5
    index = 0
    for i in data["rate"]:
        if(index  % 100 == 0):
            i = 0
        if(i >= check):
            balance += check * bet
        else:
            balance -= bet
        index = index + 1
        if(balance <= 0):
            return 0
    return balance

def simulateProfitMartingale(data):
    bet = 0.00001
    startbet = bet
    start = 2
    mult = 2
    check = start
    balance = 5.5
    startBalance = 5.5
    index = 0
    #highestBet = 0
    for i in data["rate"]:
        if(i >= check):
            balance += check * bet
            bet = startbet
        else:
            balance -= bet
            bet *= mult
        #if(bet > highestBet):
            #highestBet = bets
        index = index + 1
        if(balance <= 0):
            return index
        if(balance > startBalance * 2):
            balance = startBalance
    return 0


def simulatePayoutMartingale(data):
    bet = 0.00001
    startbet = bet
    start = 1.98
    add = 1
    check = start
    balance = 5.5
    index = 0
    #highestBet = 0
    for i in data["rate"]:
        if(i >= check):
            balance += check * bet
            bet = startbet
            check = start
        else:
            balance -= bet
            check += add
        #if(bet > highestBet):
            #highestBet = bet
        index = index + 1
        if(balance <= 0):
            return index
    return 0

if __name__ == '__main__':
    averageFail = 0
    failSum = 0
    totalBets = 0
    numbertoread = 10**6
    samples = 8
    tests = 8
    p_file = r'C:\Users\Lance Eades\Documents\\nanorate.csv'
    s_time_dask = time.time()
    pandas_df = pd.read_csv(p_file,nrows=numbertoread)
    e_time_dask = time.time()
    print(f"Length of data: {pandas_df.size}")
    print("Read with pandas: ", (e_time_dask-s_time_dask), "seconds")
    betsPerTest = 0
    failPerTest = 0
    s_time_loop = time.time()
    pool = mp.Pool(mp.cpu_count())
    print("Tests done: ",end="")
    for i in range(tests):
        #totalBets += numbertoread * samples
        # do some parallelization B)

        s_time_dask = time.time() 
        results = pool.map(simulateMartingale, [pandas_df.sample(frac=1).reset_index(drop=True) for i in range(samples)])
        e_time_dask = time.time()
        print(f"{i}", end=" ")
        pprint(results)
        failPerTest = 0
        betsPerTest = 0
        for j in range(len(results)):
            if(results[j] > 0):
                failSum += 1
                failPerTest += 1
                totalBets += results[j]
                betsPerTest += results[j]
            else:
                totalBets += numbertoread
                betsPerTest += numbertoread

        print(f"Looped through {betsPerTest} datapoints: ", (e_time_dask-s_time_dask), "seconds")  
        print(f"Failed {failPerTest} times")
    print()
    pool.close()
    pool.join()
    e_time_loop = time.time()
    averageFail = failSum / totalBets
    averageFailureIndex = totalBets / (tests*samples)
    tAnalyze = e_time_loop-s_time_loop
    #print(f"Total profit {profit}")
    print(f"Total time to analyze: {tAnalyze}")
    print(f"Average time to analyze: {tAnalyze/tests}")
    print(f"Total Bets: {totalBets}")
    print(f"Total failures: {failSum}")
    print(f"Average bust rate: {averageFail}")
    print(f"Average index of failure {averageFailureIndex}")

