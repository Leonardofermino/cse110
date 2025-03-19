import math

side = float(input("What is the length of a side of the square? "))

area_square = side ** 2

print(f"The area of the square is: {area_square:.1f}")


# What is the length of rectangle? 6
length = float(input("\nWhat is the length of rectangle? "))
# What is the width of the rectangle? 7
width = float(input("What is the width of the rectangle? "))

area_rectangle = length * width

# The area of the rectangle is: 42.0
print(f"The area of the rectangle is: {area_rectangle:.1f}")

# What is the radius of the circle? 5
radius = float(input("\nWhat is the radius of the circle? "))

area_circle = math.pi * (radius ** 2)
# The area of the circle is: 78.5
print(f"The area of the circle is: {area_circle:.1f}")

# Prompt the user for a single length value, then compute and display the areas of a square with that length of side, a circle with that radius, and then the volumes of a cube with that side and a sphere with that radius, all from the same value from the user.

value = float(input("\nWhat is the value to be used ? "))

area_square = value ** 2
area_circle = math.pi * (value ** 2)
volume_cube = value ** 3
volume_sphere = (4/3) * math.pi * (value ** 3)

print(f"\nThe area of the square is: {area_square:.1f}")
print(f"The area of the circle is: {area_circle:.1f}")
print(f"The volume of the cube is: {volume_cube:.1f}")
print(f"The volume of the sphere is: {volume_sphere:.1f}")

side = float(input("\nWhat is the length of a side of the square (in cm)? "))
area = side ** 2

print(f"The area of the square is: {area} cm^2")
print(f"The area of the square is: {area / 10000} m^2")

# Area of a rectangle
length = float(input("\nWhat is the length of rectangle (in cm)? "))
width = float(input("What is the width of the rectangle (in cm)? "))
area = length * width
print(f"\nThe area of the rectangle is: {area} cm^2")
print(f"The area of the rectangle is: {area / 10000} m^2")

# Area of a circle
radius = float(input("\nWhat is the radius of the circle (in cm)? "))
area = 3.14 * (radius ** 2)
print(f"\nThe area of the circle is: {area} cm^2")
print(f"The area of the circle is: {area / 10000} m^2")

