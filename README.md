# Random Numbers

A random number is a number generated by a process, whose outcome is unpredictable, and which cannot be subsequentially reliably reproduced.

## Randomness

What does it mean to be random? It is more defined by what it isn't than what it is. Something that is random means that it has a pattern or it is predictable. Well, that's a real problem for a computer because the entire way that we have designed, architected and built computers is for them to be deterministic.

How could we ever get a computer to be random, if it's always supposed to give a certain output for a given input, that we already know about.

Computers use Pseudorandom Number Generators instead.

**Applications:** <br>
- Cryptography
- Gambling
- Gaming
- Art

Random numbers generated by computers are not random. They are generated based off some algorithm.

# Pseudo-random Number Generators

PRNG stands for "Pseudorandom Number Generator." It is a computer algorithm or process designed to generate a sequence of numbers that appears to be random but is actually determined by a deterministic calculation. In other words, the sequence of numbers generated by a PRNG is not truly random but only exhibits characteristics of randomness, making it suitable for many practical purposes.

PRNGs are widely used in various fields, including computer simulations, cryptography, gaming, and statistical sampling. They are essential in situations where a reliable source of random-like numbers is required but obtaining true randomness is difficult or impractical.

The working principle of a PRNG involves starting with an initial value called a seed, and from that seed, subsequent numbers are generated using a mathematical formula or algorithm. When provided with the same seed, a PRNG will produce the same sequence of numbers every time. This property is useful for reproducibility, as it allows users to recreate the same sequence of "random" numbers when needed.

It's important to note that while PRNGs are sufficient for many applications, they are not suitable for cryptographic purposes or any scenario where high security is required. For cryptographic applications, a different type of random number generator known as a "cryptographically secure PRNG" (CSPRNG) is used, which provides a higher level of unpredictability and security.

**Important properties of good random numbers:** <br>
- Fast
- Portable to different computers
- Have sufficiently long cycle
- Replicable
- Use identical stream of random numbers for different systems (parallel computing)

## Algorithms

### **Middle Square Method (1946, J. von Neumann)**

- Take any integer (seed) of say a 2-digit number.
- Square it and pick the middle two digits and discard the rest.
- Now again square the selected middle two digits in the previous step.
- Repeat.

### **Lehmer Algorithm (1951, D. H. Lehmer)**

- Sometimes also referred to as the Park–Miller random number generator (after Stephen K. Park and Keith W. Miller), is a type of linear congruential generator (LCG) that operates in multiplicative group of integers modulo n. 

$$X_{k+1} = a \cdot X_{k} \mod m$$

where the `modulus m` is a prime number or a power of a prime number, the multiplier a is an element of high multiplicative order modulo `m` (e.g., a primitive root modulo n), and the seed `X`<sub>`0`</sub> is coprime to m.

- Other names are multiplicative linear congruential generator (MLCG) and multiplicative congruential generator (MCG).

**Example:** <br>

Initial seed (starting point): 7 <br>
Multiplier (a): 5 <br>
Modulus (m): 11 <br>

**Most commonly, the modulus is chosen as a prime number.**

**For the Lehmer RNG, the initial seed X<sub>0</sub> must be coprime to the modulus m.**

Formula: seed = (a * seed) % m

seed = (5 * 7) % 11 = 2 <br>
seed = (5 * 2) % 11 = 10 <br>
seed = (5 * 10) % 11 = 6 <br>

Continue this process as many times as needed to generate the sequence of random numbers.

Sequence of random numbers generated using the Lehmer algorithm with these parameters would be: `2, 10, 6, and so on`.

## References
- https://en.wikipedia.org/wiki/Middle-square_method