def middle_square(seed, num_digits):
    """
    Middle Square Method Pseudorandom Number Generator
    
    Args:
        seed (int): The initial seed value to start the generator.
        num_digits (int): The number of digits to extract from the squared value.
        
    Returns:
        int: The next pseudorandom number in the sequence.
    """
    while True:
        squared = seed ** 2
        squared_str = str(squared)
        print(squared_str)
        
        # Pad with zeros if the squared value has fewer digits than needed
        squared_str = squared_str.zfill(num_digits * 2)
        print("padded: ",squared_str)
        
        # Extract the middle digits
        middle_index = len(squared_str) // 2 - num_digits // 2
        seed = int(squared_str[middle_index: middle_index + num_digits]) # 2:6
        
        yield seed

if __name__ == "__main__":
    seed = 540
    num_digits = 4
    generator = middle_square(seed, num_digits)
    
    # Generate and print the first 10 pseudorandom numbers
    for _ in range(10):
        print("rno: ",next(generator))


"""
Algorithm from Wikipedia:

seed_number = int(input("Please enter a four-digit number:\n[####] "))
number = seed_number
already_seen = set()
counter = 0

while number not in already_seen:
    counter += 1
    already_seen.add(number)
    number = int(str(number * number).zfill(8)[2:6])  # zfill adds padding of zeroes
    print(f"#{counter}: {number}")

print(f"We began with {seed_number} and"
      f" have repeated ourselves after {counter} steps"
      f" with {number}.")
"""