# -*- coding: utf-8 -*-
"""
Created on Mon Jan 24 20:07:07 2022

@author: yusup
"""

#15-dars: Lug'at bilan ishlash

talaba_0 = {
    'ism':'alijon',
    'familiya':'shamshiyev',
    'yosh':22,
    'fakultet':'matematika',
    'kurs':4
    }

#print(talaba_0.items())

#for kalit, qiymat in talaba_0.items():
#    print(f"Kalit: {kalit}")
#    print(f"Qiymat: {qiymat}")

telefonlar = {
    'ali': 'iphone X',
    'vali': 'galaxy s9',
    'olim': 'mi 10 pro',
    'orif': 'nokia 3310',
    'anvar': 'pixel 3xl'
    }

#for k, q in telefonlar.items():
#    print(f"{k.title()}ning telefoni {q}")


mahsulotlar = {
    'olma':10000,
    'anor':20000,
    'uzum':40000,
    'anjir':25000,
    'shaftoli':30000
    }
#print(mahsulotlar.keys())

#print('Do\'kondagi mahsulotlar: ')
#for mahsulot in mahsulotlar:
#    print(mahsulot.title())


bozorlik = ['anor', 'uzum', 'non', 'baliq']
#for mahsulot in mahsulotlar:
#    if mahsulot in bozorlik:
#        print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")
        
#for buyum in bozorlik:
#    if buyum not in mahsulotlar:
#        print(f"Iltimos, do'koningizga {buyum} ham olib keling")
        
#print("Do'konimizdagi mahsulotlar: ")
#for mahsulot in sorted(mahsulotlar):
#    print(mahsulot.title())


#print(telefonlar.values())

#print("Foydalanuvchilar quyidagi telefonlarni ishlatadilar: ")
#for tel in telefonlar.values():
#    print(tel)


telefonlar = {
    'ali': 'iphone X',
    'vali': 'galaxy s9',
    'olim': 'mi 10 pro',
    'orif': 'nokia 3310',
    'anvar': 'pixel 3xl',
    'hamida':'galaxy s9',
    'maryam':'huawei p30',
    'tohir':'iphone x',
    'umar':'iphone x'
    }

#print("Foydalanuvchilar quyidagi telefonlarni ishlatadilar:")
#for tel in telefonlar.values():
#    print(tel)
    
#print("Foydalanuvchilar quyidagi telefonlarni ishlatadilar:")
#for tel in set(telefonlar.values()):
#    print(tel)


toys = {"ball", "car", "lamp", "ball", "bear", "car"}
#print(toys)

#AMALIYOT

p_dict = {
    'keys':'kalit so\'z',
    'value':'qiymat',
    'variable':'o\'zgaruvchi',
    'string':'matn',
    'float':'o\'nlik son',
    'integer':'butun son',
    'konstanta':'o\'zgarmas qiymat',
    'list':'ro\'yxat',
    'function':'funksiya',
    'boolean':'mantiqiy qiymatlar'
    }
#for k, q in sorted(p_dict.items()):
#   print(f"{k.title()} - {q}")


capitals = {
    'fransiya':'parij',
    'ispaniya':'madrid',
    'portugaliya':'lissabon',
    'janubiy koreya':'seul',
    'yaponiya':'tokiyo',
    'o\'zbekiston':'toshkent',
    'rossiya':'moskva',
    'misr':'qoira',
    'turkiya':'istanbul'
    }
#print("Davlatlar nomi:")
#for keys in sorted(capitals.keys()):
#    print(keys.upper())
#print("\nPoytaxtlar nomi:")
#for values in sorted(capitals.values()):
#    print(values.title())


capitals = {
    'fransiya':'parij',
    'ispaniya':'madrid',
    'portugaliya':'lissabon',
    'janubiy koreya':'seul',
    'yaponiya':'tokiyo',
    'o\'zbekiston':'toshkent',
    'rossiya':'moskva',
    'misr':'qoira',
    'turkiya':'istanbul'
    }
#country = input("Qaysi davlatnng poytaxtini biishni istaysiz?: ")
#capital = capitals.get(country)
#if country==None:
#    print("Bizda bunday ma'lumot yo'q")
#else:
#    print(f"{country.upper()}ning poytaxti {capital.title()}")


menu = {
        'osh':60000,
        'shashlik':25000,
        'sho\'rva':18000,
        'qozonkabob':50000,
        'somsa':23000,
        'tovuq':30000,
        'manti':10000,
        'baliq':25000,
        'lag\'mon':20000,
        'go\'shtli assorti':150000
        }
#taom1 = input("1-taomni buyurtma qiling: ")
#narx1 = menu.get(taom1)
#taom2 = input("2-taomni buyurtma qiling: ")
#narx2 = menu.get(taom2)
#taom3 = input("3-taomni buyurtma qiling: ")
#narx3 = menu.get(taom3)
#if taom1 in menu:
#    print(f"\n{taom1.title()}ning narxi {narx1} so'm")
#else:
#    print("Bizda bunday taom yo'q")
#if taom2 in menu:
#    print(f"{taom2.title()}ning narxi {narx2} so'm")
#else:
#    print("Bizda bunday taom yo'q")
#if taom3 in menu:
#    print(f"{taom3.title()}ning narxi {narx3} so'm")
#else:
#    print("Bizda bunday taom yo'q")
    
    
    
menu = {
        'osh':20000,
        "lag'mon":22000,
        'non':4000,
        'choy':5000,
        'shashlik':12000,
        'somsa':6000,
        'tabaka':15000
        }

print('3 ta taom buyurtma bering.')
buyurtmalar = []
for n in range(3):
    buyurtmalar.append(input(f"{n+1}-taom:").lower())

for buyurtma in buyurtmalar:
    if buyurtma in menu:
        print(f"{buyurtma.title()} {menu[buyurtma]} so'm")
    else:
        print(f"Kechirasiz, bizda {buyurtma} yo'q.")