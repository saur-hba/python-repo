def lbs_to_kgs(weight):
    return weight * 0.45

def kgs_to_lb(weight):
    return weight / 0.45

def find_max(numbers):
    max = numbers[0]
    for number in numbers:
        if number > max:
            max = number
    return max

def find_min(numbers):
    min = numbers[0]
    for number in numbers:
        if number < min:
            min = number
    return min