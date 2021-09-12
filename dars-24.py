import random as r

sonlar = r.sample(range(100),10)
print(sonlar)

def juftmi(x):
    return x % 2 == 0 #boolean javob qaytaradi

# juft_sonlar = list(filter(juftmi,sonlar))
# print(juft_sonlar)

juft_sonlar = list(filter(lambda x: x % 2 == 0, sonlar))
print(juft_sonlar)


mevalar = ['olma', 'anjir', 'behi', 'shaftoli', 'olcha', 'nok', 'uzum', 'anor', 'bodom']
harf = 'b'
mevalar_b = list(filter(lambda meva: meva.startswith(harf), mevalar))
print(mevalar_b)

mevalar2 = list(filter(lambda meva: len(meva)<5, mevalar))
print(mevalar2)
