def main():

    while True:
        try:
            height = int(input("Height: "))
            if height < 1 or height > 8:
                print("Only values between 1 and 8")
            else:
                break
        except ValueError:
            print("Only numbers allowed")

    for i in range(height):
        for j in range(height - i - 1):
            print(" ", end="")
        for j in range(i + 1):
            print("#", end="")
        print()


if __name__ == "__main__":
    main()
