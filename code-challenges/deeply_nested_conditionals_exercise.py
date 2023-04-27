def filter_numbers(numbers):
    filtered_numbers = []
    for number in numbers:
        if number > 10:
            if number < 20:
                filtered_numbers.append(number)
    return filtered_numbers
