# -*- coding: utf-8 -*-
"""
Created on Mon Jan 17 22:58:59 2022

@author: yusup
"""

#AMALIYOT
#davlatlar = ['Rossiya', 'Yaponiya', 'Germaniya', 'Belgiya', 'Fransiya', 'Ispaniya', 'Shimoliy Koreya']
#print(len(davlatlar))
#print(sorted(davlatlar))
#print(sorted(davlatlar, reverse=True))
#print(davlatlar)

#davlatlar.reverse()
#print(davlatlar)

#davlatlar.sort()
#print(davlatlar)

#davlatlar.sort(reverse=True)
#print(davlatlar)

#print(list(range(120, 1200, 2)))
#print(sum(list(range(120, 1200, 2))))

#print(max(list(range(120, 1200, 2))) - min(list(range(120, 1200, 2))))

#print(len(list(range(120, 1200, 2))))

#sonlar = list(range(120, 1200, 2))
#print(sonlar[:20])
#print(sonlar[261:281])
#print(sonlar[521:])

taomlar = ['somsa', 'manti', 'osh', 'chuchvara', 'kabob']
nonushta = taomlar[:]
nonushta.remove('somsa')
nonushta.remove('manti')
nonushta.remove('osh')
nonushta.remove('chuchvara')
nonushta.remove('kabob')
nonushta.append('quymoq')
nonushta.append('kasha')
print(nonushta)
print(taomlar)
nonushta = tuple(nonushta)
print(nonushta)
nonushta[0]="quymoq va non"