def srednia_arytmetyczna(L):
    """Funkcja oblicza srednia arytmetyczna liczb w liscie/krotce L"""
    assert isinstance(L, (list, tuple))
    return float(sum(L)) / len(L)


def srednia(L, typ='A'):
    """Funkcja liczy srednia.
    WEJ: L - lista
         typ - 'A' srednia arytmetyczna (domyslnie)
               'K' kwadratowa

    WYJ: FLOAT - srednia liczb z L"""

    ret = None
    if typ.upper() == 'A':
        ret = srednia_arytmetyczna(L)
    elif typ.upper() == 'K':
        print "Not implemented"

    return ret


if __name__ == "__main__":
    print srednia([1, 1, 1, 1, 1])
