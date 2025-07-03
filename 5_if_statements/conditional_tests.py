"""
5-1. Conditional Tests: 

Write a series of conditional tests. Print a statement
describing each test and your prediction for the results of each test. Your code
should look something like this:

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

• Look closely at your results, and make sure you understand why each line
evaluates to True or False.
• Create at least 10 tests. Have at least 5 tests evaluate to True and another
5 tests evaluate to False.

5-2. More Conditional Tests: 

You don’t have to limit the number of tests you
create to 10. If you want to try more comparisons, write more tests and add
them to conditional_tests.py. Have at least one True and one False result for
each of the following:

• Tests for equality and inequality with strings
• Tests using the lower() function
• Numerical tests involving equality and inequality, greater than and
less than, greater than or equal to, and less than or equal to
• Tests using the and keyword and the or keyword
• Test whether an item is in a list
• Test whether an item is not in a list
"""

FAV_COUNTRY = 'lithuania'
LT_POPULATION = 2897430
LT_FOODS = 'cepelinai'
LT_NATIVE_LANGUAGE = 'lithuanian'
LT_2ND_LANGUAGE = 'russian'
LT_SPORT = 'Basketball'
LT_INDUSTRY_0 = 'petroleum refining'
LT_INDUSTRY_1 = 'food processing'
LT_TREES = ['oak', 'scots pine', 'norwegian spruce', 'birch']


print("Is favorite country == 'poland'? I predict False.")
print(FAV_COUNTRY == 'poland')
print("\nIs favorite country == 'lithuania'? I predict True.")
print(FAV_COUNTRY == 'lithuania')

print("\nIs Lithuania's population more than 3 milion? I predict False.")
print(LT_POPULATION > 3000000)
print("\nIs Lithuania's population less than 3 milion? I predict True.")
print(LT_POPULATION < 3000000)
print("\nIs Lithuania's population equal or more than 2.9 milion? I predict", 
      "False."
    )
print(LT_POPULATION >= 2900000)
print("\nIs Lithuania's population equal or less than 2.899.000 milion?", 
      "I predict True."
    )
print(LT_POPULATION <= 2899000)
print("\nIs Lithuania's population 2.890.000 milion? I predict False.")
print(LT_POPULATION == 2890000)
print("\nIs Lithuania's population 2.897.430 milion? I predict True.")
print(LT_POPULATION == 2897430)

print("\n'Pizza' is one of Lithuania's well known foods. I predict False.")
print(LT_FOODS == 'pizza')
print("\n'Cepelinai' is one of Lithuania's well known foods. I predict True.")
print(LT_FOODS == 'cepelinai')

print("\nIs 'basketball' the most popular sport in Lithuania? I predict True!")
print(LT_SPORT.lower() == 'basketball')

print("\nAre the most commonly spoken languages in Lithuania 'lithuanian and",
      "'russian'? I predict True."
    )
print(LT_NATIVE_LANGUAGE == 'lithuanian' and LT_2ND_LANGUAGE == 'russian')

print("\n'petroleum refining' or 'food processing' is one of Lithuania's most",
      "common industries. I predict True."
    )
print(LT_INDUSTRY_0 == 'petroleum refining' or 
      LT_INDUSTRY_1 == 'food processing'
      )

print("\nIs the 'scots pine' one of Lithuania's most common trees? I predict",
      "True."
      )
print('scots pine' in LT_TREES)
print("\nIs the 'palm tree' one of Lithuania's most common trees? I predict",
      "False."
      )
print('palm tree' in LT_TREES)
