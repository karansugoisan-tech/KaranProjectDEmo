def fib_gen():
    a,b = 0,1

    while True:
        yield a
        a,b = b,a+b
    
    
    
f = fib_gen()
for _ in range(15):
    print(next(f))
