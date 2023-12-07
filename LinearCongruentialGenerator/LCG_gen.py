from collections.abc import Generator

def lcg(modulus: int, a: int, c: int, seed: int) -> Generator[int, None, None]:
    """Linear congruential generator."""
    while True:
        seed = (a * seed + c) % modulus
        yield seed

modulus = 2**31 - 1  # A large prime number often used in LCGs
a = 1103515245
c = 12345
seed = 42

# Create an instance of the LCG generator
lcg_generator = lcg(modulus, a, c, seed)

# Generate and print the first 5 values from the generator
for _ in range(5):
    next_value = next(lcg_generator)
    print(next_value)
