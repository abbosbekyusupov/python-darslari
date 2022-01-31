# -*- coding: utf-8 -*-
"""
Created on Mon Jan 31 21:16:28 2022

@author: yusup
"""

#20-dars: Funksiyadan qiymat qaytarish

#def toliq_ism_yasa(ism, familiya):
#    """To'liq ism qaytaruvchi funksiya"""
#    toliq_ism = f"{ism} {familiya}"
#    return toliq_ism
#talaba = toliq_ism_yasa('oybek', 'olimov')


#talaba1 = toliq_ism_yasa('olim', 'hakimov')
#talaba2 = toliq_ism_yasa('hakim', 'olimov')
#print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")
#print(f"{talaba1} darsga kechikib keldi")


#def toliq_ism_yasa(ism, familiya, otasining_ismi=''):
#    """To'liq ism qaytaruvchi funksiya"""
#    if otasining_ismi:
#        toliq_ism = f"{ism} {otasining_ismi} {familiya}"
#    else:
#        toliq_ism = f"{ism} {familiya}"
#    return toliq_ism.title()

#talaba1 = toliq_ism_yasa('olim', 'hakimov')
#talaba2 = toliq_ism_yasa('hakim', 'olimov', 'abrorovich')
#print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")


#def avto_info(kompaniya, model, rangi, korobka, yili, narxi=None):
#    avto = {'kompaniya':kompaniya,
#            'model':model,
#            'rangi':rangi,
#            'korobka':korobka,
#            'yil':yili,
#            'narx':narxi
#            }
#    return avto

#avto1 = avto_info('GM', 'Malibu', 'Qora', 'Avtomat', 2018)
#avto2 = avto_info('GM', 'Gentra', 'Oq', 'Mexanika', 2016, 15000)
#avtolar = [avto1, avto2]
#print("Onlayn bozorda mavjud bo'lgan avtomashinalar:")
#for avto in avtolar:
#    if avto['narx']:
#        narx = avto['narx']
#    else:
#        narx = "Noma'lum"
#    print(f"{avto['rangi']} {avto['model']}. Narxi: {narx}")


#def oraliq(min, max,):
#    sonlar = []
#    while min<max:
#        sonlar.append(min)
#        min += 1
#    return sonlar

#print(oraliq(0,10))
#print(oraliq(10,20))


#print("Saytimizdagi avtolar ro'yxatini shakllantiramiz.")
#avtolar = []
#while True:
#    print("\nQuyidagi ma'lumotlarni kiriting: ")
#    kompaniya = input("Ishlab chiqaruvchi: ")
#    model = input("Modeli: ")
#    rangi = input("Rangi: ")
#    korobka = input("Korobka: ")
#    yili = input("Ishlab chiqarilgan yili: ")
#    narxi = input("Narxi: ")
    
#    avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narxi))
#    javob = input("Yana avto qo'shasizmi? (ha/yo'q): ")
#    if javob=="yo'q":
#        break

#print("\nSalonimizdagi avtolar:")
#for avto in avtolar:
#    if avto['narx']:
#        narxi = avto['narx']
#    else:
#        narxi = "Noma'lum"
#    print(f"{avto['rangi'].title()} {avto['model'].title()}, {korobka} korobka. Narxi: {narxi}")


#AMALIYOT

#def anketa_yasa(ism, familiya, tyil, yosh, tjoy, email='', tel_raqam=''):
#    """Foydalanuvchi haqida yuqoridagi ma'lumotlarni chiqaruvchi funksiya"""
#    anketa = {'ism':ism,
#              'familiya':familiya,
#              'tyil':tyil,
#              'tjoy':tjoy,
#              'yosh':yosh,
#              'email':email,
#              'tel_raqam':tel_raqam
#              }
#    return anketa

#print("Foydalanuvchilarning anketalarini yaratamiz.")
#anketalar = []
#while True:
#    print("\nQuyidagi ma'lumotlarni kiriting:")
#    ism = input("Ismingiz: ")
#    familiya = input("Familiyangiz: ")
#    tyil = input("Tug'ilgan yilingiz: ")
#    tjoy = input("Tug'ilgan joyingiz: ")
#    yosh = input("Yoshingiz: ")
#    email = input("Emailingiz: ")
#    tel_raqam = input("Telefon raqamingiz: ")
    
#    anketalar.append(anketa_yasa(ism, familiya, tyil, yosh, tjoy, email, tel_raqam))
#    javob = input("Yana anketa yaratasizmi? (ha/yo'q): ")
#    if javob == "yo'q":
#        break
#print("\nMavjud anketalar:")
#for anketa in anketalar:
#    print(f"{anketa['ism'].title()} {anketa['familiya'].title()} {anketa['tyil']}-yilda {anketa['tjoy'].title()}da tug'ilgan. Hozirda {anketa['yosh']} yoshda. Telefon raqami: {anketa['tel_raqam']}.")
    
    
#def kattasi(x,y,z):
#    max = x
#    if y>=max:
#        max = y
#    if z>=max:
#        max = z
#    return max

#katta_son = kattasi(5, 17, -1)


#def aylana_info(radius, pi=3.14159):
#    aylana = {'radius':radius,
#              'diametr':2*radius,
#              'perimetr':2*radius*pi,
#              'yuza':pi*radius**2
#              }
#    return aylana

#aylana1 = aylana_info(5)


def tub_sonlar_top(min,max):    
    tub_sonlar = []    
    for n in range(min,max+1):
        tub = True
        if (n==1):
            tub = False
        elif(n==2):
            tub = True
        else:
            for x in range(2,n):
                if(n%x==0):
                    tub = False
        if tub:
            tub_sonlar.append(n)
                
    return tub_sonlar

#tub_son_top = tub_sonlar_top(1,20)


def fibonacci(n):
    sonlar = []
    for x in range(n):
        if x==0 or x==1:
            sonlar.append(1)        
        else:
            sonlar.append(sonlar[x-1]+sonlar[x-2])
    return sonlar

fibonacci_son = print(fibonacci(15))