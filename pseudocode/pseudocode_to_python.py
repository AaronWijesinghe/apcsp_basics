def calculate_average(numbers):
    total = 0
    for number in numbers:
        total += number
    average = total / len(numbers)
    return average

def find_minimum(numbers):
    min_value = numbers[0]
    for number in numbers:
        if number < min_value:
            min_value = number
    return min_value

# Expected output: 3.0
print(calculate_average([1, 2, 3, 4, 5]))

# Expected output: 69
print(find_minimum([100, 200, 69, 300, 400]))