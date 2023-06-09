
#ADAPTER

from math import sqrt

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

class Square:
    def __init__(self, side):
        self.side = side

    def get_side(self):
        return self.side

class CircleAdapter:
    def __init__(self, square):
        self.square = square

    def get_radius(self):
        diagonal = sqrt(2) * self.square.get_side()
        radius = diagonal / 2
        return radius


# Użycie adaptera
square = Square(8)  # Tworzenie obiektu kwadratu o boku równej 8
adapter = CircleAdapter(square)  # Tworzenie adaptera na podstawie kwadratu
circle = Circle(adapter.get_radius())  # Tworzenie obiektu okręgu na podstawie adaptera

print("Promień okręgu jest równy:", circle.get_radius())  # Wyświetlanie promienia okręgu

# singleton

class Singleton:
    _instance = None

    def __new__(cls):
        if not cls._instance: #sprawdzamy, czy już istnieje instancja
            cls._instance = super().__new__(cls)
        return cls._instance

# tworzymy dwie instancje klasy Singleton (obj1 i obj2) i sprawdzamy, czy są one tym samym obiektem, korzystając z operatora is
# Użycie wzorca Singleton
obj1 = Singleton()
obj2 = Singleton()

print(obj1 is obj2)  # True


#stos
def reverse_list(lst):
    stack = []
    for elem in lst:
        stack.append(elem)
    reversed_list = []
    while len(stack) > 0:
        reversed_list.append(stack.pop())
    return reversed_list

my_list = [10,11,12,13,14,15]
reversed_list = reverse_list(my_list)
print(reversed_list)


#Definiowanie klasy

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f"Hello, my name is {self.name} and I'm {self.age} years old.")

# Użycie klasy
person = Person("Gosia", 25)
person.say_hello()  # Hello, my name is Gosia and I'm 25 years old.

#Rekurencja

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

result = factorial(5)
print(result)  # Wyświetli: 120


#Dziel i zwyciężaj

def find_maximum(nums):
    if len(nums) == 1:
        return nums[0]

    mid = len(nums) // 2
    left_max = find_maximum(nums[:mid])
    right_max = find_maximum(nums[mid:])

    return max(left_max, right_max)

# Przykładowe użycie
numbers = [6, 9, 12, 7, 9, 2, 5]
max_number = find_maximum(numbers)
print("Największa liczba to:", max_number)



#Graf

from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            print(vertex)
            visited.add(vertex)
            queue.extend(graph[vertex])

# Przykładowy graf w postaci słownika
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Wywołanie funkcji BFS
bfs(graph, 'A')


#Kolejka

from queue import Queue

def find_smallest(arr):
    q = Queue()

    for elem in arr:
        q.put(elem)

    smallest = q.get()
    while not q.empty():
        elem = q.get()
        if elem < smallest:
            smallest = elem

    return smallest

arr = [4, 2, 7, 1, 9, 5]
smallest = find_smallest(arr)
print(smallest)