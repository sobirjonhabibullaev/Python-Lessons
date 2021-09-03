"""
#03 Python Darslari | print(), Arifmetik amallar va Sintaksisi
10/08/2021
"""


ismlar = ['Sobirjon', 'Habibullo', 'Jahongir', 'Anvarjon', 'Baxtiyor', 'Mahmudjon']

for salom in ismlar:
    print('Assalomu alaykum,',salom, '!') # Vergul bilan yozilganda avtomatik joy tashlaydi.

print(17/4)
print(17//4)

suzlar = ['bugun', 'havo', 'biroz', 'issiq', "bo'lishiga", "qaramay", "kunim", "mazmunli", "o'tdi"]

gap = ""

for suz in suzlar:
    if suz == suzlar[0]:
        gap = gap + suz.capitalize() + " "
    else:
        gap = gap + suz + " "
print(gap + "!")
