def format_lek(vlera: float) -> str:
    return f"{vlera:,.2f} Lek"

shuma = float(input("Shuma: "))
print(format_lek(shuma))
