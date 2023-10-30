import math

def nth_prime():
    n = 10001
    count = 1
    num = 2
    while count < n:
        for i in range(2,num):
            if num % i == 0:
                if num != i:
                    break
                else:
                    count += 1 
        num += 1
    print(num)

def main():
    nth_prime()

if __name__ == "__main__":
    main()