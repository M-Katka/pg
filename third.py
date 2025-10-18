def je_prvocislo(cislo):
   
    if cislo < 2:
        return False
    
    limit = int(cislo**0.5) + 1

    for delitel in range(2, limit):
        if cislo % delitel == 0:
            return False

    return True

def vrat_prvocisla(maximum):
    
    seznam_prvocisel = []
    
    for cislo_k_testu in range(2, maximum + 1):
        if je_prvocislo(cislo_k_testu):
            seznam_prvocisel.append(cislo_k_testu)
            
    return seznam_prvocisel

if __name__ == "__main__":
    cislo_text = input("Zadej maximum: ")
    maximum_cislo = int(cislo_text)
    
    prvocisla = vrat_prvocisla(maximum_cislo)
    
    print("Prvočísla od 1 do", maximum_cislo, "jsou:")
    print(prvocisla)