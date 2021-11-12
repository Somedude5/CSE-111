#The MPG Program

import math

def main():
    miles = float(input("Enter the first odometer mileage: "))

    end_miles =float(input("Enter the second odometer mileage: "))

    gallons = float(input("Enter the amount of fuel expended(Gal): "))

    mpg = miles_per_gallon(miles, end_miles, gallons)

    Liters_per_100k = Lper100k(mpg)

    print(f"{mpg:.1f} miles per gallon")
    print(f"{Liters_per_100k:.2f} liters per 100 kilometers")


def miles_per_gallon(miles, end_miles, gallons):
    mpg = abs((miles - end_miles) / gallons)
    return mpg  

def Lper100k (mpg):
    Liters_per_100k = 235.215 / mpg
    return Liters_per_100k

main()