radius = int(input("Enter the radius of the circle: "))

pi = 3.14

def circumference(radius):

    circumference = 2 * pi * radius

    return circumference

print("The circumference of the circle is:", circumference(radius))