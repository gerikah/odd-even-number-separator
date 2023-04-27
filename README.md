# odd-even-number-separator
>>> ODD - EVEN number separator

This Python program reads a text file named numbers.txt that contains 20 integers, and then creates two other text files; even.txt containing all even numbers extracted from numbers.txt and odd.txt containing all odd numbers extracted from numbers.txt.

In this program, the even and odd numbers are written to their respective files in a table format with the count of each number in the original list.

> Prerequisites

Before running this program, you need to have Python 3 installed on your computer. You can download Python 3 from the official website: https://www.python.org/downloads/

> How to run the program

1. Clone the repository to your local machine.
2. Place the numbers.txt file in the same directory as the program.
3. Open the terminal/command prompt and navigate to the project directory.
4. Run the following command: python odd-even-number-separator.py

> Description

This program reads the numbers.txt file and extracts all even and odd numbers from it, and then saves them to even.txt and odd.txt respectively. The numbers are written in a table format with the count of each number in the original list.

> Usage

The numbers.txt file must contain 20 integers separated by spaces. You can create your own numbers.txt file or use the provided numbers.txt file.

> Examples

    Example numbers.txt file:
        1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
    
    Example Output
    If you run the program with the above numbers.txt file, the following output files will be created:

    even.txt
    +------+-------+
    | Even | Count |
    +------+-------+
    | 2    | 1     |
    | 4    | 1     |
    | 6    | 1     |
    | 8    | 1     |
    | 10   | 1     |
    | 12   | 1     |
    | 14   | 1     |
    | 16   | 1     |
    | 18   | 1     |
    | 20   | 1     |
    +------+-------+
    
    odd.txt
    +-----+-------+
    | Odd | Count |
    +-----+-------+
    | 1   | 1     |
    | 3   | 1     |
    | 5   | 1     |
    | 7   | 1     |
    | 9   | 1     |
    | 11  | 1     |
    | 13  | 1     |
    | 15  | 1     |
    | 17  | 1     |
    | 19  | 1     |
    +-----+-------+

> License

This project is licensed under the MIT License - see the LICENSE.md file for details.

> Acknowledgments

This program was created as part of a Python programming exercise in Object Oriented Programming