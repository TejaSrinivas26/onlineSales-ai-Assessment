def compute(n):
    if n < 10:
        out = n ** 2  # Compute square of n for values less than 10
    elif 10 <= n <= 20:
        out = 1
        for i in range(1, n - 9):
            out *= i  # Compute factorial of (n - 9) for values between 10 and 20
    else:
        lim = n - 20
        out = sum(range(1, lim + 1))  # Compute the sum of numbers from 1 to (n - 20) for values greater than 20
    print(out)  # Output the computed result

# Testing the compute function
compute(4)   # Output: 16 (4^2)
compute(15)  # Output: 120 (5!)
compute(25)  # Output: 15 (1 + 2 + 3 + 4 + 5)
