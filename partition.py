EMPTY_SUM = 0

#inc = lambda x: x + 1
dec = lambda x: x - 1

_p = dict()


def partition(n: int) -> int:
    """Pure Python partition function, ported to Python from SageMath.
    A000041 implemented by Peter Luschny.
    @CachedFunction
    def A000041(n):
    if n == 0: return 1
    S = 0; J = n-1; k = 2
    while 0 <= J:
        T = A000041(J)
        S = S+T if is_odd(k//2) else S-T
        J -= k if is_odd(k) else k//2
        k += 1
    return S
    """
    if n in _p.keys():
        return _p[n]
    if not n:
        return 1
    sum, j, k = EMPTY_SUM, dec(n), 2
    while j >= 0:
        t = partition(j)
        if k//2 % 2:
            sum += t
        else:
            sum -= t
        if k % 2:
            j -= k
        else:
            j -= k//2
        k += 1
    _p[n] = sum
    return sum
