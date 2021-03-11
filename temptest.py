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

def add(x):
    return print(2*x)

def change(f):
    def new(x):
        return f(x)
    return print
    
add = change(add)

add(1)
