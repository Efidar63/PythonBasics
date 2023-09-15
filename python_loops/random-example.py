'''
1-100 arasinda rastgele uretilecek sayi(hak=5)
**"random modulu" icin "python random" seklinde arama yapin
***100 uzerinden puanlama yapin.her soru 20 puan
***hak bilgisini kullanicidan alin ve her soru belirtilen can sayisi uzerinden hesaplansin.

'''


import random

sayi=random.randint(1,10)
can=int(input('kac hak kullanmak istersiniz: '))
hak=can
sayac=0
while hak>0:
    hak-=1
    sayac+=1
    tahmin=int(input('tahmin: '))

    if sayi==tahmin:
        print(f'tebrikler {sayac}.defada bildiniz. Toplam puaniniz: {100-(100/can)*(sayac-1)}')
        break

    elif sayi>tahmin:
        print('yukari')
    else:
        print('asagi')
 
if hak==0:
    print('hakkiniz bitti.')
