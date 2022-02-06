# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 22:53:30 2022

@author: yusup
"""

def avto_info(kompaniya, model, rangi, korobka, yili, narxi=None):
    avto = {'kompaniya':kompaniya,
            'model':model,
            'rangi':rangi,
            'korobka':korobka,
            'yil':yili,
            'narx':narxi
            }
    return avto

def avto_kirit():
    """Foydalanuvchiga avto_info funksiyasi yordamida bir nechta avtolar haqida ma'lumotlarni bittada chiqarib beradigan funksiya"""
    avtolar = []
    while True:
        print("\nQuyidagi ma'lumotlarni kiriting: ")
        kompaniya = input("Ishlab chiqaruvchi: ")
        model = input("Modeli: ")
        rangi = input("Rangi: ")
        korobka = input("Korobka: ")
        yili = input("Ishlab chiqarilgan yili: ")
        narxi = input("Narxi: ")
        
        avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narxi))
        javob = input("Yana avto qo'shasizmi? (ha/yo'q): ")
        if javob=="yo'q":
            break
    
    
def info_print(avto_info):
    """Avtomobillar haqida ma'lumotlar saqlangan lug'atni konsolga chiqaruvchi funksiya"""
    print(f"{avto_info['rangi'].title()} {avto_info['kompaniya'].upper()} "
          f"{avto_info['model'].upper()}, {avto_info['korobka']} korobka,"
          f"{avto_info['yil']}-yil, {avto_info['narx']}$")