#Question 1

def vat_Calc(amt, rate):
    """ Returns the amount of VAT to pay based on the amt and rate
    >>> vat_Calc(100, 20)
    20.0

    >>> vat_Calc(150.55, 20)
    30.11
    """
    return (amt / 100) * rate


def main():
    print(f"20% of 100 = {vat_Calc(100,20)}")
    print(f"20% of 150.55 = {vat_Calc(150.55, 20)}")
    return None

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()




