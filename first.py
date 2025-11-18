# funkce zkontroluje, zda je funkce lichá nebo sudá
# a vypise:
# - "Cislo x je sude"
# - "Cislo x jem liché"

def sudy_nebo_lichy(cislo):
    if cislo % 2:
        print(f"Cislo {cislo} x je liche")
    else:
        print(f"Cislo {cislo} x je sude")

if __name__ == "__main__":
    sudy_nebo_lichy(5)
    sudy_nebo_lichy(1000000)

