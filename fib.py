def fib(num):
    sequence = [0, 1]
    if num == 1:
        return [0]
    for i in range(2, num):
        sequence.append(sequence[i - 1] + sequence[i - 2])
    return sequence

print(fib(15))