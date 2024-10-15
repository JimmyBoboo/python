#import math
from math import log

def hunderalder_til_menneskealder(hunderalder):
    menneskealder = 16 * log(hunderalder) + 31
    return menneskealder

print(hunderalder_til_menneskealder (20))
menneskes_alder = hunderalder_til_menneskealder(10)
print(menneskes_alder)

def inkluder_moms(pris, moms=0.25):
    pris_med_moms = pris + pris*moms
    return pris_med_moms

pris_uten_moms = 100
print(inkluder_moms(100))
print(inkluder_moms(pris_uten_moms))
