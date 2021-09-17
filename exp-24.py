def greet_user(first_name, last_name):
    print(f'whats up {first_name} {last_name}')
    print('Are you high!')


print('Start')
greet_user('Steve', last_name='Rogers')
print('Done')
# position of the arguments matter in the positional arguments,for example first name and last name
# Where as in kwargs name of the variables are given like in above example to improve readability of the code
# always try to use positional arguments. use kwargs for numerical values.
# if we want to give one kwarg and one positional argument then always positional arg comes 1st and then kwarg
# and the variables should be in the same order as in function for this to execute.
# if kwarg is given first then it will generate error. 
