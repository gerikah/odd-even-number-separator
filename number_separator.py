# Object Oriented Programming CMPE-103 PROGRAMMING EXERCISES : Problem 1
# ALDAY, Gerikah L. - BSCPE 1-5

# open the file "numbers.txt" in read mode
with open("numbers.txt", "r") as input_file:
    # read all the integers from the file and convert them to a list of integers
    numbers = list(map(int, input_file.read().split()))

# create empty lists to store even and odd numbers
even_numbers = []
odd_numbers = []

# iterate over each number in the list of numbers
for num in numbers:
    # check if the number is even or odd
    if num % 2 == 0:
        # add the even number to the list of even numbers
        even_numbers.append(num)
    else:
        # add the odd number to the list of odd numbers
        odd_numbers.append(num)

# write the even numbers to the file "even.txt"
with open("even.txt", "w") as even_file:
    even_file.write("\n".join(map(str, even_numbers)))

# write the odd numbers to the file "odd.txt"
