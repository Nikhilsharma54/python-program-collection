def fibonacci(count):
    """Return the first `count` numbers of the Fibonacci series."""
    series = []
    a, b = 0, 1
    for _ in range(count):
        series.append(a)
        a, b = b, a + b
    return series


if __name__ == "__main__":
    terms = int(input("How many terms? "))
    print(fibonacci(terms))
