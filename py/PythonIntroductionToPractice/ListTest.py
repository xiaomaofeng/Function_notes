motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)
poped_motocycle = motorcycles.pop()
print(motorcycles)
print(poped_motocycle)
motorcycles_1 = ['honda','yamaha','suzuki']
first_owned = motorcycles_1.pop(0)
print('The first motorcycle I owned was a' + first_owned.title() +'.')
motorcycles_1.remove('suzuki')
#-------------------
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)
#------------------
cars_1 = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list :")
print(cars_1)
print("\nHere is the sorted list:")
print(sorted(cars_1))
print("\n Here is the original list again: ")
print(cars_1)
cars_1.reverse()
print(cars_1)
print(len(cars_1))
#--------------------------
even_numbers = list(range(2,11,2))
print(even_numbers)
print(min(even_numbers))
print(max(even_numbers))
print(sum(even_numbers))
squares = [value**2 for value in range(1,11)]
print(squares)

