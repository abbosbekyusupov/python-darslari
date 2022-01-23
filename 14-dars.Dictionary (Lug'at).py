# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 17:28:37 2022

@author: yusup
"""

#14-dars: Dictionary (Lug'at)

car_o = {'model':'ferrari', 'rang':'qizil'}
#print(car_o['model'])
#print(car_o['rang'])

en_uz = {'apple':'olma', 'apricot':"o'rik", 'banana':'banan'}
#print(en_uz['apple'])

mevalar = {'olma':10000, 'tarvuz':8000, 'qovun':10000}
#print(mevalar['olma'])
#print(mevalar['tarvuz'])

talaba_0 = {'ism':'murod olimov', 'yosh':20, 't_yil':2002}
#print(f"{talaba_0['ism'].title()}, \
#      {talaba_0['t_yil']}-yilda tug'ilgan, \
#       {talaba_0['yosh']} yoshda")
       
talaba_0['kurs'] = 4
talaba_0['fakultet'] = 'informatika'
talaba_0['ism'] = 'abdulloh'

talaba_1 = {}
talaba_1['ism'] = 'qobil rasulov'
talaba_1['kurs'] = 3
talaba_1['yosh'] = 200
#print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kursda o'qiydi")

talaba_1['kurs'] = 4
#print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kursda o'qiydi")

talaba_0 = {'ism':'murod olimov', 'yosh':20, 't_yil':2002}
del talaba_0['yosh']

en_uz = {'apple':'olma', 'apricot':"o'rik", 'banana':'banan'}
del en_uz['banana']

telefonlar = {
    'ali': 'iphone X',
    'vali': 'galaxy s9',
    'olim': 'mi 10 pro',
    'orif': 'nokia 3310',
    'anvar': 'pixel 3xl'
    }

phone = telefonlar.get('ali', 'Bunday ism mavjud emas')
#print(phone)

meva = en_uz.get('apple', 'Bunday meva mavjud emas')
#print(meva)

meva = en_uz.get('pineapple', 'Bunday meva mavjud emas')
#print(meva)

phone = telefonlar.get('hasan')
#print(phone)

#AMALIYOT

otam = {'ism':'habibulla usmonov', 't_yil':1977, 'manzil':'jizzax', 'yosh':45}
#print(f"Otamning ismi {otam['ism'].title()},\
      #{otam['t_yil']}-yilda, {otam['manzil'].title()} tumanida tug'ilgan.")
      
      
taomlar = {
    'habibulla':'osh',
    'gulnihol':'shashlik',
    'madina':'honim',
    'shahbozbek':'manti',
    'abbosbek':'chuchvara'
    }
print(f"Dadamning ismlari Habibulla. Ularning yaxshi ko'rgan ovqati {taomlar['habibulla']}.\
      Onamning ismlari Gulnihol. Ularning yaxshi ko'rgan ovqati {taomlar['gulnihol']}.\
      Singlim Madinaning yaxshi ko'rgan ovqati {taomlar['madina']}.\
      Ukam Shahbozbekning yaxshi ko'rgan ovqati {taomlar['shahbozbek']}.\
      Mening ismim Abbosbek va mening sevimli ovqatim {taomlar['abbosbek']}.")
