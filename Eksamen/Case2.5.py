from datetime import date
def next_eu_control(year_lagd, maned_lagd):
    naa_dagens_dato = date.today()
    naa_dagens_aar = naa_dagens_dato.year
    naa_dagens_maned = naa_dagens_dato.month
    
    year_differanse = (naa_dagens_aar - year_lagd) // 2
    sist_EU_kontroll = year_lagd + (year_differanse * 2)
    
    if (naa_dagens_aar > sist_EU_kontroll or (naa_dagens_aar == sist_EU_kontroll and naa_dagens_maned >= maned_lagd)):
        neste_EU_sjekk = sist_EU_kontroll + 2
    
    else:
        neste_EU_sjekk = sist_EU_kontroll
    
    return date(neste_EU_sjekk, maned_lagd, 1)

neste_kontroll_sjekk = next_eu_control(2020, 6)
print(f"Neste EU kontroll er: {neste_kontroll_sjekk}")