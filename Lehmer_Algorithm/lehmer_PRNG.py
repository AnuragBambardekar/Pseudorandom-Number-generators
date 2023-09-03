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
    multiplier = 5
    modulus = 11

    generator = LehmerRandomGenerator(initial_seed, multiplier, modulus)

    num_numbers_to_generate = 5
    for _ in range(num_numbers_to_generate):
        random_number = generator.generate()
        print(random_number)
