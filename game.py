import random as rng

print("\nWillkommen zum Ratespiel! Du musst eine Zahl zwischen 0 und 20 erraten!")
rng_number = rng.randrange(0, 20)
game_running = True


def int_get_user_input():
    user_input_number = input("\nGib eine Zahl zwischen 1 & 20 ein: ")
    try:
        if int(user_input_number) in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20):
            return user_input_number
        else:
            int_get_user_input()
    except:
        int_get_user_input()


user_input_number = input("\nGib eine Zahl zwischen 1 & 20 ein: ")

# gameloop
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
