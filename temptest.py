def addone(x):
    print(x)
    x += 1
    print(x)
    def newfunc():
        return print(x)
    return newfunc, x

a = 1
f,a = addone(a)
f()

---

def addone(x):
    x += 1
    return x    
a = 1
addone(1)

---

def addone(x):
    x += 1
    return x    
a = 1
a = addone(1)

---

def count(x):
    if x == 0:
        return print(0)
    return count(x-1)

def change(f):
    def new(x):
        print('run new')
        return f(x)
    return new
    
count = change(count)

count(3)

---

def fib(n):
    """The nth Fibonacci number.

    >>> fib(20)
    6765
    """
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-2) + fib(n-1)

# Time

def count(f):
    """Return a counted version of f with a call_count attribute.

    >>> def fib(n):
    ...     if n == 0 or n == 1:
    ...         return n
    ...     else:
    ...         return fib(n-2) + fib(n-1)
    >>> fib = count(fib)
    >>> fib(20)
    6765
    >>> fib.call_count
    21891
    """
    def counted(*args):
        counted.call_count += 1
        return f(*args)
    counted.call_count = 0
    return counted

fib = count(fib)

fib(3)

# new fib point to counted, but f still point to old fib.

---



memo = {}
call_count_with_memo = 0
call_count_no_memo = 0

def fib(n, use_memo = True):
    global call_count_no_memo, call_count_with_memo
    if n < 0: return None
    if n < 2: return n
    if use_memo:
        if n in memo: return memo[n]
        call_count_with_memo += 1
        memo[n] = fib(n-1, use_memo) + fib(n-2, use_memo)
        return memo[n]
    else:
        call_count_no_memo += 1
        return fib(n-1, use_memo) + fib(n-2, use_memo)

for n in range(12):
    print(fib(n, False))

for n in range(12):
    print(fib(n, True))



print(call_count_with_memo)
print(call_count_no_memo)
