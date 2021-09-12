"""
DARS-23 | Modullar
2/09/2021
"""

mening_savatcham = {}

def savatchaga_qosh(**buyum):
    
    return buyum

print(savatchaga_qosh(olma=2000)) 

def toliq_ism_yasa(ism, familiya, otasining_ismi=''):
    if otasining_ismi:
        toliq_ism = f"{ism} {familiya} {otasining_ismi} o'g'li"
    else:
        toliq_ism = f"{ism} {familiya}"
    return toliq_ism