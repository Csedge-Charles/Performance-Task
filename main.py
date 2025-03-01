def round_up(num): #Rounds up a number, ex) 3.2 -> 4
    if num - int(num) == 0:
        return num 
    else:
        return int(num + 1)


def prime(num): #If a number is prime, return True, else return False
    if num < 1: #Any number less than one is not prime
        return False
    elif num - int(num) != 0: #Decimals aren't prime
        return False
    elif num == 1: #1 is not prime
        return False
    elif num == 2: #2 is prime
        return True
    else:
        for i in range(2, num): #Iterates through every number from 2 - num to check if it is divisible
            if num % i == 0:
                return False
    return True
    



def prime_numbers(num): #Lists all of the prime numbers from 1 to num
    if num == 1:
        return []
    primes = [2] #starts with 2
    for i in range(3, num + 1): #iterates through every number
        if prime(i): #checks if number is prime
            primes.append(i) #adds number if it is prime
    return primes


def prime_factor(num): #prime factorizes the number
    factors = [] #declares list to store primes
    total_primes = prime_numbers(num) #gets the all prime numbers from 1 to num
    while num != 1: #keeps iterating until num isn't divisible
        for i in total_primes: #iterates through all primes
            if num % i == 0:
                num = num / i #divides num by the prime
                factors.append(i)
                break
    return factors

def compress(factors): #Turns a list with duplicates ex) [1, 1, 2, 2] and outputs a single list with two lists inside
    #first list is the original with no duplicates and the second is how many duplicates are there for each corresponding number in the first list ex) [1, 1, 2, 2] -> [[1, 2], [2, 2]]
    count_list = [] #list for the number of duplicates
    new_list = [] #list for original without duplicates
    count = 0
    iterator = 0
    for i in factors: #iterates through all factors
        if iterator + 1 < len(factors):
            if i == factors[iterator + 1]:
                count += 1 #if current iteration equals next iteration, count increases by 1
            else:
                count += 1 #if not, add current iteration to count
                count_list.append(count) #add count to count list
                new_list.append(i) #add current iteration to new list
                count = 0 #reset count
        else:
            count += 1 #if on last iteration, count increases by 1
            new_list.append(i) #add current iteration to new list
            count_list.append(count) #add count to count list
            count = 0 #reset count
        iterator += 1 #iteration increases at the end
    return [new_list, count_list]

def lcm(num1, num2): #Finds the least common multiple of two numbers
    num1_data = compress(prime_factor(num1)) #Gets simplified version and how many duplicates
    num2_data = compress(prime_factor(num2))
    factor1_dic = {} #Dictionary used for displaying {factor: how many duplicates}
    factor2_dic = {}
    num = 1
    for i in range(len(num1_data[0])):
        factor1_dic[num1_data[0][i]] = num1_data[1][i] #Adds the elements to the dictionary
    for i in range(len(num2_data[0])):
        factor2_dic[num2_data[0][i]] = num2_data[1][i]  
        
    for i in num1_data[0]: #iterates through factors of num 1
        if i in factor2_dic: #if current factor is shared with num 2
            if factor1_dic[i] > factor2_dic[i]: #compares the number of current factors or duplicates
                num *= i ** factor1_dic[i] #take the larger one
            else:
                num *= i ** factor2_dic[i] 
        else:
            num *= i ** factor1_dic[i]
    for i in num2_data[0]: #iterating through unshared factors
        if i not in factor1_dic:
            num *= i ** factor2_dic[i] #include them into the calculation
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
            if factor1_dic[i] < factor2_dic[i]: #compares the number of current factors or duplicates
                num *= i ** factor1_dic[i] #take the smaller one
            else:
                num *= i ** factor2_dic[i]
    return num

print("This is a calculator that can find the lcm of gcf of any two positive integers")
choice = input("LCM or GCF: ")
number_1 = int(input("First number: "))
number_2 = int(input("Second number: "))

if choice.upper() == "LCM": #ensures that variations of capitalization are included
    print(lcm(number_1, number_2))
    
elif choice.upper() == "GCF":
    print(gcf(number_1, number_2))
else:
    print("Opperator not found")