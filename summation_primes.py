import math

def summation_primes(n):
    sum = 0
    primes = []
    for i in range(n):
        print(i)
        for j in primes:
            if i % j == 0:
                if j != i:
                    break
                else:
                    primes.append(j)
                    sum += j
    return sum

def main():
    print("Summation of Primes:",summation_primes(2000000))

if __name__ == "__main__":
    main()