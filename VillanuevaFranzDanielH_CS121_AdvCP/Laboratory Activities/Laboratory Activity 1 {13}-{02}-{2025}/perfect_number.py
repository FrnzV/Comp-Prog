num = int(input("Enter a number: "))
if num < 2:
    print(f"{num} is not a perfect number.")
else:
    divisors_sum = sum(i for i in range(1, num) if num % i == 0)
    if divisors_sum == num:
        print(f"{num} is a perfect number.")
    else:
        print(f"{num} is not a perfect number.")