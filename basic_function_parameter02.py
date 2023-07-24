# Create a function named calculate_sum that takes a list of numbers as a parameter.
# Inside the function, calculate the sum of all the numbers in the given list.
# Return the sum.

def calculate_sum(list):
    summ = 0
    for i in range(len(list)):
        summ += list[i]
    return summ
print(calculate_sum(list=[1,2,3]))