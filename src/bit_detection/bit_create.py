from bitarray import bitarray
import random as rand

# random.getrandbits(k)
# Returns a non-negative Python integer with k random bits. 
# This method is supplied with the Mersenne Twister generator and some other generators may also provide it as an optional part of the API. 
# When available, getrandbits() enables randrange() to handle arbitrarily large ranges.

DEFAULT_BITS: dict[int, bool] = {
    1: False,
    2: False,
    3: False,
    4: False,
    5: False,
    6: False,
    7: False
}


class bitcreate:
    def __init__(self, size: int):
        self.n = size
        rand.seed(1)

    def control(self) -> str:
        """
        Returns random bit stream in hex
        """
        return rand.getrandbits(self.n).to_bytes().hex()

    def n_bits(self, position: int, z: bool, bias: float) -> bitarray:
        """
        ### Function returns a tinkered bit array where every bit at position is biased
            position: 
                add bias to certain part of bit array, i.e 3 means every third bit will be biased
            z: 
                boolean where False represents bias towards zero (0) and True represents bias towards one (1) 
            bias: 
                is percentage chance for certain value to occur (Ex: 0.75 for 75%)
        """

        bits = bitarray(self.n)

        for i in range(self.n):
            odds = rand.random()
            if i % position == 0 and odds <= bias:
                bits[i] = z # bias being either 0 or 1
                continue
            
            bits[i] = rand.getrandbits(1) # randomly pick 0 or 1

        return bits
    
    def n_pos_bits(self, n_list:list[int], z: bool, bias:float) -> bitarray:
        """
        ### Function returns a tinkered bit array where every bit at n positions are biased
            n_list: 
                List of positions to add bias to in bit array, i.e [3, 4, 5] means every third, fourth, and fifth bit will be biased
            z: 
                boolean where False represents bias towards zero (0) and True represents bias towards one (1) 
            bias: 
                is percentage chance for certain value to occur (Ex: 0.75 for 75%)
        """
        bits = bitarray(self.n)

        # TODO: See if its more efficent to make random bit array or continue adding random bit in loop
        
        for i in range(self.n):
            odds = rand.random()
            if odds <= bias:     
                res = [i % n for n in n_list]
                if 0 in res:
                    bits[i] = z
                    continue 
            # if odds is higher than bias or not at any n positions, insert random bit 
            bits[i] = rand.getrandbits(1)

        return bits
    
    def bias_bit(self, bias: float, z: bool = False) -> int:
        odds = rand.random()
        if odds <= bias:
            return 0
        return 1

    def n_pos_bytes(self, positions: list[int], bias: float, bits_to_bias:dict[int, bool] = DEFAULT_BITS) -> bitarray:
        """
        ### Function returns a tinkered bit array where every n bytes has a chance to be biased
        
        """
        bit_array = bitarray(self.n) 
        num_bytes = self.n // 8

        for i in range(0, num_bytes, 8):
            odds = rand.random()
            at_position = [(i // 8) % n for n in positions]
            if 0 in at_position and odds <= bias:
                for j, bit in enumerate(bits_to_bias):
                    bit_array[i + j] = self.bias_bit(bias, bits_to_bias.get(bit, False)) 
                    continue
            bit_array[i: i + 8] = bitarray(rand.randbytes(1))
        return bit_array
