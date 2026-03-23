from datetime import date

def age_calculator(year, month, day):
    today = date.today()
    birth = date(year, month, day)

    age = (
        today.year
        - birth.year
        - ((today.month, today.day)
        < (birth.month, birth.day))
    )

    return age

if __name__ == "__main__":
    try:
        year = int(input("Enter your birth year: "))
        month = int(input("Enter your birth month: "))
        day = int(input("Enter your birth date: "))

        age = age_calculator(year, month, day)

        print(f"Your age is: {age}")

    except ValueError:
        print("Invalid date entered!")