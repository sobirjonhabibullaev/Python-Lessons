"""
21/08/2021
Dars - 8 | Ro'yhatlar bilan ishlash. O'zgarmas ro'yxatlar(Tuples) 
"""

cars = ['bmw', 'volvo', 'mercedes benz', 'general motors', 'audi', 'tesla']
cars_reversed = cars[:]
cars_sorted = cars[:]
#sort() metodi - ro'yxatni tartiblab qo'yadi. (*, key: None = ..., reverse: bool = ...) -> None
#sort() metodidan foydalanilganda, agar ro'yxatdan bosh harf bilan bilan boshlanadigan biror element bo'lsa, birinchi shu elementni ko'rsatadi
cars.sort()
print(cars)

#sort(reverse=True) - teskari tartib 
cars_reversed.sort(reverse = True)
print(cars_reversed)

#sorted() funksiyasi asl ro'yxatni o'zgartirmay chiqaradi.
print(sorted(cars_sorted))

#reverse() metodi ro'yxatni teskari ko'rinishda, ya'ni ortdan bosshlab chiqaradi, tartiblamaydi.
fruits = ['banana', 'pineapple', 'kiwi', 'orange', 'mandarin']
fruits.reverse()
print(fruits)

# # RO'YXAT UZUNLIGI
print("Elementlar soni: {}".format(len(fruits)))

# # RANGE()
sonlar = list(range(0,10))
print(sonlar)

# RANGE VA QADAM 
juft_sonlar = list(range(0,20,2)) # 0 dan 20 gacha 2 qadam tashlaydi
toq_sonlar = list(range(1,20,2)) # 1 dan 20 gacha 2 qadam tashlaydi
print("Juft sonlar: ", juft_sonlar)
print("Toq sonlar: ", toq_sonlar)

# MIN(), MAX(), SUM()
narxlar = [12000, 34500, 62100, 56200, 17800]
arzon = min(narxlar)
qimmat = max(narxlar)
jami = sum(narxlar)
print("Eng arzon narx: {}, eng qimmat narx: {}, jami summa: {}".format(arzon, qimmat, jami))

# # RO'YXATNI KESISH (SLICING)
cars = ['bmw', 'volvo', 'mercedes benz', 'general motors', 'audi', 'tesla']
my_cars = cars[0:4] # 4 kirmaydi
print(cars[2:5])
print(cars[:4]) # = print(cars[0:4])
print(cars[4:]) # = print(cars[4:len(cars)])
# my_cars = cars bu bitta o'zgaruvchan ro'yxatga 2ta nom berish bo'ladi
# my_cars = cars[:] ro'yxatni o'zlashtirish uchun ishlatiladi

# # TUPLES - O'ZGARMAS RO'YXATLAR
toys = ('bus', 'car', 'bear', 'lego', 'dino', 'farm', 'soliders')
print(toys[:])
print(toys[0])
print(toys[-1])
print(toys[2:5])
# toys[2] = 'teddy' ishlamaydi
# append(), remove() metodlari ishlamaydi
# Agar o'zgartirmoqchi bo'lsak, avvalo listga o'tgazib olish kerak
toys = list(toys)
toys[2] = 'teddy'
print(type(toys))
# Keyin yana tuple ga o'zgartiriladi
toys = tuple(toys)
print(type(toys))
print(toys)
