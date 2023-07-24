# Create a function named count_vowels that takes a string as a parameter.
# Inside the function, count the number of vowels (a, e, i, o, u, A, E, I, O, U) in the given string.
# Return the count of vowels.

def count_vowels(str):
    counter = 0
    list = ['a','e','u','i','o','A','E','U','I','O']
    for i in range(len(str)):
        if str[i] in list:
            counter +=1

    return counter
print(count_vowels(str='sherbekaaSHERBEK'))