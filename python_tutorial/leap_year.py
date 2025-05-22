# A leap is a year that is divisible by 4
def leapyear(year):
    if (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False
def main():
        year = int(input("Enter a year:"))
        if leapyear(year):
            print(f"It is a leap year: {year}")
        else:
            print(f"It is not a leap year: {year}")
if __name__ == "__main__":
    main()