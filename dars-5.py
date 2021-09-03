"""
#05 Python Darslari | mtn bilan ishlash (String)
20/8/2021
"""


ism = 'sobirjon'
familiya = 'habibullaev'

# methodlar - namuna: variable.method() ko'rinishida bo'ladi

ism_sharif = f"{ism} {familiya}"

print(ism_sharif.upper())
print(ism_sharif.lower())
print(ism_sharif.title())
print(ism_sharif.capitalize())


print(f"Salom, mening ismim {ism}, familiyam {familiya}!")
print(f"Salom, mening ismim {ism.title()}, familiyam {familiya.title()}!")
print(f"Salom, mening ismim {ism}, familiyam {familiya}!")

# methodni variable ga tenglab olib natijani variable ko'rinishda istalgan yerda foydalanish mumkin.

ism = ism.title()
familiya = familiya.title()

print(f"Salom, mening ismim {ism}, familiyam {familiya}!")


##############

meva = "          olma            "

print(meva)

# lstrip() method i chap tarafdagi bo'shliqni olib tashlaydi.
print(meva.lstrip())

# rstrip() method i esa o'ng tarafdagi bo'shliqni olib tashlaydi.
print(meva.rstrip())

# strip() method i ikki tarafdagi bo'shliqlarni olib tashlaydi.
print(meva.strip())

ism = input("Ismingiz nima?\n>>> ")
print("Assalomu alaykum, {}".format(ism))
