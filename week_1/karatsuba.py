

def compute(x, y):
    if len(str(x)) == 1 or len(str(y)) == 1:
        return x*y

    n = max(len(str(x)),len(str(y)))
    nby2 = n / 2
    
    a = x / 10**(nby2)
    b = x % 10**(nby2)
    c = y / 10**(nby2)
    d = y % 10**(nby2)

    ac = compute(a,c)
    bd = compute(b,d)
    ad_plus_bc = compute(a+b,c+d) - ac - bd
    prod = ac * 10**(2*nby2) + (ad_plus_bc * 10**nby2) + bd
    return prod