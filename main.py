def prime_numbers(num):
    #Lists all of the prime numbers from 1 to num
    primes = []
    factors = []
    number = 2
    while number < num:
        for i in range(number):
            if i != 0 and i != 1:
                if number % i == 0:
                    factors.append(i)
        if len(factors) == 0:
            primes.append(number)
        factors = []
        number += 1
    return primes

def prime_factor(num):
    factors = []
    total_primes = prime_numbers(num)
    while num != 1:
        for i in total_primes:
            if num % i == 0:
                num = num % i
                factors.append(i)
                break
    factors.append(num)
    return factors

print(prime_factor(20))