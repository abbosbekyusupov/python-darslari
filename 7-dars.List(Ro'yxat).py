# -*- coding: utf-8 -*-
"""
Created on Sat Jan 15 21:32:06 2022

@author: yusup
"""

#mevalar=['olma', 'anjir', 'shaftoli', "o'rik"]
#print(mevalar)
#narxlar=[12000, 18000, 10900, 22000]
#print(narxlar)
#sonlar=['bir', 'ikki', 3, 4, 5]
#print(sonlar)
#ismlar=[] #bo'sh ro'yxat
#print(ismlar)

#print("Birinchi meva: ", mevalar[0])
#print("Uchinchi meva: ", mevalar[2])
#print("Oxirgi meva: ", mevalar[3])

#hayvonlar= ['it', 'mushuk', 'sigir', 'qo\'y', 'quyon', 'mushuk']
#bozorlik= ["yog'", "un", "piyoz", "banan", "go'sht"]
#mahsulot= bozorlik.pop(1)
#print("Men " + mahsulot + " sotib oldim")
#print("Olmagan mahsulotlar: ", bozorlik)

#AMALIYOT

d_ismlari = ["Oybek", "Sunnat", "Firdavs", "Nurislomxon"] #do'stlarimning ismlari
ism=d_ismlari.pop(0)
ism2=d_ismlari.pop()
print("Salom " + ism + ',' + " bugun choyxona bormi?")
print(ism2 + ',' + " choyxonaga boramizmi?")

sonlar = [3, 5, 7, 12, -15, 17.3]
sonlar[3] = 28.9
print((sonlar[0]+sonlar[1])*sonlar[2])
print(sonlar)
sonlar[-1] = sonlar[-1] - 0.8
print(sonlar)

t_shaxslar = ["Imom al-Buxoriy", " Hazrati Umar", "Hazrati Abu Bakr", "Hazrati Usmon", "Hazrati Ali"]
z_shaxslar = ["Abdulloh domla", "Muhammadali Eshonqulov", "Umidjon Eshmuhammedov"]
print("Men tarixiy shaxslardan " + t_shaxslar.pop(1) + " bilan, \nzamonaviy shaxslardan esa " + z_shaxslar.pop(0) + " bilan suhbat qilishni istar edim.")

friends=[]
friends.append("Oybek")
friends.append("Sunnat")
friends.append("Firdavs")
friends.append("Nurislomxon")
friends.append("Muhammad")
print("Mehmonga ", friends, " do'stlarimni chaqiraman.")
friends.remove("Oybek")
print(friends)