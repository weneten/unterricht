ip = str(input("Gebe die ersten 4 Bit einer IP-Adresse ein: "))

if ip.startswith("0"):
    print("Klasse A")
elif ip.startswith("10"):
    print("Klasse B")
elif ip.startswith("110"):
    print("Klasse C")
elif ip.startswith("1110"):
    print("Klasse D")
elif ip.startswith("1111"):
    print("Klasse E")
else:
    print("Falsche Eingabe!")