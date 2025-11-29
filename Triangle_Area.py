#Calculate Area of Triangle when all sides of triangle are given

def area_triangle():
    a = int(input("Enter a side 1: "))
    b = int(input("Enter a side 2: "))
    c = int(input("Enter a side 3: "))

    if a+b>c and a+c>b and b+c>a:
        s = (a + b + c) /2
        z = (s * (s - a) * (s - b) * (s - c))
        area = z ** 0.5
        print(s)
        print(z)
        print("The area of the triangle is:", area)
    else:
        print("invalid")
area_triangle()