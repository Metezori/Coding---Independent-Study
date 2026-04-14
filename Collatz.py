import tqdm

def collatz(n):
    steps = 0
    while n > 1:
        if n%2 == 0:
            n //= 2
            print (n)
            steps += 1
        else:
            n = 3*n+1
            print (n)
            steps += 1
    return ("Steps: " + str(steps))

#print(collatz(int(input("Number: "))))

def fast_collatz(n):
    steps = 0
    while n > 1:
        if n%2 == 0:
            n //= 2
            steps += 1
        else:
            n = (3*n+1)//2
            steps += 2
    return (steps)

#print ("Steps: " + str(fast_collatz(int(input("Number: ")))))

def bitwise_collatz(n): 
    if not isinstance(n, int) or n < 1:
        return 0
    steps = 0
    while n > 1: 
        if not (n & 1):
            tz = (n & -n).bit_length() - 1 #tz is the number of times you can divide n by 2
            n >>= tz
            steps += tz
        else:
            n = 3 * n + 1
            steps += 1
    return steps

#print ("Steps: " + str(bitwise_collatz(int(input("Number: ")))))

def batch_collatz (r):
    most_steps = 0
    ms_number = []
    for n in tqdm.tqdm(range (1,r+1)):
        steps = bitwise_collatz(n)
        if steps > most_steps:
            most_steps = steps
            ms_number = [n]
        elif steps == most_steps:
            ms_number.append(n)
    print (f"Highest stopping time was {ms_number} taking {most_steps} steps")
    return ()

#batch_collatz(int(input("Range: ")))