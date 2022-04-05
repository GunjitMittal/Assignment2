import sympy as smp
x = smp.symbols("x")
f = smp.sin(1/x)**2/x**2
r = smp.trigsimp(smp.trigsimp(smp.integrate(f,x)))
print(r)