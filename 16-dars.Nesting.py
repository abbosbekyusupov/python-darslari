# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 21:23:01 2022

@author: yusup
"""

#16-dars: Nesting

car0 = {
        'model':'lacetti',
        'rang':'oq',
        'yil':2018,
        'narx':13000,
        'km':50000,
        'korobka':'avtomat'
        }

car1  = {
    'model':'nexia 3',
    'rang':'qora',
    'yil':2015,
    'narx':9000,
    'km':89000,
    'korobka':'mexanika'
    }

car2 = {
        'model':'gentra',
        'rang':'qizil',
        'yil':2019,
        'narx':15000,
        'km':20000,
        'korobka':'mexanika'
        }

#car = car0
#print(f"{car['model'].title()},"
#      f"{car['rang']} rang,"
#      f"{car['yil']}-yil, {car['narx']}$")
#car = car1
#print(f"{car['model'].title()},"
#      f"{car['rang']} rang,"
#      f"{car['yil']}-yil, {car['narx']}$")
#car = car2
#print(f"{car['model'].title()},"
#      f"{car['rang']} rang,"
#      f"{car['yil']}-yil, {car['narx']}$")


#cars = [car0, car1, car2]
#for car in cars:
#    print(f"{car['model'].title()},"
#          f"{car['rang']} rang,"
#          f"{car['yil']}-yil, {car['narx']}$")


#malibus = []
#for n in range(10):
#    new_car = {
#        'model':'malibu',
#        'rang':None,
#        'yil':2020,
#        'narx':None,
#        'km':0,
#        'karobka':'avtomat'
#        }
#    malibus.append(new_car)
    
#for malibu in malibus[:3]:
#    malibu['rang'] = 'qizil'
    
#for malibu in malibus:
#    print(malibu)
    
#for malibu in malibus[3:6]:
#    malibu['rang'] = 'qora'
    
#for malibu in malibus:
#    print(malibu)
    
#for malibu in malibus[6:]:
#    malibu['rang'] = 'qora'
#    malibu['karobka'] = 'mexanika'
    
#for malibu in malibus:
#    print(malibu)
    
#for malibu in malibus:
#    if malibu['karobka']=='avtomat':
#        malibu['narx']=40000
#    else:
#        malibu['narx']=35000

#for malibu in malibus:

#    print(malibu)
    
#dasturchilar = {
#    'ali':['python', 'c++'],
#    'vali':['html', 'css', 'js'],
#    'hasan':['php', 'sql'],
#    'husan':['python', 'php'],
#    'maryam':['c++', 'c#']
#    }

#for ism, tillar in dasturchilar.items():
#    print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi: ")
#    for til in tillar:
#        print(til.upper())
        
        
#for ism, tillar in dasturchilar.items():
#    print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi: ", end='')
#    for til in tillar:
#        print(f'{til.upper()} ', end='')
        
        
#hamkasblar = {
#    'ali':{'familiya':'valiyev',
#           'tyil':1995,
#           'malumot':'oliy',
#           'tillar':['python','c++']
#           },
#    'vali':{'familiya':'aliyev',
#            'tyil':2001,
#            'malumot':"o'rta-maxsus",
#            'tillar':['html', 'css', 'js']},
#    'hasan':{'familiya':'husanov',
#             'tyil':1999,
#             'malumot':'maxsus',
#             'tillar':['python','php']}
#    }

#for ism, info in hamkasblar.items():
#    print(f"\n{ism.title()} {info['familiya'].title()}, "
#          f"{info['tyil']}-yilda tug'ilgan. "
#          f"Ma'lumoti: {info['malumot']}. \n"
#          "Quyidagi dasturlash tillarini biladi:")
#    for til in info['tillar']:
#        print(til.upper())
        
        
#AMALIYOT

buxoriy = {'ism':'Abu Abdulloh Muhammad ibn Ismoil',
           'tyil':810,
           'vyil':870,
           'tjoy':'Buxoro',
           'asarlar':["Al-jome’ as-sahih", "Al-adab al-mufrad", "At-tarix al-kabir", "At-tarix as-sag‘ir"]
           }

qodiriy = {'ism':'Abdulla Qodiriy',
           'tyil':1894,
           'vyil':1938,
           'tjoy':'Toshkent',
           'asarlar':["O'tkan kunlar","Mehrobdan Chayon",'Obid ketmon']
           }

vohidov = {'ism':'Erkin Vohidov',
           'tyil':1936,
           'vyil':2016,
           'tjoy':"Farg'ona",
           'asarlar':["Tong nafasi","Qo'shiqlarim sizga","O'zbegim","Qiziquvchan Matmusa"]
           }

navoiy = {'ism':'Alisher Navoiy',
           'tyil':1441,
           'vyil':1501,
           'tjoy':"Xirot",
           'asarlar':["Xamsa","Lison ut-Tayr","Mahbub Al-Qulub",'Munojot']
           }

shaxslar = [buxoriy, qodiriy, vohidov, navoiy]
#for shaxs in shaxslar:
#    print(f"{shaxs['ism'].title()}, "
#         f"{shaxs['tyil']}-yilda {shaxs['tjoy']}da tug'ilgan, "
#          f"{shaxs['vyil']}-yilda vafot etgan.")

#for shaxs in shaxslar:
#    ism = shaxs['ism']
#    asarlar = shaxs['asarlar']
#    print(f"\n{ism} ning mashxur asarlari: ")
#    for asar in asarlar:
#        print(asar)


kinolar = {
    'ali':['Terminator','Rambo','Titanic'],
    'vali':['Tenet','Inception','Interstellar'],
    'hasan':['Abdullajon','Bomba','Shaytanat'],
    'husan':['Mahallada duv-duv gap','John Wick']
    }

#for ism, kinolar in kinolar.items():
#    print(f"\n{ism.title()}ning sevimli kinolari:")
#    for kino in kinolar:
#        print(kino)


davlatlar = {
    'rossiya':{'poytaxt':'moskva',
               'maydon':17_075_400,
               'myil':1991
               },
    'o\'zbekiston':{'poytaxt':'toshkent',
                    'maydon':448_978,
                    'myil':1991
                    },
    'germaniya':{'poytaxt':'berlin',
                 'maydon':357_386,
                 'myil':1949
                 },
    'aqsh':{'poytaxt':'qashington d.c.',
            'maydon':9_834_000,
            'myil':1776
            }
    }

davlat = input('Davlat nomini kiriting: ').lower()
if davlat in davlatlar:
    info = davlatlar[davlat]
    print(f"\n{davlat.capitalize()}ning poytaxti {info['poytaxt'].title()}"
          f"\nHududi: {info['maydon']} kv.km"
          f"\nMustaqillik yili: {info['myil']}")
else:
    print("Bizda bu davlat haqida ma'lumot mavjud emas")