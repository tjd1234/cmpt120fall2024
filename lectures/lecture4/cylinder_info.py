# cylinder_info.py

radius = input("Cylinder's radius? ")
radius = float(radius)
height = input("Cylinder's height? ")
height = float(height)

volume = height * (3.14 * radius ** 2)
print('Volume:', volume)

surface_area = height * (2 * 3.14 * radius) + 2 * (3.14 * radius * radius)
print('Surface area:', surface_area)
