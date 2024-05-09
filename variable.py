x, y, z = "Orange", "Banana", "Peach"

print(x)
print(y)
print(z)

fruits= ["Orange", "Banana", "Peach"]

a,b,c=fruits


d ="global variable"

def func():
    d="fantastic"
    print(x)

func()
print(x)

def is_global():
    global e 
    e= "I'm global!"

is_global()

print(e)