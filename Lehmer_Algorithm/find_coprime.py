import math

def find_coprimes(number):
    coprimes = []
    
    for i in range(2, 100):
        if math.gcd(number, i) == 1:
            coprimes.append(i)
    
    return coprimes

if __name__ == "__main__":
    input_number = 2147483647
    coprimes = find_coprimes(input_number)
    
    if not coprimes:
        print(f"There are no coprimes for {input_number}.")
    else:
        print(f"Coprimes of {input_number}: {coprimes}")
