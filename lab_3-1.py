# Author: JD 09/29/2021

point = input("Point: ")
points = int(point)
if points >= 15:
    print("This team wins a gold medal.")
else:
    if points >= 12:
        print("This team wins a silver medal.")
    else:
        if points >= 9:
            print("This team wins a bronze medal.")
        else:
            print("This team wins nothing.")