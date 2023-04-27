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
        # write the table header
    even_file.write("+------+-------+\n")
    even_file.write("| Even | Count |\n")
    even_file.write("+------+-------+\n")
#    even_file.write("\n".join(map(str, even_numbers)))

        # write each even number and its count to the table
    for num in even_numbers:
        count = numbers.count(num)
        even_file.write("| {:^4} | {:^5} |\n".format(num, count))
        even_file.write("+------+-------+\n")

# write the odd numbers to the file "odd.txt"
with open("odd.txt", "w") as odd_file:
        # write the table header
    odd_file.write("+------+-------+\n")
    odd_file.write("| Odd  | Count |\n")
    odd_file.write("+------+-------+\n")
#    odd_file.write("\n".join(map(str, odd_numbers)))

    # write each odd number and its count to the table
    for num in odd_numbers:
        count = numbers.count(num)
        odd_file.write("|  {:^3} | {:^5} |\n".format(num, count))
        odd_file.write("+------+-------+\n")
#close txt files
input_file.close()
even_file.close()
odd_file.close()