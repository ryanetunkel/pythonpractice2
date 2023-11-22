import math

def pythagorean_triplets():
    for a in range(1,332 + 1):
        for b in range(a+1,499 + 1):
            for c in range(b+1,997 + 1):
                if ((a * a) + (b * b)) == c * c and a + b + c == 1000:
                    print(a*b*c)

def main():
    pythagorean_triplets()

if __name__ == "__main__":
    main()