class Jar:
    def __init__(self, capacity: int = 12):
        self.capacity: int = capacity
        self.cookies: int = 0
        ...

    def __str__(self):
        return "🍪" * self.cookies

    def deposit(self, n: int):
        if self.capacity < self.cookies + n:
            raise ValueError("Jar Full!")
        self.cookies += n

    def withdraw(self, n: int):
        if self.cookies - n < 0:
            raise ValueError("Not enough cookies in jar.")
        self.cookies -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity: int):
        if capacity < 0:
            raise ValueError("Capacity can't be negative")
        self._capacity = capacity

    @property
    def size(self):
        return self.cookies


# jar = Jar(10)
# jar.deposit(10)
# jar.withdraw(12)
# print(jar.capacity, jar, jar.size)
