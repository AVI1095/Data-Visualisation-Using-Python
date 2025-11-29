#Celsius to fahrenheit

def temp():
    while True:
        try:
            cel = int(input("Enter the temperature in Celsius: "))
        except ValueError:
            print("Invalid input")
            continue

        break
    fah = cel * 1.8 + 32
    print("Temperature in Fahrenheit: ", fah)

temp()

