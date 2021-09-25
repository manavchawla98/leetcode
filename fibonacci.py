def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


def fib_top_down(n, memo):
    if n <= 1:
        print(f"returning {n}")
        return n
    if memo[n] != 0 and n > 1:
        return memo[n]
    print(f"calling {n - 1} and {n - 2}")
    memo[n] = fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    print(fib(10))
    print(fib_top_down(10, memo=[0] * 20))
