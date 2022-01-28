# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 08:56:13 2022

@author: yusup
"""

#17-dars: INPUT() VA WHILE

#ism = input("Ismingiz nima? ")
#savol = f"Salom, {ism.title()}. Yoshingiz nechida? "
#yosh = input(savol)

#ism = input("Ismingiz nima? ")
#savol = f"Salom, {ism.title()}. Yoshingiz nechida? "
#yosh = input(savol)
#yosh = int(yosh)
#height = input("Bo'yingiz necha metr? ")
#height = float(height)

#son = 1 # son ga 1 qiymatini beramiz
#while son<=5: # toki son 5 dan kichik yoki teng ekan...
#    print(son, end=' ') # son ni konsolga chiqaramiz,
#    son = son+1 # songa 1 qo'shamiz.
    
    
#print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
#savol = "Istalgan son kiriting "
#savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
#qiymat = ''
#while qiymat != 'exit':
#    qiymat = input(savol)
#    if qiymat != 'exit':
#        print(float(qiymat)**2)
        
        
#print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
#savol = "Istalgan son kiriting "
#savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
#ishora = True
#while ishora:
#    qiymat = input(savol)
#    if qiymat == 'exit':
#        ishora = False
#    else:
#        print(float(qiymat)**2)
              
              
#print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
#savol = "Istalgan son kiriting "
#savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

#while True: # abadiy tsikl
#    qiymat = input(savol)
#    if qiymat == 'exit':
#        break # tsiklni to'xtatish
#    else:
#        print(float(qiymat)**2)
        
        
#sonlar = list(range(1,11))
#for son in sonlar: 
#    if son == 5: # son 5 ga teng bo'lsa kod to'xtaydi
#        break
#    print(f"{son} ning kvadrati {son**2} ga teng")
    
    
#sonlar = list(range(1,11))
#for son in sonlar:
#    if son == 5: # son 5 ga teng bo'lsa tiskl boshiga qaytadi
#        continue
#    print(f"{son} ning kvadrati {son**2} ga teng")
    
    
#son = 0
#while son<10:
#    son += 1
#    if son%2!=0:
#        continue
#    else:
#        print(son)
        

#AMALIYOT

#print("Yoqtirgan kitobni chiqaradigan dastur.")
#kitoblar = "Yoqtirgan kitoblaringizni kiriting"
#kitoblar += " (dasturni to'xtatish uchun 'stop' deb yozing): "
#qiymat = ''
#while qiymat !='stop':
#    qiymat = input(kitoblar)
#    if qiymat != 'stop':
#        print(qiymat)
#print("Dastur to'xtadi")


print("Muzeyga chipta narxini yoshga qarab chiqarib beradigan dastur.")
savol = "Yoshingizni kiriting: "

while True:
    qiymat = input(savol)
    if qiymat == 'exit' or qiymat == 'quit':
        break
    yosh = int(qiymat)
    
    if yosh<7:
        narh = 2000
    elif 7<=yosh<18:
        narh = 3000
    elif 18<=yosh<65:
        narh = 10000
    else: narh = 0
    
    if narh==0:
        print("Sizga chipta bepul")
    else:
        print(f"Chipta {narh} so'm")