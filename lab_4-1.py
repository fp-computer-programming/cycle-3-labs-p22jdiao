# Author: JD 09/30/2021

magic_charge = int(input("Magic charge: "))

shield_charge = int(input("Shield charge: "))

if (magic_charge < 90) or (shield_charge < 75):
    print("The dragon burns you to a crisp.")
else:
    print("You defeated the dragon! But the princess is in another castle.")