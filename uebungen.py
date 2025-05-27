from collections import namedtuple


# Zahlen prüfen, ob sie gerade bzw. ungerade sind
def even_uneven():
    n = int(input("Gebe eine Zahl ein: "))

    if n % 2 == 0:
        print("Die Zahl is gerade!")
    elif n % 2 == 1:
        print("Die Zahl ist ungerade!")


# Summe der Zahlen, die durch 3 oder 5 teilbar sind, berechnen
def sum_of():
    sum_of_numbers = 0
    for i in range(10, 101, 1):
        if i % 3 == 0 or i % 5 == 0:
            sum_of_numbers += i

    print("Die Summe ist: " + str(sum_of_numbers))


# Zahlen nach der Größe ordnen
def sorter():
    a, b, c = input("Gebe 3 Zahlen ein: ").split()

    if a <= b and a <= c:
        smallest = a
        if b <= c:
            middle = b
            biggest = c
        else:
            middle = c
            biggest = b
    elif b <= a and b <= c:
        smallest = b
        if a <= c:
            middle = a
            biggest = c
        else:
            middle = c
            biggest = a
    else:
        smallest = c
        if a <= b:
            middle = a
            biggest = b
        else:
            middle = b
            biggest = a

    print("Die Zahlen sortiert nach Größe sind:", smallest, "<=", middle, "<=", biggest)


# Zahl erraten Spiel
def guess_random_number():
    import random as rng

    print("\nWillkommen zum Ratespiel! Du musst eine Zahl zwischen 0 & 20 erraten!")
    rng_number = rng.randrange(0, 20)
    game_running = True

    def int_get_user_input():
        while True:
            user_input_number = input("\nGib eine Zahl zwischen 1 & 20 ein: ")
            try:
                user_input_number = int(user_input_number)
                if int(user_input_number) in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20):
                    return user_input_number
                else:
                    print("\nDu musst eine Zahl zwischen 1 & 20 eingeben.")
            except:
                print("\nDu musst eine Zahl zwischen 1 & 20 eingeben.")

    while game_running:
        try:
            if int(user_input_number) == rng_number:
                print("\nWOW! GG!")
                game_running = False
            elif int(user_input_number) > rng_number:
                print("\nDeine Zahl ist zu Groß! Probiere es nochmal")
                user_input_number = int_get_user_input()
            elif int(user_input_number) < rng_number:
                print("\nDeine Zahl ist zu klein! Probiere es nochmal")
                user_input_number = int_get_user_input()
        except:
            user_input_number = int_get_user_input()


# Collatz Folge
def collatz_sequence():
    number = int(input("Gebe eine Startzahl ein: "))
    count = 0

    while number > 1:

        if number % 2 == 0:
            number = number / 2
            print(number)
        elif number % 2 == 1:
            number = number * 3 + 1
            print(number)

        count += 1

        if number == 1:
            print(f"Beendet in {count} Operationen.")


# Fibonacci Folge
def fibonacci_sequence():
    a = 0
    b = 1
    input_correct = False

    while not input_correct:
        user_number = input("Gebe eine Zahl zwischen 3 & 20 ein: ")
        try:
            user_number = int(user_number)
            if 3 <= user_number <= 20:
                input_correct = True
            else:
                print("\nUngültige Zahl! Die Zahl muss zwischen 3 & 20 sein.\n")
        except ValueError:
            print("\nEingabe ungültig! Es muss eine Zahl zwischen 3 & 20 sein.\n")

    for i in range(1, user_number):
        c = a + b  # 2 fib: c = 0 + 1       3 fib: c(2) = 1 + 1      4 fib: c(3) = 1 + 2
        a = b  # a = 1                  a = 1                    a = 2
        b = c  # b = 1                  b = 2                    b = 3

    print(f"\nDie {user_number}te Zahl der Fibonacci Folge ist: {b}")


# Fibonacci Folge mit 0 als Start
def fibonacci_sequence_with_error():
    a = 0
    b = 1
    user_number = input("Gebe eine Zahl zwischen 3 & 20 ein: ")

    try:
        user_number = int(user_number)
        if user_number == 1:
            print(f"\nDie {user_number}te Zahl der Fibonacci Folge ist: 0")
        elif user_number == 2:
            print(f"\nDie {user_number}te Zahl der Fibonacci Folge ist: 1")
        elif 3 <= user_number <= 20:
            for i in range(1, user_number - 1):
                c = a + b  # 2 fib: c = 0 + 1       3 fib: c(2) = 1 + 1      4 fib: c(3) = 1 + 2
                a = b  # a = 1                  a = 1                    a = 2
                b = c  # b = 1                  b = 2                    b = 3
            print(f"\nDie {user_number}te Zahl der Fibonacci Folge ist: {b}")
        else:
            print("\nUngültige Zahl! Die Zahl muss zwischen 3 & 20 sein.\n")
    except ValueError:
        print("\nEingabe ungültig! Es muss eine Zahl zwischen 3 & 20 sein.\n")


# fibonacci tabelle
def fibonacci_with_tables():
    number = int(input("Bis zu welcher Zahl möchtest du die Fibonacci-Reihe ausrechnen (max 30)? "))
    for i in range(number + 1):
        a = 0
        b = 1
        if i == 1:
            print(f" {i:2} | {0:6d}")
        elif i == 2:
            print(f" {i:2} | {1:6d}")
        elif 3 <= i <= 30:
            for i in range(1, i - 1):
                c = a + b  # 2 fib: c = 0 + 1       3 fib: c(2) = 1 + 1      4 fib: c(3) = 1 + 2
                a = b  # a = 1                  a = 1                    a = 2
                b = c  # b = 1                  b = 2                    b = 3
            print(f" {i + 2:2} | {b:6d}")


# fibonacci_with_tables()


# zahlen nach größe ordnen
def sorter_new():
    user_numbers = input("Gebe mindestens 2 Zahlen ein: ").split()
    user_numbers_int = list(map(int, user_numbers))
    user_numbers_int.sort()
    print(str(user_numbers_int).strip("[]"))


def useless_min_max():
    user_numbers = input("Gebe eine beliebige Anzahl an Zahlen ein: ").split()
    user_numbers_int = list(map(int, user_numbers))
    minimum = user_numbers_int[0]
    maximum = user_numbers_int[0]
    i = 1

    while i < len(user_numbers_int):
        if user_numbers_int[i] < minimum:
            minimum = user_numbers_int[i]
        elif user_numbers_int[i] > maximum:
            maximum = user_numbers_int[i]
        i += 1
    print(minimum, maximum)


# useless_min_max()


def new_min_max_avg(user_numbers):
    first = float(user_numbers[0])
    min = max = first
    sum = count = 0
    for i in user_numbers:
        i = float(i)
        count += 1
        sum += i
        if i > min:
            max = i
        elif i < max:
            min = i
    avg = sum / count
    print(f"{min}, {max}, {avg:.2f}")


# new_min_max_avg(input("Gebe mehrere Zahlen ein: ").split())


def greet(name: str):
    print(f"Hello {name}!")


# greet(input("Wie heißt du? "))


def calc(a: float, b: float, factor: int):
    end = (a + b) * factor
    print(end)


# calc(a = 1, b = 3.5, factor = 2)

def make_upper(string: str):
    while string == "":
        print("Du musst etwas eingeben!")
        string = input("Gebe einen beliebigen Text ein den du in Großbuchstaben haben möchtest: ")
    print(string.upper())


# make_upper(input("Gebe einen beliebigen Text ein, den du in Großbuchstaben haben möchtest: "))


def wiederhole_name(name: str, repeat: int) -> str:
    return name * repeat


def summe(a: float, b: float) -> (float):
    return a + b


def multiplicationByTwo():
    n = 1
    for i in range(10):
        endTuple = (i + 1, n)
        n *= 2
        print(endTuple)


# multiplicationByTwo()


def multiplicationByTwoWithNamedTuples():
    n = 1
    endNumbers = namedtuple("Tuple", ["Index", "Number"])
    for i in range(10):
        t = endNumbers(i + 1, n)
        n *= 2
        print(t)

# multiplicationByTwoWithNamedTuples()



def namesSetFix():
    names1 = ["tom", "Jürgen", "ANNA", "max"]
    names2 = ["Tom", "  max ", "anna", "peter"]

    fixedNames1 = {names.strip().lower().capitalize() for names in names1}
    fixedNames2 = {names.strip().lower().capitalize() for names in names2}
    
    print("Duplicates: " + str(sorted(fixedNames1 & fixedNames2)).strip("[]").replace("'", ""))
    print("All names: " + str(sorted(fixedNames1 | fixedNames2)).strip("[]").replace("'", ""))


namesSetFix()