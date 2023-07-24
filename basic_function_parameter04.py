# Create a function named calculate_average that takes a list of numbers as a parameter.
# Inside the function, calculate the average of all the numbers in the given list.
# Return the average.
# Return the average.

def calculate_average(list):
    summ = 0
    for i in range(len(list)):
        summ += list[i]

    average = summ // len(list)
    return average
print(calculate_average(list=[5,5,3,4,5,5]))