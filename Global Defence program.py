aliens = 2
password = "ALIENS"
print("Quickly!Aliens are invading the plant.")
print("You need to activate the global defence platforms.")
print("Hope you know the password,for Earth's sake...")
print()
print("-----------------------------------")
print("    WELCOME TO THE  GLOBAL DEFENCE NETWORK    ")
print("----------------------------------------")
print()
guess = input("Please enter the password: ").upper()
while guess !=password:
    print()
    print("INCORRECT PASSWORD.")
    print()
    aliens = aliens**2
    print("There are",aliens,"aliens now on Earth.Try again!")

    if aliens > 7400000000:
        break
    print()
    print("Password hint: the things that are attacking us.")
    print()
    guess = input("Quickly!please enter the password:").upper()
if aliens > 74000000000:
    print("N000000000! The aliens have outnumbered us. All is lost.")
else:
    print("Hooray! we won the fight and the the world is saved!")
