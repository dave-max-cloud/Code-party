languages = ['python', 'java', 'c++']
def uppercase(word):
    return word.upper()
result = map(uppercase, languages)
#print(list(result))

numbers = (1, 2, [3, 4], 5)
numbers[2][1] = 99
#print(numbers)

fruits = ('apple', 'banana', 'cherry')
fruits_list = list(fruits)
fruits_list.append('mango')
#print(fruits_list)
fruits_tuple = tuple(fruits_list)
#print(fruits_tuple)

def sum_inner_list(numbers):
    result = []
    for inner_list in numbers:
        total = 0
        for number in inner_list:
            total += number
        result.append(total)
    return result
numbers = [[2, 3, 4], [1, 5, 7], [4, 6, 8]]
result = sum_inner_list(numbers)
#print(result)

def divisible_by_3_and_5(number):
    return number % 3 == 0 and number % 5 == 0
number = range(1, 51)
result = filter(divisible_by_3_and_5, number)
#print(list(result))

def even(number):
    return number % 2 == 0
numbers = range(1, 21)
result = filter(even, numbers)
print(list(result))
