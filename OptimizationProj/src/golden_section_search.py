golden_section_search.py
'''
python program for golden section search.
This implementation does not reuse function evaluation.
'''
import math

gr = (math.sqrt(5) + 1) / 2

def gss(f, a, b, tol=1e-5):
    '''
    golden section search
    to find the minimum of f on [a,b]
    f: a strictly unimodal function on [a,b]

    example:
    >>> f = lambda x: (x-2)**2
    >>> x = gss(f,1,5)
    >>>x
    2.0000096448775678

    '''

    c = b - (b - a) / gr
    d = a + (b - a) / gr

    while abs(c - d) > tol:
        if f(c) < f(d):
            b = d
        else: 
             a = c

        c = b - (b - a) / gr
        d = a + (b - a) / gr

    return (b + a) / 2