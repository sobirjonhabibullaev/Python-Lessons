"""
22/08/2021
Dars - 9 | FOR LOOP
"""

mehmonlar = ["Ali", "Vali", "Hasan", "Husan", "Olim", "Jamol", "Shuxrat", "Usmon"]
for mehmon in mehmonlar:
    print("Salom", mehmon) 

sonlar = list(range(1,11))
for son in sonlar:
    print(f"{son}ning kvadrati {son**2}ga teng")

dostlar =  []
for n in range(5):
    dostlar.append(input(f"{n+1}-do'stingizni kiriting: "))
print(dostlar)