"""
20/08/2021
Dars - 7 | Lists 
"""
mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]
print("{}\n{}\n{}".format(mevalar, type(mevalar), len(mevalar)))

print(mevalar[-1].title())
"""
>>>"they're bill's friends from the UK".title()
"They'Re Bill'S Friends From The Uk"
! A workaroun for apostrophes can be constructed using regular expressions:
>>> import re
>>> def titlecase(s):
...   return re.sub(r"[A-Za-z]+('[A-Za-z]+)?",
...                 lambda mo: mo.group(0).capitalize(),
...                 s)
...
>>> titlecase("they're bill's friends from the UK")
"They're Bill's Friends From The UK"
! Bosh harfdan tarkib topgan so'zning qolgan harflari kichik bo'lib qolayabdi. Sababi noma'lum....
"""

print("they're bill's friends from the UK".title())
import re
def titlecase(s):
    return re.sub(r"[A-Za-z]+('[A-Za-z]+)?",lambda mo: mo.group(0).capitalize(),s)


print(titlecase("they're bill's friends from the UK"))

mevalar.append("nok") #append() metodi ro'yxatning oxiriga qo'shiladi

mevalar.insert(2, 'gilos') #insert() metodi istalgan o'ringa elemntni qo'sha oladi

#!!! Maslahat: -Ro'yhat nomi ko'plikda bo'lsin

del mevalar[1] # del ma'lum bir elementni o'chirib yuborish uchun foydalaniladi.

mevalar.remove("o'rik") #ro'yxatdagi elementning indexi noma'lum bo'lsa foydalansa bo'ladi
#remove() metodi agar ro'yxatda birnechta bir xil element bo'lsa birinchisini o'chirib yuboradi

meva = mevalar.pop(3) #ro'yxatdagi indexi 3 bo'lgan elementni ajratib oladi.
#agar hech qanday index berilmasa ro'yxatdagi oxirgi elemntni ajratib oladi.
