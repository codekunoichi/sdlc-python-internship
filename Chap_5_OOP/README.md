# Object-Oriented Programming (30 minutes):

- Introduction to classes and objects.
- Defining classes and creating objects.
- Class attributes and instance methods.
- Inheritance and method overriding.

Object-oriented programming (OOP) is a programming paradigm that revolves around organizing code into reusable and self-contained units called objects. These objects represent real-world entities or concepts and have their own characteristics (attributes) and behaviors (methods). Let's discuss four key principles of OOP:

1. Encapsulation: Imagine a box that holds different items. Encapsulation is like putting related things in that box. In OOP, encapsulation means bundling data (attributes) and the operations that manipulate that data (methods) together within an object. It helps to keep related code and data together, making it easier to manage and understand.

2. Inheritance: Imagine a family with a parent and their children. Inheritance is like passing down certain traits or characteristics from parents to children. In OOP, inheritance allows objects (child classes) to inherit properties and behaviors from other objects (parent classes). It promotes code reuse and helps in creating specialized objects based on more general ones.

3. Polymorphism: Imagine different shapes, such as a circle, square, and triangle. Polymorphism is like the ability of each shape to be used interchangeably. In OOP, polymorphism refers to the ability of objects of different types (classes) to be used and treated in a consistent way. It allows different objects to have their own specific implementations of methods while still adhering to a common interface.

4. Abstraction: Imagine a remote control with buttons but no knowledge of how it works internally. Abstraction is like focusing on the essential details while hiding unnecessary complexity. In OOP, abstraction allows us to create simplified models of real-world objects, focusing only on the necessary attributes and behaviors. It helps in managing complexity and allows us to work with objects without needing to know all the underlying details.

By understanding and applying these principles, object-oriented programming provides a way to structure code and design software in a modular, reusable, and understandable manner. It encourages the creation of objects that mimic real-world entities, making it easier to write and maintain complex software systems.

## Classes and Objects

In object-oriented programming (OOP), a class is a blueprint or a template for creating objects. It defines the structure and behavior that objects of that class will have. It serves as a blueprint because it specifies the attributes (data) and methods (functions) that the objects created from the class will possess. 

A class encapsulates related data and functions into a single entity. It defines the properties and behaviors that the objects will exhibit. Think of a class as a blueprint for constructing objects, describing their common characteristics and behaviors.

On the other hand, an object is an instance of a class. When you create an object, you are creating a specific, unique entity based on the class blueprint. It represents a particular occurrence or realization of the class. An object has its own unique state and can interact with other objects.

To put it simply, a class is like a blueprint or a plan, while an object is an actual realization or manifestation of that blueprint. The class describes what an object will be like, and the object is the specific instance that exists and can interact with other objects or the system.

For example, consider a class called "Car." The class definition would include attributes like color, make, and model, as well as methods like start(), stop(), and accelerate(). When you create an object of the "Car" class, such as "my_car = Car()", you have an actual car instance with specific values for the attributes and the ability to perform actions using the defined methods.

In summary, a class is a blueprint that defines the structure and behavior of objects, while an object is an instance or a specific realization of that class with its own unique state and behavior.

## Example Illustration for Inheritance, Encapsulation, Abstraction, Polymorphism

Here's an example Python code snippet that demonstrates the principles of inheritance, polymorphism, abstraction, and encapsulation using the classic shape example:

```
from abc import ABC, abstractmethod

# Abstract class representing a shape
class Shape(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate_area(self):
        pass

# Concrete class representing a circle
class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def calculate_area(self):
        return 3.14 * self.radius * self.radius

# Concrete class representing a triangle
class Triangle(Shape):
    def __init__(self, name, base, height):
        super().__init__(name)
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height

# Concrete class representing a square
class Square(Shape):
    def __init__(self, name, side):
        super().__init__(name)
        self.side = side

    def calculate_area(self):
        return self.side * self.side


# Usage example
shapes = [
    Circle("Circle 1", 5),
    Triangle("Triangle 1", 4, 6),
    Square("Square 1", 7)
]

for shape in shapes:
    print(f"Name: {shape.name}")
    print(f"Area: {shape.calculate_area()}")
    print("-------------------")
```

Explanation:

1. Inheritance: The `Circle`, `Triangle`, and `Square` classes inherit from the abstract class `Shape`. They inherit the `name` attribute and the `calculate_area()` method defined in the `Shape` class.

2. Polymorphism: The `shapes` list contains objects of different types (`Circle`, `Triangle`, `Square`). The `calculate_area()` method is polymorphic because each subclass provides its own implementation, specific to its shape.

3. Abstraction: The `Shape` class is an abstract class defined using the `ABC` module and the `@abstractmethod` decorator. It contains the `name` attribute and the abstract method `calculate_area()`. The abstract method enforces that all subclasses must implement the `calculate_area()` method.

4. Encapsulation: Each shape class encapsulates its specific data (`radius`, `base`, `height`, `side`) within its own class. The data is accessed and manipulated through the class's methods (`__init__` and `calculate_area()`), ensuring that the internal details are encapsulated and hidden from external code.

The example demonstrates how inheritance allows the subclasses to inherit attributes and methods from the abstract class, how polymorphism enables calling the same method on different shapes, how abstraction defines a common interface for shape objects, and how encapsulation keeps the data and methods within each class separate and controlled.
