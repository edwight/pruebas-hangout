#serie fibonaci Sem5Des2+EdwightDelgado.py
# usando recursividad
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n > 1:
        return fib(n-1) + fib(n-2)

x = input('n')
for i in range(0, x):
    print fib(i)
