"""
4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20,
inclusive.

4-4. One Million: Make a list of the numbers from one to one million, and then
use a for loop to print the numbers. (If the output is taking too long, stop it by
pressing ctrl-C or by closing the output window.)

4-5. Summing a Million: Make a list of the numbers from one to one million,
and then use min() and max() to make sure your list actually starts at one and
ends at one million. Also, use the sum() function to see how quickly Python can
add a million numbers.

4-6. Odd Numbers: Use the third argument of the range() function to make a list
of the odd numbers from 1 to 20. Use a for loop to print each number.

4-7. Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to
print the numbers in your list.

4-8. Cubes: A number raised to the third power is called a cube. For example,
the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that
is, the cube of each integer from 1 through 10), and use a for loop to print out
the value of each cube.

4-9. Cube Comprehension: Use a list comprehension to generate a list of the
first 10 cubes.
"""

for value in range(1,21):
    print(value)

milion = list(range(1, 1000001))
for number in milion:
    print(number)

print("\nThe minimum number: " + str(min(milion)))
print("The maximum number: " + str(max(milion)))
print("The sum of all numbers: " + str(sum(milion)))

print("\nAll odd numbers between 1 to 20:")
odd_numbers = list(range(1,21,2))
for number in odd_numbers:
    print(number)

print("\nMultiples of 3 from 3 to 30:")
multiples = []
for value in range(1,31):
    multiple = value*3
    multiples.append(multiple)
    print(multiple)

print("\nThe first 10 cubes are:")
cubes = []
for value in range(1,11):
    cube = value**3
    cubes.append(cube)
    print(cube)

print("\nThe first 10 cubes using a comprehension list:")
cube_comp = [value**3 for value in range(1,11)]
for cube in cube_comp:
    print(cube)

