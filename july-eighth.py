""" This question was asked by ContextLogic.

Implement division of two positive integers without using the division, multiplication, or modulus operators. Return the quotient as an integer, ignoring the remainder. """

def div(int1, int2):
    if int1 < 0 or int2 < 0:
        print(f'{int1} and/or {int2} is/are negative')
        exit()
    # assuming int1 >= int2
    if int1 < int2:
        return 0
    else:
        return 1 + div(int1-int2,int2)



# iteration implementation of function
def iter_div(int1,int2):
    count = 0
    if int1 < 0 or int2 < 0:
        print(f'{int1} and/or {int2} is/are negative')
        exit()
    while int1 >= int2:
        int1 = int1 - int2
        count += 1
    return count



print(f'100 divided by 5 is {div(100,5)}')
print(f'24 divided by 7 is {div(24,7)}')
print(f'-1 divided by 0 is {div(-1,0)}')

# runs into maximum recursion error. not sure how to fix.