'''
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
'''

def ChampernowneConstant(n):
    # n is the number of zeros till that we need multiplication
    i = 1
    my_list = ['1', '1']
    position = 0
    result = 1
    while i != n:
        position += 9*i*(10**(i-1))
        number = (10**(i+1) - position)//(i+1)
        Rem = (number + 1) % (i+1)
        my_list.append(str(number+1  + 10**i - 1)[Rem - 1])
        i += 1
    for x in my_list:
        result *= int(x)
    return result

print(ChampernowneConstant(6))