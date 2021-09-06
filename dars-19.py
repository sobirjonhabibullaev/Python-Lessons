"""
19-DARS | FUNCTIONS
25/08/2021
"""

# def toliq_ism_yasa(ism, familiya):
#     toliq_ism = f"{ism} {familiya}"
#     return toliq_ism

# print(toliq_ism_yasa("Sobirjon", "Habibullaev"))


def toliq_ism_yasa(ism, familiya, otasining_ismi=''):
    if otasining_ismi:
        toliq_ism = f"{ism} {familiya} {otasining_ismi} o'g'li"
    else:
        toliq_ism = f"{ism} {familiya}"
    return toliq_ism


print(toliq_ism_yasa("Sobirjon", "Habibullaev"))
print(toliq_ism_yasa("Sobirjon", "Habibullaev", "Ziyodullo"))

