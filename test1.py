digit = [1,2,3,4,5,6]
print(min(digit))
print(max(digit))
print(sum(digit))
print(digit)

squares = [value**2 for value in range(1,11)]
print(squares)

def tekshir(son,num):
    if son == num:
        return 1
    else:
        print("Kattaroq son kiriting", end=". ")
        return 0

while True:
    son = int(input("Son kiriting: "))
    if tekshir(son, 3) == 1:
        break