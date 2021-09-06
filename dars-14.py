"""
14-DARS | Dictionary (lug'at)
25/08/2021
"""
ism_sharif = {"orif":"kobulov", 'kamol':'yulashev', 'rustam':'rajabov', 'ali':"numonov"}
print(ism_sharif)
print(ism_sharif.keys())
print(ism_sharif.values())
print(ism_sharif.items())

ism = input("Ism kiriting: ")
print(ism_sharif.get(ism.lower(), "Bunday ism bizning ro'yxatda mavjud emas")) # Text bo'lmasa None chiqadi.
