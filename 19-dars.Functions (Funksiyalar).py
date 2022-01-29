# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 21:34:01 2022

@author: yusup
"""

#19-dars: FUNCTIONS (FUNKSIYALAR)

#def salom_ber():
#    """Salom beruvchi funksiya"""
#    print("Assalomu alaykum")

#salom_ber()


#def salom_ber(ism):
#    """Foydalanuvchining ismini qabul qilib,
#    unga salom beruvchi funksiya"""
#    print(f"Assalomu alaykum, hurmatli {ism.title()}")
    
#salom_ber('hasan')
#salom_ber('olim')


#def toliq_ism(ism, familiya):
#    """Foydalanuvchi ismi va familiyasini jamlab chiqaruvchi funksiya"""
#    print(f"Foydalanuvchi ismi: {ism.title()}",
#          f"Foydalanuvchi familiyasi: {familiya.title()}")
#toliq_ism('abbosbek', 'yusupov')


#def yosh_hisobla(ism, tugilgan_yil):
#    """Foydalanuvchining yoshini hisoblaydigan funksiya"""
#    print(f"{ism.title()} {2022-tugilgan_yil} yoshda")
#yosh_hisobla('abbosbek', 2003)
#yosh_hisobla(tugilgan_yil=2003, ism='abbosbek')


#def yosh_hisobla(tugilgan_yil, joriy_yil=2022):
#    """Foydalanuvchi tugilgan yilidan yoshini hisoblaydi"""
#    print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")
#yosh_hisobla(2003,2022)
#yosh_hisobla(2003)


#AMALIYOT

#def tugilgan_yil(ism, yosh):
#    """Foydalanuvchi ismi va yoshini so'rab, uning tugilgan yilini chiqaruvchi funksiya"""
#    print(f"Foydalanuvchi ismi: {ism.title()}",
#          f"\nFoydalanuvchi yoshi: {yosh}",
#          f"\n{ism.title()}, siz {2022-yosh}-yilda tug'ilgan ekansiz")
#tugilgan_yil('olim', 23)


#def son_kirit(son):
#    """Foydalanuvchi kiritgan sonning kvadrati va kubini chiqaruvchi funksiya"""
#    print(f"Kiritilgan sonning kvadrati {son**2} ga teng",
#          f"\nKiritlgan sonning kubi {son**3} ga teng")
#son_kirit(6)


#def son_chiqar(son):
#    """Foydalanuvchi kiritgan sonning juft yoki toqligiini chiqaruvchi funksiya"""
#   if son%2==0:
#        print("Kiritilgan son juft")
#    else:
#        print("Kiritilgan son toq")
#son_chiqar(12)


#def sonni_kirit(son1, son2):
#    """Foydalanuvchidan 2 ta son olib, kattasini chiqaruvchi dastur"""
#    if son1>son2:
#        print(son1)
#    elif son1<son2:
#        print(son2)
#    elif son1==son2:
#        print('Sonlar teng')
#sonni_kirit(12, 12)


#def sonlar(x, y):
#    print(f"{x-y}")
#sonlar(18, 10)


#def sonlar(x, y=2):
#    print((x+y)**2)
#sonlar(13)


def bolinish_alomatlari(son):
    for n in range(2,11):
        if not son%n:
            print(f"{son} {n} ga qoldiqsiz bo'linadi")

bolinish_alomatlari(20)