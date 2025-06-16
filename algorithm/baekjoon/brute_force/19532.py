a,b,c,d,e,f = list(map(int, input().split()))

try:
    y = (c*d - a*f)/(b*d - a*e)
    x = (c - (b*y))/a
except ZeroDivisionError:
    if a == 0:
        y = c / b
        x = (f - e*c/b)/d
    else:
        y = 0
        x = 0
finally:
    print(int(x), int(y))