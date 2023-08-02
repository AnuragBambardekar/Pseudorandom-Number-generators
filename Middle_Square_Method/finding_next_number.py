# Finding out the next random number generated in a given sequence

def middle_square(seed, n_digits):
    seed = seed ** 2
    seed_str = str(seed).zfill(2 * n_digits)
    middle_digits = seed_str[n_digits//2: n_digits//2 + n_digits]
    return int(middle_digits)

def find_next_pseudorandom_number(sequence, n_digits):
    last_number = sequence[-1]
    return middle_square(last_number, n_digits)

if __name__ == "__main__":
    n_digits = 2  # Number of digits in each pseudorandom number
    given_sequence = [42, 76, 77, 92]

    next_pseudorandom_number = find_next_pseudorandom_number(given_sequence, n_digits)
    print("Next pseudorandom number:", next_pseudorandom_number)
