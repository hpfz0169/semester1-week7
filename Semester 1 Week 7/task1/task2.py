class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __str__(self):
        return f"{self.x}, {self.y}"
    
point1 = Point(10, 5)
point2 = Point(4, 2)

print(point1)
print(point2)
print(point1+point2)

# Given a Point class, define the __str__ and __add__ methods
# Test your code by defining 2 Point objects
# Print the Points and the sum of the 2 Points 
