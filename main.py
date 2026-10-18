import random

print("Gizli sayiyi bul")
print("1 ile 100 arasinda bir sayi tuttum.")
print("bulmak icin 7 hakkin var")

gizli_sayi = random.randint(1, 100)
kalan_hak = 7

while kalan_hak > 0:
    print(f"\nkalan hakkin:{kalan_hak}")
    cevap = input("Tahminin: ")

    try:
        tahmin = int(cevap)

    except ValueError:
        print("lutfen tam sayi yaz. Ornegin : 25")
        continue

    if tahmin < 1 or tahmin > 100:
        print("1 ile 100 arasinda bir sayi yaz.")
        continue

    kalan_hak = kalan_hak - 1

    if tahmin == gizli_sayi:
        print("Tebrikler! Gizli sayiyi buldun chucky! ")
        print(f"toplam {7-kalan_hak} denemede bildin")
        break
    elif tahmin < gizli_sayi:
        print("daha buyuk bir sayi dene")
    else:
        print("Daha kucuk bir sayi dene")
if kalan_hak == 0 and tahmin != gizli_sayi:
    print(f"\n Oyun Bitti! Gizli sayi :{gizli_sayi}")

print("Oynadigin icin tesekkurler chucky!")