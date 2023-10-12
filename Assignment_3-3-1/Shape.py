import math

class Shape:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    @classmethod
    def create_shape(cls):
        radius = float(input("Enter the radius of the circle: "))
        return cls(radius)

class Sphere(Shape):
    def __init__(self, radius):
        super().__init__(radius)

    def area(self):
        return 4 * math.pi * self.radius**2

    def volume(self):
        return (4/3) * math.pi * self.radius**3

    @classmethod
    def create_shape(cls):
        radius = float(input("Enter the radius of the sphere: "))
        return cls(radius)

def main():
    shape_type = input("Enter the type of shape (2D or 3D): ").lower()

    if shape_type == "2d":
        circle = Shape.create_shape()
        area = circle.area()
        print(f"Area of the circle: {area}")
    elif shape_type == "3d":
        sphere = Sphere.create_shape()
        area = sphere.area()
        volume = sphere.volume()
        print(f"Surface area of the sphere: {area}")
        print(f"Volume of the sphere: {volume}")
    else:
        print("Invalid input. Please enter '2D' or '3D.")

if __name__ == "__main__":
    main()
