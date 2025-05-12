while True:
    try:
        grade = int(input("Geben Sie eine Note ein: "))
        if grade in (1, 2, 3, 4, 5, 6):
            if grade == 1:
                print("Sehr gut")
            elif grade == 2:
                print("Gut")
            elif grade == 3:
                print("Befriedigend")
            elif grade == 4:
                print("Ausreichend")
            elif grade == 5:
                print("Mangelhaft")
            elif grade == 6:
                print("Ungenügend")
            break
        else:
            print("Geben Sie eine ganze Zahl zwischen 1 & 6 ein.")
    except:
        print("Geben Sie eine ganze Zahl zwischen 1 & 6 ein:")