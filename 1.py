name = input('What is your name: ')
age = int(input('What is your age: '))
print('You will be ' + str(age + 100) + ' years old after 100 years passed ' + name)
multp = ('You will be ' + str(age + 100) + ' years old after 100 years passed ' + name + "\n") * 4
print(multp)