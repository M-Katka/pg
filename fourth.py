
def je_tah_mozny(figurka, cilova_pozice, obsazene_pozice):
 
    
    aktualni_pozice = figurka["pozice"]
    typ_figury = figurka["typ"]

    r1, s1 = aktualni_pozice
    r2, s2 = cilova_pozice

    if not (1 <= r2 <= 8 and 1 <= s2 <= 8):
        return False

    if cilova_pozice in obsazene_pozice:
        return False

    if typ_figury == "pěšec":
        if s1 != s2:
            return False
        if r2 == r1 + 1:
            return True
        return False

    elif typ_figury == "jezdec":
        dr = abs(r2 - r1)
        ds = abs(s2 - s1)
        if (dr == 2 and ds == 1) or (dr == 1 and ds == 2):
            return True
        else:
            return False

    elif typ_figury == "král":
        dr = abs(r2 - r1)
        ds = abs(s2 - s1)
        if dr <= 1 and ds <= 1:
            return True
        else:
            return False

    elif typ_figury == "věž":
        if r1 != r2 and s1 != s2:
            return False

        if r1 != r2:
            krok = 1 if r2 > r1 else -1
            for r_mezi in range(r1 + krok, r2, krok):
                pozice_mezi = (r_mezi, s1)
                if pozice_mezi in obsazene_pozice:
                    return False
            return True

        if s1 != s2:
            krok = 1 if s2 > s1 else -1
            for s_mezi in range(s1 + krok, s2, krok):
                pozice_mezi = (r1, s_mezi)
                if pozice_mezi in obsazene_pozice:
                    return False
            return True

    elif typ_figury == "střelec":
        dr = abs(r2 - r1)
        ds = abs(s2 - s1)

        if dr != ds or dr == 0:
            return False

        krok_r = 1 if r2 > r1 else -1
        krok_s = 1 if s2 > s1 else -1

        r_mezi = r1 + krok_r
        s_mezi = s1 + krok_s

        while (r_mezi, s_mezi) != cilova_pozice:
            pozice_mezi = (r_mezi, s_mezi)
            if pozice_mezi in obsazene_pozice:
                return False
            r_mezi += krok_r
            s_mezi += krok_s
        
        return True

    elif typ_figury == "dáma":
        dr = abs(r2 - r1)
        ds = abs(s2 - s1)

        je_tah_veze = (r1 == r2) or (s1 == s2)
        je_tah_strelce = (dr == ds)

        if not (je_tah_veze or je_tah_strelce) or (dr == 0 and ds == 0):
            return False

        if je_tah_veze:
            if r1 != r2:
                krok = 1 if r2 > r1 else -1
                for r_mezi in range(r1 + krok, r2, krok):
                    if (r_mezi, s1) in obsazene_pozice:
                        return False
                return True
            if s1 != s2:
                krok = 1 if s2 > s1 else -1
                for s_mezi in range(s1 + krok, s2, krok):
                    if (r1, s_mezi) in obsazene_pozice:
                        return False
                return True

        if je_tah_strelce:
            krok_r = 1 if r2 > r1 else -1
            krok_s = 1 if s2 > s1 else -1
            
            r_mezi = r1 + krok_r
            s_mezi = s1 + krok_s

            while (r_mezi, s_mezi) != cilova_pozice:
                if (r_mezi, s_mezi) in obsazene_pozice:
                    return False
                r_mezi += krok_r
                s_mezi += krok_s
            
            return True

    return False


if __name__ == "__main__":
    pesec = {"typ": "pěšec", "pozice": (2, 2)}
    jezdec = {"typ": "jezdec", "pozice": (3, 3)}
    vez = {"typ": "věž", "pozice": (8, 8)}
    strelec = {"typ": "střelec", "pozice": (6, 3)}
    dama = {"typ": "dáma", "pozice": (8, 3)}
    kral = {"typ": "král", "pozice": (1, 4)}
    obsazene_pozice = {(2, 2), (8, 2), (3, 3), (5, 4), (8, 3), (8, 8), (6, 3), (1, 4)}

    print(je_tah_mozny(pesec, (3, 2), obsazene_pozice))
    print(je_tah_mozny(pesec, (4, 2), obsazene_pozice))
    print(je_tah_mozny(pesec, (1, 2), obsazene_pozice))

    print(je_tah_mozny(jezdec, (4, 4), obsazene_pozice))
    print(je_tah_mozny(jezdec, (5, 4), obsazene_pozice))
    print(je_tah_mozny(jezdec, (1, 2), obsazene_pozice))
    print(je_tah_mozny(jezdec, (9, 3), obsazene_pozice))

    print(je_tah_mozny(dama, (8, 1), obsazene_pozice))
    print(je_tah_mozny(dama, (1, 3), obsazene_pozice))
    print(je_tah_mozny(dama, (3, 8), obsazene_pozice))