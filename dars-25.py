"""
DARS - 25 | Son Topish O'yini 
3/09/2021
"""
import random as r

def tekshir_komp(oylangan_son, taxmin_son, urinish):
    if oylangan_son != taxmin_son:
        if oylangan_son > taxmin_son:
            holat = "kattaroq"
        else:
            holat = "kichikroq"
        return print(f"Xato! Men oylagan son bundan {holat}. Yana harakat qilib ko'ring.")
    else:
        print(f"TOPDINGIZ! {oylangan_son} sonini o'ylagan edim. {urinish} ta urunishda topdingiz. Tabriklayman!")
        return 1
        
def yakuniy_natija(h_urinish, c_urinish):
    if c_urinish < h_urinish:
        print(f"Men {c_urinish} ta taxmin bilan topib, sizni yutdim!!!\n")
    elif c_urinish > h_urinish:
        print(f"Siz {h_urinish} ta taxmin bilan topdingiz va yutdingiz!!!\n")
    else:
        print(f"Durrang!  Ikkimiz ham {h_urinish} ta taxmin bilan topdik.")


A = True

print("Keling, o'ylangan sonni topish o'ynaymiz!")

while A:
    oylangan_son = r.randint(1,10)
    h_urinish, c_urinish = 0, 0
    taxmin_son = int(input("1 dan 10 gacha bir son o'yladim. Topa olasizmi?\n>>> "))
    while True:
        h_urinish += 1
        if tekshir_komp(oylangan_son, taxmin_son, h_urinish) == 1:
            break
        taxmin_son = int(input(""))
    
    print("1 dan 10 gacha son o'ylang. Men topishga harakat qilaman.")
    start = input("Son o'ylagan bo'lsangiz, istalgan tugmani bosing.")
    if start != "" or start != "\n":
        aniqlash_xabari = "To'gri (T), men o'ylagan son bundan kattaroq (+), yoki kichikroq (-)?? "
        c_son = r.randint(1, 10)
        c_son_old = 1
        c_son_max = 10
        while True:
            c_urinish += 1
            ask = input(f"Siz {c_son} sonini o'yladingiz: " + aniqlash_xabari)
            if c_son_old > c_son and c_son < c_son_max:
                print("Meni aldamang")
                break
            if ask == "+":
                c_son_old = c_son + 1
                c_son = r.randint(c_son_old, c_son_max)
            elif ask == "-":
                c_son_max = c_son - 1
                c_son = r.randint(c_son_old, c_son_max)
            elif ask == "T" or ask == "t":
                print(f"Soningizni {c_urinish} ta taxmin bilan topdim!")
                break

    yakuniy_natija(h_urinish, c_urinish)

    yanami = int(input("Yana o'ynaymizmi: ha(1) / yo'q(0): "))
    if yanami == 1:
        A = True
    else:
        A = False
