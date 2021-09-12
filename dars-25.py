"""
DARS - 25 | Son Topish O'yini 
3/09/2021
"""
import random as r

# oylangan_son = 7
# urinish = 0

# print("Keling, o'ylangan sonni topish o'ynaymiz!")
# taxmin_son = int(input("1 dan 10 gacha bir son o'yladim. Topa olasizmi?\n>>> "))

# def tekshir_komp(oylangan_son, taxmin_son, *urinish):
#     if oylangan_son != taxmin_son:
#         if oylangan_son > taxmin_son:
#             holat = "kattaroq"
#         else:
#             holat = "kichikroq"
#         return print(f"Xato! Men oylagan son bundan {holat}. Yana harakat qilib ko'ring.")
#     else:
#         return print(f"TOPDINGIZ! {oylangan_son} sonini o'ylagan edim. {urinish} ta urunishda topdingiz. Tabriklayman!")

    
print("1 dan 10 gacha son o'ylang. Men topishga harakat qilaman.")
print("Son o'ylagan bo'lsangiz, istalgan tugmani bosing.")

ask = ": To'g'ri (T), men o'ylgan son bundan kattaroq (+), yoki kichikroq (-)?\n>>> "
def tekshir_odam(ask,*urinish):
    print(f"Siz {urinish} sonini o'yladingiz{ask}")

def taxmin_qil(*args):    
    return r.randrange(1,11)
print(taxmin_qil())

# Chellengew Messege bor
while True:
    yanami = int(input("Yana o'ynaymizmi: ha(1) / yo'q(0): "))
    if yanami == 1:
        #code bor
        continue
    else:
        break
        