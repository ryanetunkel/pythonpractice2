import math

def nth_prime():
    n = 10001
    count = 0
    num = 2
    while count < n:
        print(count)
        idx = 2
        while idx <= num:
            if num % idx == 0:
                if num != idx:
                    break
                elif num == idx:
                    count += 1 
            idx += 1
        if count < n:
            num += 1
    print(num)

def main():
    nth_prime()

if __name__ == "__main__":
    main()