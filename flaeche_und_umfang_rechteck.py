falsche_eingabe = True

while falsche_eingabe:
    a = input("Gebe eine Zahl a für die Länge eines Rechtecks ein: ")
    b = input("Gebe eine Zahl b für die Breite eines Rechtecks ein: ")
    try:
        a = float(a)
        b = float(b)
        falsche_eingabe = False
    except ValueError:
        print("Die Eingaben dürfen nur Zahlen mit oder ohne Nachkommastellen sein.")

flaeche = a * b
umfang = 2 * a + 2 * b

print(f"Die Fläche des Rechtecks beträgt {flaeche:.2f} und die Breite beträgt {umfang:.2f}.")


# a = float(input("a: "))
# b = float(input("b: "))
#
# flaeche = a * b
# umfang = 2 * a + 2 * b
#
# print(f"Die Fläche des Rechtecks beträgt {flaeche} und die Breite beträgt {umfang}.")
