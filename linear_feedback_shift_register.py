"""

The most commonly used linear function of single bits is exclusive-or (XOR). Thus, an LFSR is most often a shift register
whose input bit is driven by the XOR of some bits of the overall shift register value.

Applications of LFSRs include generating pseudo-random numbers, pseudo-noise sequences,

https://en.wikipedia.org/wiki/Linear-feedback_shift_register
https://www.youtube.com/watch?v=Ks1pw1X22y4
"""

if __name__ == '__main__':
    state = 0b1001
    for i in range(20):
        print("{:04b}".format(state))
        new_bit = (state ^ (state >> 1)) & 1
        state = (state >> 1) | (new_bit << 3)
