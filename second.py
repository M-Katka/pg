def cislo_text(cislo):
 
    jednotky = {
        0: "nula", 1: "jedna", 2: "dva", 3: "tři", 4: "čtyři", 5: "pět", 6: "šest", 7: "sedm", 8: "osm", 9: "devět"
    }
 
    teen = {
        11: "jedenáct", 12: "dvanáct", 13: "třináct", 14: "čtrnáct", 15: "patnáct", 16: "šestnáct", 17: "sedmnáct", 18: "osmnáct", 19: "devatenáct"
    }
 
    desitky_plne = {
        10: "deset", 20: "dvacet", 30: "třicet", 40: "čtyřicet", 50: "padesát", 60: "šedesát", 70: "sedmdesát", 80: "osmdesát", 90: "devadesát"
    }

    if 0 <= cislo < 10:
        return jednotky[cislo]
 
    if cislo == 10:
        return desitky_plne[cislo]
 
    if 10 < cislo < 20:
        return teen[cislo]
 
    if cislo == 100:
        return "sto"
 
    if 20 <= cislo < 100:
        desitka_hodnota = (cislo // 10) * 10
        jednotka_hodnota = cislo % 10 
 
        if jednotka_hodnota == 0:
            return desitky_plne[desitka_hodnota]
        else:
            return f"{desitky_plne[desitka_hodnota]} {jednotky[jednotka_hodnota]}"
    
 
    return "Číslo musí být celé a mezi 0 a 100"


if __name__ == "__main__":
    
    zadany_text = input("Zadej celé číslo od 0 do 100: ")
    cislo_k_prevodu = int(zadany_text)
    text = cislo_text(cislo_k_prevodu)
    
    print(text)