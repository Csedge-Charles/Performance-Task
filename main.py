def round_up(num):
    if num - int(num) == 0:
        return num
    else:
        return int(num) + 1


def prime(num):
    if num < 1:
        return False
    elif num - int(num) != 0:
        return False
    elif num == 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, int(round_up((num) ** 0.5))):
            if num % i == 0:
                return False
    return True
    



def prime_numbers(num):
    #Lists all of the prime numbers from 1 to num
    primes = [2]
    for i in range(3, num):
        if prime(i):
            primes.append(i)
    return(primes)



def prime_factor(num):
    factors = []
    total_primes = prime_numbers(num)
    while num != 1:
        for i in total_primes:
            if num % i == 0:
                num = num / i
                factors.append(i)
                break
    return factors

def compress(factors):
    count_list = []
    new_list = []
    count = 0
    iterator = 0
    for i in factors:
        if iterator + 1 < len(factors):
            if i == factors[iterator + 1]:
                count += 1
            else:
                count += 1
                count_list.append(count)
                new_list.append(i)
                count = 0
        else:
            count += 1
            new_list.append(i)
            count_list.append(count)
            count = 0
        iterator += 1
    return [count_list, new_list]

def multiply(factors):
    num = 1
    for i in factors:
        num *= i
    return num

def getElement(list_1, element):
    x = 0
    for i in list_1:
        if i == element:
            return x
        x += 1
    return False

def lcm(num_1, num_2):
    if prime(num_1) or prime(num_2):
        return num_1 * num_2
    else: 
        lcm_list = []
        count1 = compress(prime_factor(num_1))[0]
        count2 = compress(prime_factor(num_2))[0]
        factor1 = compress(prime_factor(num_1))[1]
        factor2 = compress(prime_factor(num_2))[1]
        
        if len(count1) > len(count2):
            count1 = count2
            count2 = count1
            factor1 = factor2
            factor2 = factor1
        for i in range(len(count1)):
            if factor1[i] not in factor2:
                lcm_list.append(factor1[i] ** count1[i])
            else:
                if count1[i] <= count2[getElement(factor2, factor1[i])]:
                    lcm_list.append(factor1[i] ** count2[getElement(factor2, factor1[i])]) 
                else:
                    lcm_list.append(factor1[i] ** count1[i])
        for i in range(len(factor2)):
            if factor2[i] not in lcm_list and factor2[i] not in factor1:
                lcm_list.append(factor2[i])
        return multiply(lcm_list)


def gcf(num_1, num_2):
    lcm_list = []
    count1 = compress(prime_factor(num_1))[0]
    count2 = compress(prime_factor(num_2))[0]
    factor1 = compress(prime_factor(num_1))[1]
    factor2 = compress(prime_factor(num_2))[1]
    
    if len(count1) > len(count2):
        count1 = count2
        count2 = count1
        factor1 = factor2
        factor2 = factor1
    for i in range(len(count1)):
        if factor1[i] in factor2:
            if count1[i] <= count2[getElement(factor2, factor1[i])]:
                lcm_list.append(factor1[i] ** count1[i]) 
            else:
                lcm_list.append(factor1[i] ** count2[getElement(factor2, factor1[i])])
    return multiply(lcm_list)

print(gcf(21928, 3192))
                
    
        