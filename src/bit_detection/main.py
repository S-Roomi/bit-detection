from .bit_create import bitcreate
from bitarray import bitarray

# CHOICES: dict[str:str] = {
    # "1": ""
# }


def to_file(name: str, bits: bitarray) -> None:
    with open(name, 'w') as f:
        f.write(bits.tobytes().hex())

def start():
    n = 2**10 
    test = bitcreate(n)
    
    a = test.n_bits(3, False, 0.75)

    to_file("test.txt", a)
if __name__ == "__main__":
    start()
