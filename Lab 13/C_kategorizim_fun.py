def notat_ne_fjalë(n: float) -> str:
    if n < 0 or n > 10:
        return "Jashtë intervalit"
    elif n < 5:
        return "Dobët"
    elif n < 7:
        return "Mjaftueshëm"
    elif n < 9:
        return "Mire"
    else:
        return "Shkëlqyeshëm"

def eshte_abonuar(kodi: str) -> bool:
    return kodi.strip().upper() == "TIK12"

nota = float(input("Nota: "))
print(notat_ne_fjalë(nota))

kodi = input("Kodi: ")
print("Abonimi:", "Po" if eshte_abonuar(kodi) else "Jo")
