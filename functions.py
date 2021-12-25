from sympy import symbols, solve

def trans_quad(a,b,c):
    x = symbols('x')
    return a * x**2 + b*x + c
    

def compute_roots(quad):
    return solve(quad)
    #listroots = [key for key in roots_zer.keys()]
    #return listroots








