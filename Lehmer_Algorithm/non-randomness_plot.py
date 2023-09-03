import matplotlib.pyplot as plt

class LehmerRandomGenerator:
    def __init__(self, seed, multiplier, modulus):
        self.seed = seed
        self.multiplier = multiplier
        self.modulus = modulus

    def generate(self):
        self.seed = (self.multiplier * self.seed) % self.modulus
        return self.seed

if __name__ == "__main__":
    initial_seed = 7
    multiplier =  23 # 16807
    modulus =  401 # 2147483647

    generator = LehmerRandomGenerator(initial_seed, multiplier, modulus)

    num_numbers_to_generate = 500
    lehmer_sequence = []
    for _ in range(num_numbers_to_generate):
        random_number = generator.generate()
        print(random_number)
        lehmer_sequence.append(random_number)

    plt.figure(figsize=(8, 6))
    plt.scatter(lehmer_sequence[:-1], lehmer_sequence[1:], alpha=0.7)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title(f"Lehmer Random Number Generator (a = {multiplier}, m = {modulus})")
    plt.show()

"""
The plot has a pattern, this shows us that the "random" points are not random.
"""