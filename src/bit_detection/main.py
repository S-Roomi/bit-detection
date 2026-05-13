from .bit_create import bitcreate
from bitarray import bitarray
from .imagine_gen import image_generator
from pathlib import Path

PATH = str(Path(__file__).resolve().parents[2])
NOISY_IMAGE_PATH = f'{PATH}/files/noisy_img.png'


def to_file(name: str, bits: bitarray) -> None:
    with open(name, 'w') as f:
        f.write(bits.tobytes().hex())

def bit_create_tests(size: int):
    """
    size:  
        Parameter integer determining bit array size
    """

    # TODO: See if having bias be towards 0 is easier to detect or if having bias be 1 makes detection easier.

    files = [f"file{i}.txt" for i in range(10)]
    
    bc = bitcreate(size)

    # File 0 will be control
    control = bc.control()
    with open(files[0], 'w') as control_file:
        control_file.write(control)
    
    # File 1 will be every third bit manipulated, with 60% chance to be 0
    test1 = bc.n_bits(3, False, 0.6)
    to_file(files[1], test1)

    # File 2 will be every third bit manipulated, with 55% chance to be 0
    test2 = bc.n_bits(3, False, 0.55)
    to_file(files[2], test2)

    # File 3 will be every 2, 4, 6, 8 bits be main, with 80% to be 1
    test3 = bc.n_pos_bits([2, 4, 6, 8], True, 0.8)
    to_file(files[3], test3)
    # File 4 will be every 3, 5, 7, 9  bits be manipulated, with 80% to be 1
    test4 = bc.n_pos_bits([3, 5, 7, 9], True, 0.8)
    to_file(files[4], test4)

    # File 5 will be every 2, 4, 6, 8 bits be main, with 55% to be 1
    test5 = bc.n_pos_bits([2, 4, 6, 8], True, 0.55)
    to_file(files[5], test5)

    # File 6 will be every 3, 5, 7, 9  bits be manipulated, with 55% to be 1
    test6 = bc.n_pos_bits([3, 5, 7, 9], True, 0.55)
    to_file(files[6], test6)

    # File 7 will be every third (3rd) byte will be manipulated
    # Additionally, every bit in the selected byte will be biased towards 0
    test7 = bc.n_pos_bytes([3], 0.55, {0: False, 1: False, 2: False, 3: False, 4: False, 5: False, 6: False, 7: False })
    to_file(files[7], test7)

    # File 8 will be every 2nd, 4th, 6th, 8th byte will be manipulated 
    # Bits 0, 2, 4, 6 will be biased towards 0 
    # Bits 1, 3, 5, 7 will be biased towards 1
    test8 = bc.n_pos_bytes([2, 4, 6, 8], 0.55, {0: False, 1: True, 2: False, 3: True, 4: False, 5: True, 6: False, 7: True })
    to_file(files[8], test8)

    # File 9 will be every 1st, 3rd, 5th, 7th byte will be manipulated 
    # Bits 0, 2, 4, 6 will be biased towards 0 
    # Bits 1, 3, 5, 7 will be biased towards 1
    test9 = bc.n_pos_bytes([1, 3, 5, 7], 0.55, {0: False, 1: True, 2: False, 3: True, 4: False, 5: True, 6: False, 7: True })
    to_file(files[9], test9)

    # TODO 
    # File 10 will be a little weird. Randomly manipulate 3 random positions
    # 
    #  
def start():
    # n = 2**10 
    # test = bitcreate(n)
    
    # a = test.n_bits(3, False, 0.75)

    # to_file("test.txt", a)

    # test = image_generator()
    # noisy_img = test.generate_noisy_image(1080, 1920, NOISY_IMAGE_PATH, True)
    # test.insert_into_image(NOISY_IMAGE_PATH, "Hello World")

    bit_create_tests()

if __name__ == "__main__":
    start()
