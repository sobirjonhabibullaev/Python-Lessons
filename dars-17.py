talabalar = ['ali', 'vali', 'hasan', 'husan']
baholangan_talabalar = {}

while talabalar:  # agar talabalar ro'yxatida 1tagina bo'lsa ham element bo'lsa, True qabul qiladi.
    talaba = talabalar.pop()
    baho = input(f"{talaba.capitalize()}ning bahosini kiriting: ")
    baholangan_talabalar[talaba] = int(baho)

for t, b in baholangan_talabalar.items():
    print(f"{t.capitalize()}ning bahosi - {b}.")