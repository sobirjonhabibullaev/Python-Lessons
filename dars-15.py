"""
15-DARS | Lug'atlar bilan ishlash
25/08/2021
"""
ism_sharif = {"orif": "kobulov", 'kamol': 'yulashev',
              'rustam': 'rajabov', 'ali': "numonov"}

for kalit, qiymat in ism_sharif.items():
    print(f"Ism: {kalit.title()}")
    print(f"Familiya: {qiymat.title()} \n")

print(type(list(ism_sharif.keys())))
print(list(ism_sharif.keys()))

mahsulotlar = {"olma": 7500, "go'sht": 71000, "sabzi": 1200, "guruch": 8000, "piyoz": 2500, "yog'": 19000, "mayiz": 17000}
bozorlik = ["olma", "sabzi", "sedana", "isiriq", "tuxum", "go'sht"]
bor = []
yuq = bozorlik[:]

for mahsulot in mahsulotlar:
    if mahsulot in bozorlik:
        print(f"{mahsulot.capitalize()} bor ekan. Narxi {mahsulotlar[mahsulot]} so'm.")
        bor.append(mahsulot.capitalize())
        yuq.remove(mahsulot)
print(f"{bor} - mahsulotlar bor ekan")
print(f"{yuq} - mahsulotlar yuq ekan")

print(sorted(mahsulotlar))

# set() - ham method bo'lishi mumkin, ham ma'lumot turi. Takrorlanmas ma'lumotlarni o'z ichiga jamlaydi.
toys = {"ball", "lamp", "car", "truck", "ball"} 
print(type(toys)) 
print(toys)