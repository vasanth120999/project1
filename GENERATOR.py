# GENERATOR:

"""def count_of(n):
    count=1
    while count<=n:
        yield count
        count+=1
for i in count_of(5):
    print(i)"""

# PROGRAM TO PRINT SQUARE NO & CUBE NO:

"""def fun(n):
    yield n**2
    yield n**3
print(list(fun(5)))"""

# PROGRAM TO PRINT 1-10 :

"""def number_generator():
    for num in range(1, 11):
        yield num
print(list(number_generator()))"""

# TO PRINT EVEN NUMBERS:

"""def fun(n):
    for i in range(2,n+1,2):
        yield i
for a in fun(10):
    print(a)"""

# FIBONACCI NUMBER IN THE LIST :

"""def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
n = 10
fib_list = list(fib(n))
print(fib_list)"""

# EACH CHARACTER IN STRING LINE BY LINE

"""def heal_string(s):
    for i in range(1,len(s)+1):
        yield s[:i].upper()
name = "vasanth"
for healed in heal_string(name):
    print(healed)"""

# SQUARE OF A NUMBER FROM 1-10:

"""def heal_squares():
    for num in range(1, 11):
        yield f"{num ** 2}"
for healed in heal_squares():
    print(healed)"""

# GENERATOR COMPREHENSION :

# CUBE OF A NUMBER FROM 1-20:

"""print(list(i**3 for i in range(1,21)))"""

# GENERATOR EXPRESSION EVEN NUMBER 1-100:

"""print (list((i for i in range(1,101)if i%2==0)))"""

# GENERATOR EXPRESSION LENGTH OF EACH STRING :

"""a=["apple","for", "a"]
print(list(len(a) for a in a))"""

# GENERATOR EXPRESSION THAT HEALS UPPER CASE:

"""s="vasanth"
m=(list(s.upper()for s in s))
for i in m:
    print(i)"""

# GENERATOE EXPRESSION A SQUARE OF THE NUMBER 1-50:

"""print(list(i**2 for i in range(1,51) if i%2==1))"""


# FUNCTIONS STARTING WITH VOWELS AND ENDING WITH VOWELS:

"""a=list(input().split())
def fun(a):
    for i in range (len(a)):
        if a[0][0] in 'aeiou' and a[0][-1] in 'aeiou':
            yield(i,a[i])
print(list(fun(a)))"""


# WRITE TO RETURN ELEMENT BY RAISING TO INDEX IN GENERATOR:

"""def index(lst):
    for index, value in enumerate(lst):
        yield value ** index
a= [2, 3, 4, 5]
print(list(index(a)))"""

"""a=[1,2,3,4,5]
def fun(a):
    for i,j in enumerate(a):
        yield j**i
print(list(fun(a)))"""

################# CLOSURE ###################

"""def retro(x):
    def sample(y):
        print(x+y)
    return sample
obj=retro(5)
obj(10)"""

#GREETING MESSAGE WITH NAME :

"""def name(x):
    def func(y):
        print(x+y)
    return func
obj=name("love you")
obj("babe")"""

#COMPUTE X RAISED TO THE POWER OF N:

"""def power_function(n):
    def compute_power(x):
        return x ** n
    return compute_power
square = power_function(2)
print(square(5))"""

# COUNT THE VALUE EVERYTIME WHEN ITS CALLED :

"""def counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    def get_count():
        return count
    return increment, get_count
inc, get_value = counter()
print(inc())
print(inc())  
print(get_value())"""

# CLOSURE STIMULATE DEPOSITS & WITHDRAWL &BANK BALANCE:

"""def bank_account(initial_balance=0):
    balance = initial_balance
    def transaction():
        def deposit(amount):
            nonlocal balance
            if amount > 0:
                balance += amount
                return f"Deposited: ₹{amount}. New Balance: ₹{balance}"
            return "Deposit amount must be positive."
        def withdraw(amount):
            nonlocal balance
            if 0 < amount <= balance:
                balance -= amount
                return f"Withdrawn: ₹{amount}. New Balance: ₹{balance}"
            return "Insufficient funds or invalid withdrawal amount."
        def check_balance():
            return f"Current Balance: ₹{balance}"

        return deposit, withdraw, check_balance
    return transaction()
deposit, withdraw, check_balance = bank_account(1000)
print(deposit(500))
print(withdraw(300))
print(check_balance())"""

# RECRESSION FUNCTION TO PRINT FIBONACCI NUMBER :

"""def fibonacci_memoized():
    a= {}  

    def fib(n):
        if n in a:  
            return a[n]
        if n <= 1:  
            result = n
        else:
            result = fib(n - 1) + fib(n - 2)  
        a[n] = result  
        return result

    return fib  
fib = fibonacci_memoized()
for i in range(11):
    print(f"fib({i}) =", fib(i))"""

"""def outer():
    def inner(n):
        if n<=1:
            return n
        return inner(n-1)+inner(n-2)
    return inner
obj=outer()
print(obj(5))"""

################# ITERATOR ####################

"""l1=[1,2,3,4,5]
l1=iter(l1)
print(next(l1))
print(next(l1))"""

#USE CLOSURE TO IMPLEMENT A VERSION OF RECRUSIVE FACTORIAL FUNCTION :

"""def memoized_factorial():
    cache = {}

    def factorial(n):
        if n in cache:  
            return cache[n]
        if n <= 1:
            result = 1
        else:
            result = n * factorial(n - 1)
        cache[n] = result  
        return result
    return factorial
factorial = memoized_factorial()
print(factorial(5)) 
print(factorial(6))""" 

# REVERSE A NUMBER USING CLOSURE :

"""def reverse_number_closure():
    def reverse(n):
        return int(str(n)[::-1])

    return reverse
reverse_number = reverse_number_closure()
print(reverse_number(12345))  
print(reverse_number(987))"""


