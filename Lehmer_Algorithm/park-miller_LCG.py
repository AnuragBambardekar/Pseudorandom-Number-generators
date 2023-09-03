def lcg_parkmiller(state):
    state[0] = (state[0] * 48271) % 0x7FFFFFFF
    return state[0]

if __name__ == "__main__":
    initial_state = [12345]
    next_random = lcg_parkmiller(initial_state)
    print(next_random)
