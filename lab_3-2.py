# Author: JD 09/29/2021

point = int(input("Point: "))

if point >= 15:
    print("This team wins a gold medal.")
elif point >= 12:
    print("This team wins a silver medal.")
elif point >= 9:
    print("This team wins a bronze medal.")
else:
    print("This team wins nothing.")