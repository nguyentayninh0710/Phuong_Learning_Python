'''
cenario

A transportation company manages different types of vehicles:

Vehicle (parent class): has plateNumber, capacity.

Car (subclass): inherits from Vehicle, adds fuelType.

Bus (subclass): inherits from Vehicle, adds routeNumber.

The system must:

Create a list of Car and Bus objects.

Write a linear search to find a Bus by its routeNumber.

Write a selection sort to sort the list of Car by capacity.

Write a filtering function to return all Car objects with fuelType = "Electric".

Expected Output

cars = [
    Car("51A-12345", 4, "Petrol"),
    Car("51B-22222", 4, "Electric"),
    Car("51C-33333", 7, "Diesel"),
    Car("51D-44444", 5, "Electric")
]

buses = [
    Bus("79A-11111", 30, "R01"),
    Bus("79B-22222", 45, "R02"),
    Bus("79C-33333", 40, "R03")
]

== Linear Search Bus ==
Bus 79B-22222, capacity 45, route R02

== Selection Sort Cars by Capacity ==
Car 51A-12345, capacity 4, fuel: Petrol
Car 51B-22222, capacity 4, fuel: Electric
Car 51D-44444, capacity 5, fuel: Electric
Car 51C-33333, capacity 7, fuel: Diesel

== Filter Electric Cars ==
Car 51B-22222, capacity 4, fuel: Electric
Car 51D-44444, capacity 5, fuel: Electric
'''