def dec_to_bin(cislo):
   
    try:
        dekadicke_cislo = int(cislo)
    except ValueError:
        return "Chyba"

    if dekadicke_cislo == 0:
        return "0"

    binarni_vysledek = ""
    aktualni_cislo = dekadicke_cislo

    while aktualni_cislo > 0:
        zbytek = aktualni_cislo % 2  
        binarni_vysledek = str(zbytek) + binarni_vysledek 
        aktualni_cislo = aktualni_cislo // 2    

    return binarni_vysledek


def test_bin_to_dec():
    assert dec_to_bin("0") == "0"
    assert dec_to_bin(1) == "1"
    assert dec_to_bin("100") == "1100100"
    assert dec_to_bin(101) == "1100101"
    assert dec_to_bin(127) == "1111111"
    assert dec_to_bin("128") == "10000000"