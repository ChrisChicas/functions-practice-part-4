"""
/Write a Python function called max_num()to find the maximum of three numbers.
/Write a Python function called mult_list() to multiply all the numbers in a list.
/Write a Python function called rev_string() to reverse a string.
/Write a Python function called num_within() to check whether a number falls in a given range.
/The function accepts the number, beginning of range, and end of range (inclusive) as arguments.
/Examples: num_within(3,2,4) returns True, num_within(3,1,3) returns True, num_within(10,2,5) returns False.
Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
The function accepts the number n, the number of rows to print
Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal. Each number is the two numbers above it added together.
"""
def max_num(int1, int2, int3):
    return max(int1, int2, int3)
print(max_num(81,723,111))
print(max_num(81,723,1211))
print(max_num(8231231,723,111))

def mult_list(list):
    if len(list) == 0:
        return 0
    product = 1
    for i in list:
        product = product * i
    return product
print(mult_list([3,3,3,2]))
print(mult_list([]))

def rev_string(string):
    if isinstance(string, str):
        return string[::-1]
    else:
        return "Not a string."
print(rev_string("hello friends"))
print(rev_string(123))

def num_within(num, r1, r2):
    print(num in range (r1, r2 + 1))
num_within(3,2,4)
num_within(3,1,3)
num_within(10,2,5)

triangle = [[1], [1,1]]
def pascal(n):
    if n < 1:
        print("Invalid number of rows.")
    elif n == 1:
        print(triangle[0])
    else:
        row_number = 2
        while len(triangle) < n:
            row = []
            row_prev = triangle[row_number - 1]
            length = len(row_prev) + 1
            for i in range(length):
                if i == 0:
                    row.append(1)
                elif i > 0 and i < length-1:
                    row.append(triangle[row_number - 1][i-1] + triangle[row_number - 1][i])
                else:
                    row.append(1)
            triangle.append(row)
            row_number += 1

        for row in triangle:
            print(row)
pascal(2)
pascal(5)