def G(q,r,k):
    num=1;
    den=1;
    for i in range(1,k+1):
        num*=q**r-q**(k-i);
        den*=q**k-q**(k-i);
    return num//den
