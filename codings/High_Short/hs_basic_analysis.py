import hs_basic as hs
import pickle
from datetime import datetime

newHighMarge = [x/1000 for x in range(0, 102, 2)]
gainRealizationAt = [x/1000 for x in range(2, 202, 2)]
knockOut = [x/1000 for x in range(2, 202, 2)]

values, val1, val2 = [], [], []
today = datetime.now()
uniqueResults = True # if True, output will be unique, False: Output will show combinations

def valuate(self, searchkey='totalGain'):
    
    max, nhmVal, gainVal, knockVal = 0, [], [], []
    print("Started with Analysis")
    for val1 in range(0, len(newHighMarge)):
        for val2 in range(0, len(gainRealizationAt)):
            for val3 in range(0, len(knockOut)):
                if values[val1][val2][val3][searchkey] == max:
                    nhmVal.append(val1)
                    gainVal.append(val2)
                    knockVal.append(val3)
                if values[val1][val2][val3][searchkey] > max:
                    max = values[val1][val2][val3][searchkey]
                    nhmVal = [val1]
                    gainVal = [val2]
                    knockVal = [val3]
    print("Finished with Analysis, return [VALUES]")
    return (max, nhmVal, gainVal, knockVal)

for nhM in range(0, len(newHighMarge)):
    print(nhM, len(newHighMarge))
    for gain in range(0, len(gainRealizationAt)):
        for knock in range(0, len(knockOut)):
            Inst = hs.Instance(newHighMarge = newHighMarge[nhM], gainRealizationAt = gainRealizationAt[gain], knockOut = knockOut[knock])
            val2.append(Inst.valuate())
        val1.append(val2)
    values.append(val1)

with open("value_data/values_" + str(today.year) + "-" + str(today.month) + "-" + str(today.day) + "_" + str(today.hour) +\
    "h" + str(today.minute) +"min" + str(today.second) + "sec.pickle", "wb") as file:
    pickle.dump(values, file)

resultValues = valuate('totalGain')
nhmVal = [newHighMarge[n] for n in resultValues[1]]
gainVal = [gainRealizationAt[n] for n in resultValues[2]]
knockVal = [knockOut[n] for n in resultValues[3]]
ret = [round(values[resultValues[1][index]][resultValues[2][index]][resultValues[3][index]]['ret'], 2) for index in range(0, len(nhmVal))]
totalCost = [round(values[resultValues[1][index]][resultValues[2][index]][resultValues[3][index]]['totalCost'], 2) for index in range(0, len(nhmVal))]

if uniqueResults:
    nhmVal = set(nhmVal)
    gainVal = set(gainVal)
    knockVal = set(knockVal)
    ret = set(ret)
    totalCost = set(totalCost)


print('Your Search: \n\t- Max_Value: ' + str(resultValues[0]) +\
    '\n\t- newHighMarge: ' + str(nhmVal) +\
    '\n\t- gainRealizationAt: ' + str(gainVal) + \
    '\n\t- knockOut: ' + str(knockVal) +\
    '\n\t- return: ' + str(ret) + "%" +\
    '\n\t- totalCost: ' + str(totalCost))