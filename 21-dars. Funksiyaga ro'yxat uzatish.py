# -*- coding: utf-8 -*-
"""
Created on Tue Feb  1 20:57:51 2022

@author: yusup
"""

#21-dars: Funksiyaga ro'yxat uzatish

#def bahola(ismlar):
#    baholar = {}
#    while ismlar:
#        ism = ismlar.pop()
#        baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
#        baholar[ism]=int(baho)
#    return baholar
#talabalar = ['ali', 'vali', 'hasan', 'husan']
#baholar = bahola(talabalar[:])
#print(baholar)


#AMALIYOT

#def katta_harf(matnlar):
#    for i in range(len(matnlar)):
#        matnlar[i] = matnlar[i].title()
#ismlar = ['ali', 'vali', 'hasan', 'husan']
#katta_harf(ismlar)
#print(ismlar)


def katta_harf(matnlar):
    matnlar = matnlar[:]
    for i in range(len(matnlar)):
        matnlar[i]=matnlar[i].title()
    return matnlar

ismlar = ['ali', 'vali', 'hasan', 'husan']
yangi_ismlar = katta_harf(ismlar)
print(ismlar)
print(yangi_ismlar)


def bahola(ismlar):
    baholar = {}
    for ism in ismlar:
        baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
        baholar[ism] = baho
    return baholar
talabalar = ['ali', 'vali', 'hasan', 'husan']
baholar = bahola(talabalar)
print(baholar)
print(talabalar)