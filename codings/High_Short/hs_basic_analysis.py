import hs_basic as hs

newHighMarge = [x/1000 for x in range(0, 100, 2)]
gainRealizationAt = [x/1000 for x in range(5, 305, 5)]
knockOut = [x/1000 for x in range(5, 305, 5)]

values = []

def valuate(self, str='totalGain'):
    if not str == 'totalGain': # we could search for others like 'ret' or 'totalKnockOuts' as well
        return "Search not implemented"
    
    max = 0

    

for nhM in newHighMarge:
    for gain in gainRealizationAt:
        for knock in knockOut:
            Inst = hs.Instance(newHighMarge = nhM, gainRealizationAt = gain, knockOut = knock)
            buff = Inst.valuate()
            values[nhM, gain, knock] = (buff['totalGain'], buff['totalKnockOuts'], buff['ret'])

print(valuate())
