import hs_basic as hs
import pickle
from datetime import datetime as dt
import matplotlib.pyplot as plt

newHighMarge = [0.005] #[x/1000 for x in range(0, 51)] + [x/1000 for x in range(52, 102, 2)]
gainRealizationAt = [0.01, 0.02, 0.04, 0.06]#[x/1000 for x in range(2, 202, 2)]
knockOut = [0.01, 0.05, 0.07]#[x/1000 for x in range(2, 202, 2)]

values, val1, val2, time = [], [], [], []
today = dt.now()
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
    for gain in range(0,len(gainRealizationAt)):
        print(gain, ' of ', len(gainRealizationAt), ' - ', nhM, ' of ', len(newHighMarge))
        for knock in range(0, len(knockOut)):
            time1 = dt.now()
            Inst = hs.Instance(newHighMarge = newHighMarge[nhM], gainRealizationAt = gainRealizationAt[gain], knockOut = knockOut[knock])
            val2.append(Inst.valuate())
            time.append((dt.now()-time1).total_seconds())
        val1.append(val2)
    values.append(val1)

with open("result_data/values_" + str(today.year) + "-" + str(today.month) + "-" + str(today.day) + "_" + str(today.hour) +\
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

time = [t / len(knockOut) for t in time]
with open("result_data/time_" + str(today.year) + "-" + str(today.month) + "-" + str(today.day) + "_" + str(today.hour) +\
    "h" + str(today.minute) +"min" + str(today.second) + "sec.pickle", "wb") as file2:
    pickle.dump(time, file2)

plt.plot(time)
plt.ylabel('Seconds per 100 Instances')
plt.xlabel('Batches - Progress')
plt.show()

print('Your Search: \n\t- Max_Value: ' + str(resultValues[0]) +\
    '\n\t- newHighMarge: ' + str(nhmVal) +\
    '\n\t- gainRealizationAt: ' + str(gainVal) + \
    '\n\t- knockOut: ' + str(knockVal) +\
    '\n\t- return: ' + str(ret) + "%" +\
    '\n\t- totalCost: ' + str(totalCost))