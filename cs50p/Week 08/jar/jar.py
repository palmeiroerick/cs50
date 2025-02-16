class Jar():
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return "🍪" * self.size

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 0:
            raise ValueError("Non-positive error")
        else:
            self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if size < 0:
            raise ValueError("Insufficient cookies")
        elif size > self.capacity:
            raise ValueError("Cookie capacity overflow")
        else:
            self._size = size

    def deposit(self, cookies):
        self.size += cookies

    def withdraw(self, cookies):
        self.size -= cookies
