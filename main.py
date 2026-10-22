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

            with open(
                "Compression_output.txt", "w", encoding="utf-8"
            ) as file:
                file.write(compressed_data)

            save_dictionary_to_file("code.txt", {bits: symbol for symbol, bits in code.items()})
            save_dictionary_to_file("original_code.txt", {bits: symbol for symbol, bits in original_code.items()}
)

            print("Compression completed.")
            print("Compressed data saved to Compression_output.txt")

        elif choice == "2":
            with open(
                "Compression_output.txt", "r", encoding="utf-8"
            ) as file:
                compressed_data = file.read().strip()

            code_file = load_dictionary_from_file("code.txt")
            original_code_file = load_dictionary_from_file("original_code.txt")

            result = decompress_modified(
                iter(compressed_data),
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