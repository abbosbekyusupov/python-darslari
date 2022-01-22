# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 22:20:21 2022

@author: yusup
"""
yosh = int(input("Yoshingiz nechida?\n>>>"))
if yosh<=4:
    print("Sizga kirish bepul")
elif yosh<=12:
    print("Sizga kirish 5000 so'm")
elif yosh<=18:
    print("Sizga kirish 8000 so'm")
else:
    print("Sizga kirish 10000 so'm")

#yosh = int(input("Yoshingiz nechida?\n>>>"))
#if yosh<=4:
#    narx = 0
#elif yosh<=12:
#    narx = 5000
#elif yosh<=18:
#    narx = 8000
#else:
#    narx = 10000
    
#print(f"Sizga kirish {narx} so'm")

#kun = input("Bugun qaysi kun?>>> ")
#if kun.lower()=='shanba' or kun.lower()=='yakshanba':
#    print("Bugun dam olish kuni")
#else:
#    print("Bugun ish kuni")

#kun = input("Bugun qaysi kun?>>> ")
#harorat = float(input("Havo harorati qanday?>>> "))
#if kun.lower()=='yakshanba' or kun.lower()=='shanba' and harorat>=30:
#    print("Cho'milishga ketdik!")
#elif kun.lower()=='yakshanba' or kun.lower()=='shanba' and harorat<30:
#    print("Uyda dam olamiz!")

#narx = 15000
#choy = True
#salad = True

#if choy and salad:
#    narx = narx + 10000
#elif choy or salad:
#    narx = narx + 5000
    
#print(f"Jami {narx} so'm")


#narx = 15000
#choy = 1
#salat = 0
#non = 1
#kompot = 1
#assorti = 1

#if choy:
#    print("MIjoz choy oldi")
#    narx = narx + 3000
#if salat:
#    print("Mijoz salat oldi")
#    narx = narx + 5000
#if non:
#    print("Mijoz non oldi")
#    narx = narx + 2000
#if kompot:
#    print("Mijoz kompot oldi")
#    narx = narx + 5000
#if assorti:
#    print("Mijoz assorti oldi")
#    narx = narx + 15000
    
#print(f"Jami {narx} so'm")


#menu = ['osh', 'qozonkabob', 'shashlik', 'norin', 'somsa']
#'manti' in menu


#menu = ['osh', 'qozonkabob', 'shashlik', 'norin', 'somsa']
#ovqat = input("Nima ovqat yaysiz?>>> ")
#if ovqat.lower() not in menu:
#    print("Afsuski bizda bunday ovqat yo'q")
#else:
#    print("Buyurtma qabul qilindi")


#menu = ['osh', 'qozonkabob', 'shashlik', 'norin', 'somsa']
#buyurtmalar = ['osh', 'qozonkabob', 'manti', 'shashlik']
#for taom in buyurtmalar:
#    if taom in menu:
#        print(f"Menuda {taom} bor")
#    else:
#        print(f"Kechirasiz, menuda {taom} yo'q")


#AMALIYOT

#son = int(input("Juft son kiriting: "))
#if son%2:
#    print("Bu juft son emas.")
#else:
#    print("Rahmat!")


#yosh = int(input("Yoshingiz nechida?>>> "))
#if yosh<=4 or yosh>=60:
#    print("Sizga kirish bepul.")
#elif yosh<18:
#    print("Sizga kirish 10000 so'm.")
#elif yosh>=18:
#    print("Sizga kirish 20000 so'm.")

#yosh = int(input("Yoshingiz nechida?>>> "))
#if yosh<=4 or yosh>=60:
#    price=0
#elif yosh<18:
#    price=10000
#elif yosh>=18:
#    price=20000
#print(f"Sizga kirish {price} so'm.")


#a = float(input("1-sonni kiriting: "))
#b = float(input("2-sonni kiriting: "))
#if a>b:
#    print("a>b")
#elif a<b:
#    print("a<b")
#else:
#    print("a=b")


#mahsulotlar = ["un", "tuz", "choy", "makaron", "go'sht", "kolbasa", "salfetka", "guruch", "shakar", "lag'mon"]
#savat = []
#for n in range(5):
#    savat.append(input(f"Savatga {n+1}-mahsulotni kiriting: "))
#for mahsulot in savat:
#    if mahsulot in mahsulotlar:
#        print(f"Do'konimizda {mahsulot} bor")
#    else:
#        print(f"Do'konimizda {mahsulot} yo'q")


