# Random Numbers

A random number is a number generated by a process, whose outcome is unpredictable, and which cannot be subsequentially reliably reproduced.

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