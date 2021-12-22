import random
from sys import exit

count = 0
operators = ['*', '-', '+']
result = 0

print('Which level do you want? Enter a number:')
print('1 - simple operations with numbers 2-9')
print('2 - integral squares of 11-29')

correct_level = ['1', '2']
level_input = input()
if not level_input.strip('-').isnumeric():
    while level_input.strip('-').isnumeric() not in correct_level:
        print('Incorrect format.')
        level_input = input()


if level_input == '1':
    level = '1'
    level_description = 'simple operations with numbers 2-9'

    for _ in range(5):
        x = random.randint(2, 9)
        y = random.randint(2, 9)
        operator = random.choice(operators)

        if operator == '*':
            result = x * y
            print(x, '*', y)
        elif operator == '-':
            result = x - y
            print(x, '-', y)
        elif operator == '+':
            result = x + y
            print(x, '+', y)

        user_input = input()

        if not user_input.strip('-').isnumeric():
            while user_input.strip('-').isnumeric() is not True:
                print('Incorrect format.')
                user_input = input()
                if user_input.strip('-').isnumeric():
                    if int(user_input) == result:
                        print('Right!')
                        count += 1
                    else:
                        print('Wrong!')
        else:
            if int(user_input) == result:
                print('Right!')
                count += 1
            else:
                print('Wrong!')

if level_input == '2':
    level = '2'
    level_description = 'integral squares of 11-29'

    for _ in range(5):
        x = random.randint(11, 29)
        result = x * x
        print(x)

        user_input = input()

        if not user_input.strip('-').isnumeric():
            while user_input.strip('-').isnumeric() is not True:
                print('Incorrect format.')
                user_input = input()
                if user_input.strip('-').isnumeric():
                    if int(user_input) == result:
                        print('Right!')
                        count += 1
                    else:
                        print('Wrong!')
        else:
            if int(user_input) == result:
                print('Right!')
                count += 1
            else:
                print('Wrong!')


print(f'Your mark is {count}/5. Would you like to save your result to the file? Enter yes or no.')

positive = ["Yes", "YES", "yes", "y", "Y"]
negative = ["No", "NO", "no", "n", "N"]

save_input = input()

if save_input in positive:
    print('What is your name?')
    name = input()
    res_file = open('results.txt', "a+")
    res_text = str(f'{name}: {count}/5 in level {level} ({level_description}).')
    res_file.write(res_text)
    res_file.close()
    print('The results are saved in "results.txt".')

elif save_input in negative:
    exit()
