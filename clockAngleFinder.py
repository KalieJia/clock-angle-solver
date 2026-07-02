from clock_logic import calculate_acute_angle


if __name__ == "__main__":
    hours = int(input("Enter hours: "))
    minutes = int(input("Enter minutes: "))
    print(f"The acute angle is {calculate_acute_angle(hours, minutes):.1f}°")
