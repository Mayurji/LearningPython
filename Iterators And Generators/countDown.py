class Countdown:
    def __init__(self, start) -> None:
        self.start = start

    # Forward Iterator
    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    # Reverse Iterator
    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1

cnt = Countdown(10)
print([c for c in reversed(cnt)])
