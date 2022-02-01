# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 21:50:37 2022

@author: yusup
"""

#22-dars: *args va **kwargs

#def summa(*sonlar):
#    """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
#    yigindi = 0
#    for son in sonlar:
#        yigindi += son
#    return yigindi

#print(summa(1,2))
#print(summa(1,2,3,4,5))
#print(summa(4,5,6,7))


#def summa(x,y,*sonlar):
#    """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
#    return x+y+sum(sonlar)
#print(summa(1,2))
#print(summa(1,2,3,4,5))
#print(summa(4,5,6,7))
#print(summa(2,4))


#def avto_info(kompaniya, model, **malumotlar):
#    """Avto haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
#    malumotlar['kompaniya'] = kompaniya
#    malumotlar['model'] = model
#    return malumotlar
#avto1 = avto_info("GM", "malibu", rang='qora', yil=2018)
#avto2 = avto_info("Kia", "K5", rang='qizil', narx=35000, yil=2020, korobka='avtomat')


#AMALIYOT

#def kopaytmani_hisobla(*sonlar):
#    """Kiritilgan sonlarning ko'paytmasini hisoblaydigan funksiya"""
#    kopaytma = 1
#    for son in sonlar:
#        kopaytma = kopaytma*son
#    return kopaytma
#print(kopaytmani_hisobla(2,3,4))
#print(kopaytmani_hisobla(0,1,2,3,4,5,6,7,8))


def talaba_info(ism, familiya, **malumotlar):
    """Talabalar haqidagi ma'lumotlarni lug'at ko'rinishida chiqaruvchi funksiya"""
    malumotlar['ism'] = ism
    malumotlar['familiya'] = familiya
    return malumotlar
talaba1 = talaba_info("Oybek", "Olimov")
talaba2 = talaba_info("Hakim", "Samadov", t_yil=2000, fakultet='matematika')
print(talaba1)
print(talaba2)