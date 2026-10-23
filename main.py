
from compress import *
from decompress import *
import ast

def save_dictionary_to_file(filename , dictionary):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(repr(dictionary))

def load_dictionary_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return ast.literal_eval(file.read())


def main():
    while True:
        print("\n===== Lossless Compression =====")
        print("1. Compress")
        print("2. Decompress")
        print("3. Exit")

        choice = input("Choose an option: ").strip()
        

        if choice == "1":
            with open("Input.txt", "r", encoding="utf-8") as file:
                data = file.read()
            compressed_data, code, original_code = compress(data)
            padding_lenght= (8-len(compressed_data)%8)%8
            padding_str=compressed_data+('0'*padding_lenght)
            byte_array = bytearray()
            for x in range(0,len(padding_str),8):
                byte_str = padding_str[x:x+8]
                byte_array.append(int(byte_str, 2))

            with open("Compression_output.bin", "wb") as file:
             file.write(byte_array)
            with open("padding.txt","w") as padding_file:
                padding_file.write(str(padding_lenght))
            save_dictionary_to_file("code.txt", {bits: symbol for symbol, bits in code.items()})
            save_dictionary_to_file("original_code.txt", {bits: symbol for symbol, bits in original_code.items()}
)

            print("Compression completed.")
            print("Compressed data saved to Compression_output.bin")

        elif choice == "2":
            bit_by_bit=[]
           
             
            with open("Compression_output.bin", "rb") as file:
                while True:
                    byte = file.read(1)
                    if not byte:
                     break
                    byte_val = byte[0]
                    bits = format(byte_val, '08b')
                    bit_by_bit.extend(bits)

            code_file = load_dictionary_from_file("code.txt")
            original_code_file = load_dictionary_from_file("original_code.txt")
            with open("padding.txt","r") as padding_file:
                padding_lenght= int(padding_file.read())
                if padding_lenght > 0:
                 bit_by_bit = bit_by_bit[:-padding_lenght]

            result = decompress_modified(
                iter(bit_by_bit),
                code_file,
                original_code_file
            )

            with open(
                "Decompression_output.txt", "w", encoding="utf-8"
            ) as file:
                file.write(result)

            print("Decompression completed.")
            print("Output saved to Decompression_output.txt")


        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()