import numpy as np
import pandas as pd

class Position:
        
        def __init__(self, buyPrice, index, knockOut, gainRealizationAt):
            self.index = index
            self.buyPrice = buyPrice
            self.knockOutHurdle = round(buyPrice * (1 + knockOut), 2)
            self.gainrealization = round(buyPrice * (1 - gainRealizationAt), 2)
            self.cost = round(buyPrice * knockOut, 2)
            self.outknocked = False
            self.closed = False
            self.result = 0
            self.gain = 0
            
        def sell(self, sellPrice, knockedOut):
            self.sellPrice = sellPrice
            self.closed = True
            self.outknocked = knockedOut
            self.result = self.buyPrice - self.sellPrice
            if self.outknocked:
                self.result = 0
            self.gain = self.result - self.cost

class Instance:

    def __init__(self, csv_file="../../data/DAX_DATA/Price_History_daily_50y.csv", newHighMarge = 0.005, gainRealizationAt = 0.06, knockOut = 0.01):
        self.data = pd.read_csv(csv_file) # path to file
        self.newHighMarge = newHighMarge # in percent
        self.gainRealizationAt = gainRealizationAt # in percent
        self.knockOut = knockOut # in percent
        self.positions = []

    def check(self, currentValue):
        for pos in self.positions:
            if pos.closed:
                continue
            if currentValue < pos.gainrealization:
                pos.sell(currentValue, False)
            elif currentValue > pos.knockOutHurdle:
                pos.sell(currentValue, True)

    def valuate(self):

        allTimeHigh, currVal = 0, 0
        totalPositions, totalCost, totalResult, totalGain = 0, 0, 0, 0

        for val in self.data.itertuples():
            if allTimeHigh * (1 + self.newHighMarge) < val[1]:
                self.positions.append(Position(val[1], val[0], self.knockOut, self.gainRealizationAt))
                allTimeHigh = val[1]
            self.check(val[1])

            notClosedPositions = [pos for pos in self.positions if not pos.closed]

        totalKnockOuts = 0
        for pos in self.positions:
            totalCost += pos.cost
            totalResult += pos.result
            totalGain += pos.gain
            if pos.outknocked:
                totalKnockOuts += 1
            
        totalPositions = len(self.positions)
        totalCost = round(totalCost, 2)
        totalGain = round(totalGain, 2)
        totalResult = round(totalResult, 2)
        totalKnockOuts = round(totalKnockOuts, 2) 

        ret = (totalGain / totalCost) * 100 # in percent
        yoyret = 0
        if ret > 0:
            yoyret = ((1+(ret / 100)) ** 0.02) * 100 - 100 # 50 years of data

        return {'totalPositions': totalPositions, 'totalCost': totalCost ,'totalGain': totalGain, 
        'totalResult': totalResult, 'totalKnockOuts': totalKnockOuts ,'ret': ret, 'yoyret': yoyret}


if __name__ == '__main__':
    I1 = Instance()
    val = I1.valuate()
    print(val)