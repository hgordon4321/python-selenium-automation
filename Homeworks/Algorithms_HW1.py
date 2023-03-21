# Problem 1


def sum_to_n(n: int):
    total = 0
    for i in range(1, n+1):
        total = total + i
    return [n, total]


# Problem 2, short way
def find_max (a:int , b: int, c: int):
    return[a, b, c, max(a, b, c)]


# Because max function makes problem 2 trivial, I assume something like the following was desired:
def find_max_long (a:int , b: int, c: int):
    max = a
    if max < b:
        max = b
    if max < c:
        max = c
    return [a, b, c, max]


#Problem 3
def count_even_odd (n: int):
    number = n
    even_ct = 0
    odd_ct = 0
    r = 0
    while n !=0:
        r = n % 10
        odd = r % 2
        odd_ct = odd_ct + odd
        even_ct = even_ct + (1 - odd)
        n = n // 10
    return [number, odd_ct, even_ct]


#Function calls
ex1 = sum_to_n(7)
print(f'Sum of numbers from 1 to {ex1[0]}: {ex1[1]}')
ex2 = find_max(200, 56, 235)
print(f'The highest number among {ex2[0]}, {ex2[1]}, and {ex2[2]} is {ex2[3]}')
ex3 = find_max_long(200, 56, 235)
print(f'The highest number among {ex3[0]}, {ex3[1]}, and {ex3[2]} is {ex3[3]}')
ex4 = count_even_odd(46872)
print(f'For {ex4[0]}, number of odd digits is {ex4[1]}, number of even digits is {ex4[2]}')