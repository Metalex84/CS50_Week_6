class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Wrong capacity!")
        self._capacity = capacity
        self._size = 0


    def __str__(self):
        return "🍪" * self._size


    def deposit(self, n):
        if self._size + n > self._capacity:
            raise ValueError("Too many cookies in the jar!")
        self._size += n


    def withdraw(self, n):
        if n > self._size:
            raise ValueError("No more cookies in the jar!")
        self._size -= n


    @property
    def capacity(self):
        return self._capacity


    @property
    def size(self):
        return self._size

def main():
    jar = Jar()

    cookies = int(input("How many cookies do you want to deposit? "))
    jar.deposit(cookies)
    print("Depositting...", end=" ")
    print(str(jar))
    print(f"Current capacity = {jar.capacity}")
    print(f"Current size = {jar.size}")

    cookies = int(input("How many cookies do you want to withdraw? "))
    jar.withdraw(cookies)
    print("Withdrawing...", end=" ")
    print(str(jar))
    print(f"Current capacity = {jar.capacity}")
    print(f"Current size = {jar.size}")


main()
