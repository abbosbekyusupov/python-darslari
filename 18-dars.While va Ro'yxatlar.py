# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 21:22:57 2022

@author: yusup
"""

#18-dars: WHILE VA RO'YXATLAR

#print("Yaqin do'stlaringiz ro'yxatini tuzamiz.")
#ismlar = []
#n=1
#while True:
#    savol = f"{n}-do'stingiz ismini kiriting: "
#    ism = input(savol)
#    ismlar.append(ism)
#    takrorlash = input("Yana ism qo'shasizmi? (ha/yo'q): ")
#    n+=1
#    if takrorlash != 'ha':
#        break
    
#print("Do'stlaringiz ro'yxati:")
#for ism in ismlar:
#    print(ism.title())


#print("Do'stlaringiz yoshini saqlaymiz.")
#dostlar = {}
#ishora = True
#while ishora:
#    ism = input("Do'stingizning ismini kiriting: ")
#    yosh = input(f"{ism.title()}ning yoshini kiriting: ")
#    dostlar[ism] = int(yosh)
    
#    javob = input("Yana ma'lumot qo'shasizmi? (ha/yo'q): ")
#    if javob == 'yo\'q':
#        ishora = False
        
#for ism, yosh in dostlar.items():
#    print(f"{ism.title()} {yosh} yoshda")
    
    
#cars = ['lacetti', 'nexia', 'toyota', 'nexia', 'audi', 'malibu', 'nexia']
#while 'nexia' in cars:
#    cars.remove('nexia')
#print(cars)


#talabalar = ['hasan', 'husan', 'olim', 'botir']
#baholangan_talabalar = {}
#while talabalar:
#    talaba = talabalar.pop()
#    baho = input(f"{talaba.title()}ning bahosini kiriting: ")
#    print(f"{talaba.title()} baholandi")
#    baholangan_talabalar[talaba] = int(baho)


#AMALIYOT

#print("Buyurtma qabul qiluvchi dastur.")
#n=1
#buyurtma = []
#while True:
#    savol = f"{n}-mahsulotni kiriting: "
#    mahsulot = input(savol)
#    buyurtma.append(mahsulot)
#    takrorlash = input("Yana buyurtma berasizmi? (ha/yo'q): ")
#    n+=1
#    if takrorlash != 'ha':
#        break
#print(f'Sizning buyurtmangiz:\n{buyurtma}')


#print("e-bozor uchun mahsulotlar va ularning narxlarini ko'rsatuvchi dastur.")
#cost_list = {}
#ishora = True
#while ishora:
#    mahsulot = input("Mahsulotni kiriting: ")
#    narx = input("Narxni belgilang: ")
#    cost_list[mahsulot] = int(narx)
    
#    javob = input("Yana ma'lumot qo'shasizmi? (ha/yo'q): ")
#    if javob == "yo'q":
#        ishora = False


buyurtmalar = ['olma','anjir','uzum','qovun']
mahsulotlar = {'olma':20000,
               'shaftoli':25000,
               'tarvuz':18000,
               'uzum':22000}

while buyurtmalar:
    buyurtma = buyurtmalar.pop()
    if buyurtma in mahsulotlar.keys():
        narh = mahsulotlar[buyurtma]
        print(f"{buyurtma.title()} - {narh} so'm")
    else:
        print(f"Bizda {buyurtma} yo'q")