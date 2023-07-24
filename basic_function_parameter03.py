# Create a function named find_smallest that takes a list of numbers as a parameter.
# Inside the function, find the smallest number in the given list.
# Return the smallest number.

def find_smallest(list):
    sml = list[0]
    for i in range(len(list)):
        if sml > list[i]:
            sml = list[i]
    return sml

print(find_smallest(list=[2,3,4,5,1]))