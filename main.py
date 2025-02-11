def round_up(num):
    #Rounds up a number, ex) 3.2 -> 4
    if num - int(num) == 0:
        return num
    else:
        return int(num + 1)


def prime(num):
    #If a number is prime, return True, else return False
    if num < 1:
        return False
    elif num - int(num) != 0: #Decimals are False
        return False
    elif num == 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
    return True
    



def prime_numbers(num):
    #Lists all of the prime numbers from 1 to num
    primes = [2]
    for i in range(3, num + 1):
        if prime(i):
            primes.append(i)
    return primes


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
    return [new_list, count_list]

    x = 0
    for i in list_1:
        if i == element:
            return x
        x += 1
    return False

def lcm(num1, num2):
    num1_data = compress(prime_factor(num1))
    num2_data = compress(prime_factor(num2))
    factor1_dic = {}
    factor2_dic = {}
    num = 1
    for i in range(len(num1_data[0])):
        factor1_dic[num1_data[0][i]] = num1_data[1][i]
    for i in range(len(num2_data[0])):
        factor2_dic[num2_data[0][i]] = num2_data[1][i]  
    
    for i in num1_data[0]:
        if i in factor2_dic:
            if factor1_dic[i] > factor2_dic[i]:
                num *= i ** factor1_dic[i]
            else:
                num *= i ** factor2_dic[i]
        else:
            num *= i ** factor1_dic[i]
    for i in num2_data[0]:
        if i not in factor1_dic:
            num *= i ** factor2_dic[i]
    return num


def gcf(num1, num2):
    num1_data = compress(prime_factor(num1))
    num2_data = compress(prime_factor(num2))
    factor1_dic = {}
    factor2_dic = {}
    num = 1
    for i in range(len(num1_data[0])):
        factor1_dic[num1_data[0][i]] = num1_data[1][i]
    for i in range(len(num2_data[0])):
        factor2_dic[num2_data[0][i]] = num2_data[1][i]    
    for i in num1_data[0]:
        if i in factor2_dic:
            if factor1_dic[i] < factor2_dic[i]:
                num *= i ** factor1_dic[i]
            else:
                num *= i ** factor2_dic[i]
    return num

                