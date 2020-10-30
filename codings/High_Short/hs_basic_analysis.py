import hs_basic as hs

newHighMarge = [x/1000 for x in range(0, 100, 2)]
gainRealizationAt = [x/1000 for x in range(2, 302, 2)]
knockOut = [x/1000 for x in range(2, 302, 2)]

values = []

def valuate(self, str='totalGain'):
    index = 2
    if str == 'totalPositions':
        index = 0
    elif str == 'totalCost':
        index = 1
    elif str == 'totalResult':
        index = 3
    elif str == 'totalKnockOuts':
        index = 4
    elif str == 'ret':
        index = 5
    elif str == 'yoyret':
        index = 6
    
    max, nhmVal, gainVal, knockVal = 0, [], [], []

    for val1 in range(0, len(values)):
        for val2 in range(0, len(val1)):
            for val3 in range(0, len(val2)):
                if values[val1, val2, val3, index] == max:
                    nhmVal.add(val1)
                    gainVal.add(val2)
                    knockVal.add(val3)
                elif values[val1, val2, val3, index] > max:
                    max = values[val1, val2, val3, 0]
                    nhmVal = [val1]
                    gainVal = [val2]
                    knockVal = [val3]
    
    return (max, nhmVal, gainVal, knockVal)

for nhM in newHighMarge:
    for gain in gainRealizationAt:
        for knock in knockOut:
            Inst = hs.Instance(newHighMarge = nhM, gainRealizationAt = gain, knockOut = knock)
            buff = Inst.valuate()
            values[nhM, gain, knock] = (buff['totalPositions'], buff['totalCost'], buff['totalGain'], buff['totalResult'], buff['totalKnockOuts'], buff['ret'], buff['yoyret'])

resultValues = valuate('totalGain')

print('Your Search: \n\t- Max_Value: ', resultValues[0], '\n\t- newHighMarge: ', resultValues[1], '\n\t- gainRealizationAt: ', resultValues[2], '\n\t- knockOut: ', resultValues[3])
