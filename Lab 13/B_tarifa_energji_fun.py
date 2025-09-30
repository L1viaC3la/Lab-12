def tarifa_energji(kwh: int) -> int:
    if kwh < 0:
        return -1
    taksa = 120
    if kwh <= 100:
        total = kwh * 8
    elif kwh <= 300:
        total = 100 * 8 + (kwh - 100) * 12
    else:
        total = 100 * 8 + 200 * 12 + (kwh - 300) * 15
    return total + taksa

kwh = int(input("kWh: "))
totali = tarifa_energji(kwh)
if totali == -1:
    print("E pavlefshme")
else:
    print(f"Totali: {totali}")
