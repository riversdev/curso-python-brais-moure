# higher order functions
def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5

def sum_two_values_and_add_value(first_value, second_value, f_sum_one):
    return f_sum_one(first_value + second_value)

print(sum_two_values_and_add_value(5, 2, sum_one))
print(sum_two_values_and_add_value(5, 2, sum_five))



# closures
def sum_ten(original_value):
    def add(value):
        return value + 10 + original_value
    return add

add_closure = sum_ten(1)
print(add_closure(5))

print(sum_ten(5)(1))



# Built-in Higher Order Functions
numbers = [2, 5, 10, 21, 3, 30]

# Map
def multiply_two(number):
    return number * 2

print(list(map(multiply_two, numbers)))
print(list(map(lambda number: number * 2, numbers)))

# Filter
def filter_greater_than_ten(number):
    return number > 10

print(list(filter(filter_greater_than_ten, numbers)))
print(list(filter(lambda number: number > 10, numbers)))

# Reduce
from functools import reduce

def sum_all(acc, curr):
    return acc + curr

print(reduce(sum_all, numbers))
print(reduce(lambda a, b: a + b, numbers))