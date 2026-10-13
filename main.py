from compress import *
def main():
    while True:
        print("\n===== Lossless Compression =====")
        print("1. Compress")
        print("2. Decompress")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            data=input("Inter Your Data: ")
            compress(data)
            #abcazdafcqdadcuabapd

        elif choice == "2":
            pass

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()