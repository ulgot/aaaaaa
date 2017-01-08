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

    if typ.upper() == 'A':
        ret = srednia_arytmetyczna(L)
    elif typ.upper() == 'K':
        print "Not implemented"

    return None

